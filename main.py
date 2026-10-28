import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"AxesInMotion Bot is alive!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()
import asyncio
import os
import random
import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Base de données complète des pays par continent
QUIZ_DATA = {
    "Europe": {
        "france": "paris",
        "germany": "berlin",
        "spain": "madrid",
        "italy": "rome",
        "united kingdom": "london",
        "netherlands": "amsterdam",
        "sweden": "stockholm",
        "switzerland": "bern",
        "poland": "warsaw",
        "belgium": "brussels",
        "austria": "vienna",
        "norway": "oslo",
        "denmark": "copenhagen",
        "finland": "helsinki",
        "ireland": "dublin",
        "czech republic": "prague",
        "hungary": "budapest",
        "romania": "bucharest",
        "ukraine": "kyiv",
        "croatia": "zagreb",
        "slovakia": "bratislava",
        "greece": "athens",
        "portugal": "lisbon",
    },
    "Asia": {
        "japan": "tokyo",
        "china": "beijing",
        "south korea": "seoul",
        "india": "new delhi",
        "thailand": "bangkok",
        "vietnam": "hanoi",
        "indonesia": "jakarta",
        "philippines": "manila",
        "saudi arabia": "riyadh",
        "turkey": "ankara",
        "malaysia": "kuala lumpur",
        "singapore": "singapore",
        "pakistan": "islamabad",
        "bangladesh": "dhaka",
        "iran": "tehran",
    },
    "Africa": {
        "egypt": "cairo",
        "south africa": "pretoria",
        "nigeria": "abuja",
        "kenya": "nairobi",
        "senegal": "dakar",
        "morocco": "rabat",
        "algeria": "algiers",
        "tunisia": "tunis",
        "ghana": "accra",
        "ethiopia": "addis ababa",
        "tanzania": "dodoma",
        "uganda": "kampala",
        "rwanda": "kigali",
        "cameroon": "yaounde",
        "angola": "luanda",
        "zimbabwe": "harare",
        "zambia": "lusaka",
        "madagascar": "antananarivo",
        "ivory coast": "yamoussoukro",
    },
    "Americas": {
        "united states": "washington d.c.",
        "canada": "ottawa",
        "brazil": "brasilia",
        "argentina": "buenos aires",
        "mexico": "mexico city",
        "colombia": "bogota",
        "peru": "lima",
        "chile": "santiago",
        "cuba": "havana",
        "jamaica": "kingston",
        "venezuela": "caracas",
        "ecuador": "quito",
        "bolivia": "sucre",
        "uruguay": "montevideo",
        "paraguay": "asuncion",
        "costa rica": "san jose",
        "panama": "panama city",
        "dominican republic": "santo domingo",
        "haiti": "port-au-prince",
        "guatemala": "guatemala city",
    },
    "Oceania": {
        "australia": "canberra",
        "new zealand": "wellington",
        "fiji": "suva",
        "papua new guinea": "port moresby",
        "vanuatu": "port vila",
        "samoa": "apia",
        "tonga": "nuku'alofa",
        "solomon islands": "honiara",
        "palau": "ngerulmud",
        "kiribati": "tarawa",
        "micronesia": "palikir",
        "marshall islands": "majuro",
        "nauru": "yaren",
        "tuvalu": "funafuti",
    },
}


@client.event
async def on_ready():
  print(f"Logged in as {client.user} (ID: {client.user.id})")
  try:
    synced = await tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


@tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):
  latency = round(client.latency * 1000)
  await interaction.response.send_message(
      f"Pong! Gateway latency: {latency} ms."
  )


@tree.command(name="greeting", description="Greet the bot")
async def greeting(interaction: discord.Interaction):
  await interaction.response.send_message(
      f"Hi, I'm {client.user.name}, let's chat!"
  )


@tree.command(name="quiz", description="Play a multiplayer capital quiz!")
@app_commands.describe(
    rounds="Number of rounds (max 30, default 10)",
    timeout="Time per question in seconds (max 30, default 10)",
    continent="Choose a specific continent or All",
)
@app_commands.choices(
    continent=[
        app_commands.Choice(name="All (Worldwide)", value="All"),
        app_commands.Choice(name="Europe", value="Europe"),
        app_commands.Choice(name="Asia", value="Asia"),
        app_commands.Choice(name="Africa", value="Africa"),
        app_commands.Choice(name="Americas", value="Americas"),
        app_commands.Choice(name="Oceania", value="Oceania"),
    ]
)
async def quiz(
    interaction: discord.Interaction,
    rounds: int = 10,
    timeout: int = 10,
    continent: app_commands.Choice[str] = None,
):
  # Blocage des valeurs maximales à 30
  rounds = max(1, min(rounds, 30))
  timeout = max(5, min(timeout, 30))
  selected_continent = continent.value if continent else "All"

  # Sélection du bassin de pays
  pool = {}
  if selected_continent == "All":
    for c_data in QUIZ_DATA.values():
      pool.update(c_data)
  else:
    pool = QUIZ_DATA.get(selected_continent, {})

  if not pool:
    await interaction.response.send_message(
        "No countries found for this continent!", ephemeral=True
    )
    return

  actual_rounds = min(rounds, len(pool))

  await interaction.response.send_message(
      f"🎮 **MULTIPLAYER QUIZ STARTED!**\n"
      f"🌍 **Region:** {selected_continent} | 📌 **Rounds:** {actual_rounds} |"
      f" ⏱️ **Time:** {timeout}s\n"
      f"Everyone can answer in the chat!"
  )

  scores = {}
  positive_reactions = ["yes!", "yeah!", "right!", "true!"]
  negative_reactions = ["no", "fake", "not true 😶"]

  # Anti-doublon strict avec random.sample
  selected_items = random.sample(list(pool.items()), actual_rounds)

  for manche, (country, capital) in enumerate(selected_items, 1):
    await interaction.channel.send(
        f"\n📍 **Round {manche}/{actual_rounds}** : What is the capital of"
        f" **{country.title()}** ?"
    )

    def check(m):
      return m.channel == interaction.channel and not m.author.bot

    try:
      while True:
        msg = await client.wait_for("message", check=check, timeout=float(timeout))
        if msg.content.strip().lower() == capital.lower():
          player = msg.author
          scores[player] = scores.get(player, 0) + 1
          reaction = random.choice(positive_reactions)
          await interaction.channel.send(
              f"✅ {reaction} {player.mention} got it right!"
          )
          break
    except asyncio.TimeoutError:
      reaction = random.choice(negative_reactions)
      await interaction.channel.send(
          f"⏰ Time's up! {reaction} (The answer was: **{capital.title()}**)"
      )

  # Leaderboard final
  if not scores:
    await interaction.channel.send(
        "\n🏆 **GAME OVER !** No one scored any points!"
    )
  else:
    ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    leaderboard_text = "\n🏆 **FINAL LEADERBOARD** 🏆\n"
    medals = ["🥇", "🥈", "🥉"]

    for index, (player, score) in enumerate(ranking):
      prefix = medals[index] if index < 3 else f"#{index + 1}"
      leaderboard_text += f"{prefix} {player.mention} : **{score} pt(s)**\n"

    await interaction.channel.send(leaderboard_text)


# Récupération sécurisée du token via les variables d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
