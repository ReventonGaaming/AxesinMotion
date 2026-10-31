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
        elif any(phrase in contenu_texte for phrase in ["are you the creator of ecds", "is that the creator of ecds acc", "are you axesinmotion", "you created ecds"]):
            reponse = random.choice(["i'm not the real axesinmotion, but the best bot version of him!", "dude, i'm AxesinMotionxD, the best bot forever XD"])
        elif "yo" in contenu_texte:
            reponse = random.choice(["yo!", "hi, what's up ?", "hey!"])
        elif "yes" in contenu_texte:
            reponse = random.choice(["w", "ok", "okay"])
        elif "no" in contenu_texte:
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
        elif "bro" in contenu_texte:
            reponse = random.choice(["what", "wha"])
        elif any(phrase in contenu_texte for phrase in ["hi", "hai"]):
            reponse = random.choice(["hi👋", "hii"])
        elif "of course" in contenu_texte:
            reponse = random.choice(["yay 👏, what you want to talk?", "okay! so what for chatting ?"])
        elif "idk" in contenu_texte:
            reponse = random.choice(["hummm, ok.. do you know axesinmotion team is real peak?", "oh.. do you know the capital of france is paris?"])
        
        else:
            # Réponse par défaut
            reponse = random.choice(["yo, do you want to talking", "did you pinged me ?", "Hey 👋", "did someone pinged me ?"])

        if reponse:
            await message.channel.send(reponse)

    await bot.process_commands(message)

# ==========================================
# 4. COMMANDES SLASH
# ==========================================

@bot.tree.command(name="questions", description="Affiche toutes les questions et réponses du bot")
async def questions_cmd(interaction: discord.Interaction):
    # Liste de tes questions et réponses (tu pourras l'agrandir facilement ici)
    qa_list = [
        ("Are you the creator of ecds", "i'm not the real axesinmotion, the best bot version of him!"),
        ("capital of france", "paris"),
        ("mvds", "Mvds ? Hmm i think it's a pretty good game, but everyone has their opinion!"),
        ("how are you", "good / happy cause ecds...")
    ]
    
    # Construction du message texte
    texte = "**📋 Liste des questions / réponses de mon code :**\n"
    for question, reponse in qa_list:
        texte += f"• **Question :** `{question}` ➔ **Réponse :** `{reponse}`\n"
    
    # ephemeral=True rend le message visible UNIQUEMENT par la personne qui a tapé la commande
    await interaction.response.send_message(texte, ephemeral=True)
    
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

# Récupération sécurisée du token via les variables d'environnement
bot.run(TOKEN)
