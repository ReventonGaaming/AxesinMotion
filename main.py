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
            reponse = random.choice([
                "good, i'm happy cause ecds hit 1b downloads recently",
                "felling good, my team is so peak btw 😏",
                "sure",
                "sure 🤝"
            ])
        elif "i need something" in contenu_texte:
            reponse = "tell me 🪎"
        elif "what game you like the most" in contenu_texte:
            reponse = random.choice([
                "ecds, that's so peak!",
                "extreme car driving simulator, for sure!"
            ])
        elif any(phrase in contenu_texte for phrase in [
            "what you think about multi-verse driving simulator",
            "do you like multi-verse driving simulator",
            "do you like mvds",
            "what you think about mvds",
            "is multi-verse driving simulator your friend",
            "is mvds your friend"]):
            reponse = random.choice([
                "huhhh, yeah i i like it",
                "oiia oiia",
                "never heard that game",
                "bro mvds is my bessst friend"]) 
        elif any(phrase in contenu_texte for phrase in ["what is ecds", "what's ecds"]):
            reponse = random.choice([
                "the best game 4ever 😏",
                "a car game, better than all the others xD (even mvds)"])
        elif any(phrase in contenu_texte for phrase in ["how much downloads is ecds", "downloads ecds"]):
            reponse = "1 billon 🔥"
        elif any(phrase in contenu_texte for phrase in ["why your name is like that", "what mean axesinmotion", "what is axesinmotion"]):
            reponse = "i have the best name that's it 😏"
        elif any(phrase in contenu_texte for phrase in ["really", "for real", "that's real", "are you serious"]):
            reponse = random.choice(["yeah🤌", "oh yeah 🔥", "yes brother"])
        elif any(phrase in contenu_texte for phrase in ["ok", "ah", "oh", "okay"]):
            reponse = random.choice(["🙃", "👀", "👍"])
        elif any(phrase in contenu_texte for phrase in ["huh", "huhh", "what"]):
            reponse = random.choice(["hehe", "jk", "🤌"])
        elif any(phrase in contenu_texte for phrase in ["8.0 out ?", "new ecds update ?"]):
            reponse = random.choice(["later, but peak update will coming 😏",
                "i just can tell you the update will be peak!"])
        elif "yo" in contenu_texte:
            reponse = random.choice(["yo!", "hi, what's up ?", "hey!"])
        elif "yes" in contenu_texte:
            reponse = random.choice(["w", "ok", "okay"])
        elif "no" in contenu_texte:
            reponse = random.choice(["k", "😶", "L"])
        elif any(phrase in contenu_texte for phrase in ["hi", "hello", "hey"]):
            reponse = random.choice(["helloo", "yo" or "hey!"])
        elif "lagaxesinmotion2" in contenu_texte :
            reponse = "eeeelaaaaaggdhhglgflfghhh"
        elif any(phrase in contenu_texte for phrase in [lol, lool, lmao, lmfao]):
            reponse = random.choice(["hehe" or "😎"])
        else:
            # Réponse par défaut
            reponse = random.choice([
                "yo, do you want to talking",
                "did you pinged me ?",
                "Hey 👋",
                "did someone pinged me ?"
            ])

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
    await interaction.response.send_message("mvds ? Humm i think it's a pretty good game, but ecds have 1b downloads, so that game is cook xD")
@bot.tree.command(name="axesinmotion", description="Affiche ce qu'est axesinmotion, selon lui")
async def axesinmotion_cmd(interaction: discord.Interaction):
    await interaction.response.send_message("is the best game enterprise, the youtuber vicky lol gaming is famous because of it, and is known throughout the entire world 🗿!")
    
    import asyncio
import random

# Your quiz questions database (Country : Capital)
QUESTIONS_QUIZ = {
    "france": "paris",
    "germany": "berlin",
    "spain": "madrid",
    "italy": "rome",
    "japan": "tokyo"
}

@bot.tree.command(name="quiz", description="Play a capital quiz without duplicate questions!")
async def quiz_cmd(interaction: discord.Interaction):
    # Create a copy of the available countries for this specific game session
    available_countries = list(QUESTIONS_QUIZ.keys())
    
    # Number of questions per game session (e.g., 3 questions)
    number_of_questions = 3
    score = 0
    
    await interaction.response.send_message("🎮 **Quiz Started!** Get ready for some questions...")

    def check(m):
        return m.channel == interaction.channel and not m.author.bot

    for i in range(number_of_questions):
        if not available_countries:
            break # Stop if there are no countries left
            
        # Pick a random country from the remaining ones
        country = random.choice(available_countries)
        
        # IMPORTANT: Remove it from the list so it won't repeat in this game!
        available_countries.remove(country)
        
        expected_capital = QUESTIONS_QUIZ[country]
        
        # Ask the question
        await interaction.followup.send(f"🌍 **Question {i+1}** : What is the capital of **{country}**? *(You have 15 seconds!)*")
        
        try:
            user_message = await bot.wait_for('message', timeout=15.0, check=check)
            
            if user_message.content.lower() == expected_capital:
                score += 1
                await interaction.followup.send(f"🎉 Correct answer! (+1 point)")
            else:
                await interaction.followup.send(f"❌ Incorrect! The correct answer was **{expected_capital}**.")
                
        except asyncio.TimeoutError:
            await interaction.followup.send(f"⏰ Time's up! Nobody answered. The correct answer was **{expected_capital}**.")
            
        # Small 2-second pause before the next question
        await asyncio.sleep(2)

    # End of the quiz
    await interaction.followup.send(f"🏆 **Quiz Over!** Final score: **{score}/{number_of_questions}**")
    

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
