import os
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import discord
from discord.ext import commands
from discord import app_commands

# ==========================================
# 1. MINI SERVEUR WEB (Pour Render 24/7)
# ==========================================
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

# ==========================================
# 2. CONFIGURATION DU BOT DISCORD
# ==========================================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Synchronisation des commandes slash sur Discord
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur de synchronisation : {e}")
    print(f'Connecté en tant que {bot.user.name} !')

# ==========================================
# 3. GESTION DES MESSAGES AUTOMATIQUES
# ==========================================
@bot.event
async def on_message(message):
    # Ignorer les messages envoyés par le bot lui-même
    if message.author == bot.user:
        return

    contenu_texte = message.content.lower()

    # Le bot réagit s'il est mentionné ou si "axesinmotion" / des mots clés sont dans le texte
    is_mentioned = bot.user in message.mentions
    has_keyword = "axesinmotion" in contenu_texte

    if is_mentioned or has_keyword:
        reponse = None

        if "how are you" in contenu_texte:
            reponse = random.choice(["good, i'm happy cause ecds hit 1b downloads recently","felling good, my team is so peak btw 😏", "sure, i feel good 🤝", "good👌"])
        elif "capital of albania" in contenu_texte:
            reponse = "tirana!"
        elif "capital of germany" in contenu_texte:
            reponse = "berlin!"
        elif "capital of belgium" in contenu_texte:
            reponse = "brussels!"
        elif "capital of spain" in contenu_texte:
            reponse = "madrid!"
        elif "capital of france" in contenu_texte:
            reponse = "paris!"
        elif "capital of algeria" in contenu_texte:
            reponse = "algiers!"
        elif "capital of cameroon" in contenu_texte:
            reponse = "yaounde!"
        elif "capital of egypt" in contenu_texte:
            reponse = "cairo!"
        elif "capital of morocco" in contenu_texte:
            reponse = "rabat!"
        elif "capital of senegal" in contenu_texte:
            reponse = "dakar!"
        elif "capital of china" in contenu_texte:
            reponse = "beijing!"
        elif "capital of india" in contenu_texte:
            reponse = "new delhi!"
        elif "capital of japan" in contenu_texte:
            reponse = "tokyo!"
        elif "capital of thailand" in contenu_texte:
            reponse = "bangkok!"
        elif "capital of vietnam" in contenu_texte:
            reponse = "hanoi!"
        elif "capital of australia" in contenu_texte:
            reponse = "canberra!"
        elif "capital of fiji" in contenu_texte:
            reponse = "suva!"
        elif "capital of new zealand" in contenu_texte:
            reponse = "wellington!"
        elif "capital of papua new guinea" in contenu_texte:
            reponse = "port moresby!"
        elif "capital of vanuatu" in contenu_texte:
            reponse = "port-vila!"
        elif "capital of south africa" in contenu_texte:
            reponse = "pretoria!"
        elif "capital of ivory coast" in contenu_texte:
            reponse = "yamoussoukro!"
        elif "capital of madagascar" in contenu_texte:
            reponse = "antananarivo!"
        elif "capital of nigeria" in contenu_texte:
            reponse = "abuja!"
        elif "capital of tunisia" in contenu_texte:
            reponse = "tunis!"
        elif "i need something" in contenu_texte:
            reponse = "tell me 🪎"
        elif any(phrase in contenu_texte for phrase in ["what game you like the most", "what's your favorite game"]):
            reponse = random.choice(["ecds, that's so peak!", "extreme car driving simulator, for sure!"])
        elif any(phrase in contenu_texte for phrase in ["what do you think about multi-verse driving simulator","do you like multi-verse driving simulator","do you like mvds", "what do you think about mvds"]):
            reponse = random.choice(["huhhh, yeah i i like it", "bro never heard that game", "bro mvds is my bessst friend"]) 
        elif any(phrase in contenu_texte for phrase in ["what is ecds", "what's ecds"]):
            reponse = random.choice(["the best game 4ever 😏", "a car game, better than all the others xD (even mvds)"])
        elif any(phrase in contenu_texte for phrase in ["how much downloads is ecds", "downloads ecds"]):
            reponse = "1 billon 🔥"
        elif any(phrase in contenu_texte for phrase in ["why your name is like that", "your name is so weird"]):
            reponse = "that's the best name, that's it 😏"
        elif any(phrase in contenu_texte for phrase in ["really", "for real", "is that real", "are you serious"]):  
            reponse = random.choice(["yeah🤌", "oh yeah 🔥", "yes brother"])
        elif any(phrase in contenu_texte for phrase in ["ok", "okay"]):
            reponse = random.choice(["🙃", "👀", "👍"])
        elif any(phrase in contenu_texte for phrase in ["huhh", "what wdym"]):
            reponse = random.choice(["hehe", "jk", "🤌"])
        elif any(phrase in contenu_texte for phrase in ["8.0 out ?", "new ecds update ?"]):
            reponse = random.choice(["later, but peak update will coming 😏", "i just can tell you the update will be peak!"])
        elif any(phrase in contenu_texte for phrase in ["are you the creator of ecds", "is that the creator of ecds acc", "are you axesinmotion"]):
            reponse = random.choice(["i'm not the real axesinmotion, but the best bot version of him!", "dude, i'm AxesinMotionxD, the best bot forever XD"])
        elif "yo" in contenu_texte:
            reponse = random.choice(["yo!", "hi, what's up ?", "hey!"])
        elif "yes" in contenu_texte:
            reponse = random.choice(["w", "ok", "okay"])
        elif "no bro" in contenu_texte:
            reponse = random.choice(["k", "😶", "L"])
        elif any(phrase in contenu_texte for phrase in ["hello", "hey"]):
            reponse = random.choice(["helloo", "yo", "hey!"])
        elif "lagaxesinmotion3" in contenu_texte :
            reponse = "eeee_laaaaagg!!!!-------eEeEEE"
        elif any(phrase in contenu_texte for phrase in ["lol", "lmao", "lmfao"]):
            reponse = random.choice(["hehe", "😎"])
        elif "capital of axesinmotion" in contenu_texte:
            reponse = "me!"
        elif "capital of ecds" in contenu_texte:
            reponse = "axesinmotion 😏"
        
        else:
            # Réponse par défaut
            reponse = random.choice(["yo, do you want to talking", "did you pinged me ?", "Hey 👋", "did someone pinged me ?"])

        if reponse:
            await message.channel.send(reponse)

    await bot.process_commands(message)

# ==========================================
# 4. COMMANDES SLASH
# ==========================================
@bot.tree.command(name="ping", description="Vérifie la latence du bot")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong ! Latence de la passerelle : {latency} ms.")
@bot.tree.command(name="greeting", description="Dis bonjour au bot")
async def bonjour(interaction: discord.Interaction):
    await interaction.response.send_message("hi, i'm axesinmotionxD, let's chat!")
@bot.tree.command(name="mvds", description="Affiche ce que pense le bot du jeu mvds")
async def mvds_cmd(interaction: discord.Interaction):
    await interaction.response.send_message("mvds ? Humm i think it's a pretty good game, but ecds is 1b downloads, so that game is cook xD")
@bot.tree.command(name="axesinmotion", description="Affiche ce qu'est axesinmotion, selon lui")
async def axesinmotion_cmd(interaction: discord.Interaction):
    await interaction.response.send_message("is the best game enterprise, the youtuber vicky lol gaming is famous because of it, and is known throughout the entire world 🗿!")

# ==========================================
# 5. LANCEMENT DU BOT
# ==========================================
TOKEN = os.getenv("DISCORD_TOKEN")

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

threading.Thread(target=run_server, daemon=True).start

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


@bot.event
async def on_ready():
  print(f"Logged in as {bot.user} (ID: {bot.user.id})")
  try:
    synced = await tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

@bot.tree.command(name="quiz", description="Play a multiplayer capital quiz!")
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
        msg = await bot.wait_for("message", check=check, timeout=float(timeout))
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
bot.run(TOKEN)
