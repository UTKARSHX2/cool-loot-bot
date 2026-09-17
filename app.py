import discord
from discord.ext import commands
import random
import os
import json
from datetime import datetime

# 1. Your exact asset loot table database
LOOT_TABLE = [
  {
    "id": "liq_llama",
    "name": "llama spit",
    "type": "liquid",
    "probability_percent": 40,
    "rarity": "uncommon",
    "gold_value": 30,
    "description": "ugh.. what is this llama spit,im not drinking that",
    "sprite_path": "item_llamaspit.png"
  },
  {
    "id": "pet_cat",
    "name": "larry",
    "type": "pet",
    "probability_percent": 0.01,
    "rarity": "GIGACHAD",
    "gold_value": 9999999,
    "description": "caution- larry will be in your closet tonight,he may try to sell himself to destroy the economy,take good care of him",
    "sprite_path": "item_larry.png"
  },
  {
    "id": "tool_case",
    "name": "briefcase",
    "type": "tool",
    "probability_percent": 30,
    "rarity": "uncommon",
    "gold_value": 150,
    "description": "it is a brief case with a note inside it,the note says just,does this mean it is there for just in case",
    "sprite_path": "item_suitcase.png"
  },
  {
    "id": "food_egg",
    "name": "hein's ballz",
    "type": "food",
    "probability_percent": 25,
    "rarity": "uncommon",
    "gold_value": 2,
    "description": "what,who put deez here,de-deez ballz?",
    "sprite_path": "item_egg.png"
  },
  {
    "id": "liq_juice",
    "name": "soda",
    "type": "liquid",
    "probability_percent": 60,
    "rarity": "common",
    "gold_value": 10,
    "description": "its name is soda ,but the id says juice,huh",
    "sprite_path": "item_soda.png"
  },
  {
    "id": "hum_bob",
    "name": "bob",
    "type": "human_item",
    "probability_percent": 1,
    "rarity": "legendary",
    "gold_value": 0,
    "description": "bob the builder , find him,keep him,makes a quick building for you",
    "sprite_path": "item_bob.png"
  },
  {
    "id": "food_uranium",
    "name": "uranium rod",
    "type": "food",
    "probability_percent": 3,
    "rarity": "rare",
    "gold_value": 300,
    "description": "this is what I wanted to eat,finally I can taste it",
    "sprite_path": "item_uraniumrod.png"
  },
  {
    "id": "tool_cloak",
    "name": "cloak",
    "type": "tool",
    "probability_percent": 30,
    "rarity": "uncommon",
    "gold_value": 150,
    "description": "it is a cloak with a frog drawn on it,aww.. so cute",
    "sprite_path": "item_frogcloak.png"
  },
  {
    "id": "mat_chip",
    "name": "CPU chip",
    "type": "material",
    "probability_percent": 1,
    "rarity": "rare",
    "gold_value": 200,
    "description": "provides a 67GHz speed for a lightning fast brainrot",
    "sprite_path": "item_CPU.png"
  },
  {
    "id": "food_bag",
    "name": "food bag",
    "type": "food",
    "probability_percent": 55,
    "rarity": "common",
    "gold_value": 10,
    "description": "it is... a food bag?",
    "sprite_path": "item_foodbag.png"
  },
  {
    "id": "food_bread",
    "name": "baugette",
    "type": "food",
    "probability_percent": 100,
    "rarity": "common",
    "gold_value": 100,
    "description": "look its a baugette,I'll go tell teto",
    "sprite_path": "item_baugette.png"
  },
  {
    "id": "liq_acid",
    "name": "green acid",
    "type": "liquid",
    "probability_percent": 30,
    "rarity": "uncommon",
    "gold_value": 50,
    "description": "this suspiciously reminds me of that cunning fox",
    "sprite_path": "item_acid.png"
  },
  {
    "id": "food_pick",
    "name": "pickle",
    "type": "food",
    "probability_percent": 20,
    "rarity": "uncommon",
    "gold_value": 60,
    "description": "aww man,I thought it was cucumbe- I meant oh man so good we god something delicious",
    "sprite_path": "item_pickle.png"
  },
  {
    "id": "food_pow",
    "name": "white powder",
    "type": "food",
    "probability_percent": 60,
    "rarity": "common",
    "gold_value": 40,
    "description": "yup this powder is glucose powder,not the other one",
    "sprite_path": "item_powder.png"
  },
  {
    "id": "food_rice",
    "name": "bowl of rice",
    "type": "food",
    "probability_percent": 5,
    "rarity": "rare",
    "gold_value": 75,
    "description": "tastes like asia,fills you with the power of da dragon worria",
    "sprite_path": "item_ricebowl.png"
  },
  {
    "id": "mat_book",
    "name": "maths book",
    "type": "material",
    "probability_percent": 35,
    "rarity": "uncommon",
    "gold_value": 35,
    "description": "i know you want to throw this in lava but it is important to make you a great dragon worria",
    "sprite_path": "item_maths.png"
  },
  {
    "id": "tool_stick",
    "name": "glue stick",
    "type": "tool",
    "probability_percent": 20,
    "rarity": "uncommon",
    "gold_value": 20,
    "description": "might fix your relationship",
    "sprite_path": "item_gluestick.png"
  },
  {
    "id": "tool_belt",
    "name": "leather belt",
    "type": "tool",
    "probability_percent": 1,
    "rarity": "rare",
    "gold_value": 200,
    "description": "made from the fine leather farmed by the ancient worrias",
    "sprite_path": "item_leatherbelt.png"
  },
  {
    "id": "liq_beer",
    "name": "beer",
    "type": "liquid",
    "probability_percent": 20,
    "rarity": "uncommon",
    "gold_value": 30,
    "description": "this caused a man to unalive a deer",
    "sprite_path": "item_beer.png"
  },
  {
    "id": "mys_wing",
    "name": "wing",
    "type": "mysterious",
    "probability_percent": 0.5,
    "rarity": "legendary",
    "gold_value": 666,
    "description": "ill go and wingmy ding till it becomes a black hole",
    "sprite_path": "item_wing.png"
  },
  {
    "id": "pet_llama",
    "name": "llama",
    "type": "pet",
    "probability_percent": 20,
    "rarity": "uncommon",
    "gold_value": 100,
    "description": "is this the one who gave the spit to seal in bottles",
    "sprite_path": "item_llama.png"
  },
  {
    "id": "mat_metal",
    "name": "metal",
    "type": "material",
    "probability_percent": 70,
    "rarity": "common",
    "gold_value": 30,
    "description": "no matter how you try,you cannot know what metal it is",
    "sprite_path": "item_metal.png"
  },
  {
    "id": "tool_jar",
    "name": "jar",
    "type": "tool",
    "probability_percent": 65,
    "rarity": "common",
    "gold_value": 45,
    "description": "might be used to fill something,I wonder what",
    "sprite_path": "item_jar.png"
  },
  {
    "id": "bon_sub",
    "name": "subscribe",
    "type": "bonus",
    "probability_percent": 2,
    "rarity": "legendary",
    "gold_value": 0,
    "description": "youtubers might use it always",
    "sprite_path": "item_subscribe.png"
  }
]

DATA_FILE = "user_data.json"
MAX_SLOTS = 20

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

USER_DATA = load_data()

def get_user_profile(user_id):
    uid_str = str(user_id)
    if uid_str not in USER_DATA:
        USER_DATA[uid_str] = {"gold": 0, "inventory": []}
    return USER_DATA[uid_str]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} and ready for unhinged chaos!")

# Cooldown error handler to catch spamming attempts gracefully
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        seconds = round(error.retry_after, 1)
        unhinged_cooldown_messages = [
            f"🛑 Chill out! Your hands are shaking. Wait `{seconds}s` before chasing that dopamine rush again.",
            f"❌ Economy protection triggered! You are looting too fast. Try again in `{seconds}s`.",
            f"⏳ Whoa there speedrunner, calm down. Your cooldown ends in `{seconds}s`."
        ]
        await ctx.send(random.choice(unhinged_cooldown_messages))
    else:
        raise error

# 2-minute cooldown system to completely stop spam exploits
@bot.command()
@commands.cooldown(1, 7200, commands.BucketType.user)
async def loot(ctx):
    user_id = ctx.author.id
    profile = get_user_profile(user_id)
    
    if len(profile["inventory"]) >= MAX_SLOTS:
        ctx.command.reset_cooldown(ctx) # Refund cooldown if slots are full
        await ctx.send(f"❌ **Your hoard is overflowing ({len(profile['inventory'])}/{MAX_SLOTS})!** Use `!sell <item name>` to clean space.")
        return

    weights = [item["probability_percent"] for item in LOOT_TABLE]
    chosen_item = random.choices(LOOT_TABLE, weights=weights, k=1)[0]
    
    profile["inventory"].append(chosen_item["id"])
    save_data(USER_DATA)

    rarity_colors = {
        "common": 0x95a5a6,      
        "uncommon": 0x2ecc71,    
        "rare": 0x3498db,        
        "legendary": 0x9b59b6,   
        "gigachad": 0xe74c3c     
    }
    color = rarity_colors.get(chosen_item["rarity"].lower(), 0xffffff)

    image_file_path = f"icons/{chosen_item['sprite_path']}"
    file = None
    thumbnail_url = None
    
    if os.path.exists(image_file_path):
        file = discord.File(image_file_path, filename=chosen_item['sprite_path'])
        thumbnail_url = f"attachment://{chosen_item['sprite_path']}"

    embed = discord.Embed(
        title=f"🎁 {chosen_item['name'].upper()}",
        description=f"*{chosen_item['description']}*",
        color=color
    )
    embed.add_field(name="Rarity", value=f"`{chosen_item['rarity'].upper()}`", inline=True)
    embed.add_field(name="Type", value=chosen_item["type"].title(), inline=True)
    embed.add_field(name="Value", value=f"💰 {chosen_item['gold_value']} Gold", inline=True)
    
    if thumbnail_url:
        embed.set_thumbnail(url=thumbnail_url)
        
    slots_used = len(profile["inventory"])
    embed.set_footer(text=f"Rolled by {ctx.author.name} | Bag: {slots_used}/{MAX_SLOTS}")

    if file:
        await ctx.send(file=file, embed=embed)
    else:
        await ctx.send(embed=embed)

@bot.command()
async def inv(ctx):
    user_id = ctx.author.id
    profile = get_user_profile(user_id)
    inventory = profile["inventory"]
    
    slots_used = len(inventory)
    if slots_used == 0:
        embed = discord.Embed(title=f"🎒 {ctx.author.name}'s Bag", description="Completely empty. Run `!loot` to find some junk.", color=0x95a5a6)
        embed.add_field(name="Wallet Balance", value=f"💰 {profile['gold']} Gold")
        await ctx.send(embed=embed)
        return

    item_counts = {}
    for item_id in inventory:
        item_counts[item_id] = item_counts.get(item_id, 0) + 1
        
    inv_desc = ""
    for item_id, count in item_counts.items():
        item_meta = next((i for i in LOOT_TABLE if i["id"] == item_id), None)
        if item_meta:
            inv_desc += f"• **{item_meta['name'].upper()}** x{count} (`{item_meta['rarity'].upper()}` | Value: {item_meta['gold_value']}g each)
"

    embed = discord.Embed(
        title=f"🎒 {ctx.author.name}'s Storage",
        description=inv_desc,
        color=0x3498db
    )
    embed.add_field(name="Net Wealth", value=f"💰 {profile['gold']} Gold", inline=True)
    embed.add_field(name="Storage Slots", value=f"📦 `{slots_used}/{MAX_SLOTS}` Slots", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def sell(ctx, *, item_name: str = None):
    if not item_name:
        await ctx.send("⚠️ Usage: `!sell <item name>` (e.g. `!sell soda`)")
        return

    user_id = ctx.author.id
    profile = get_user_profile(user_id)
    inventory = profile["inventory"]

    target_item = next((i for i in LOOT_TABLE if i["name"].lower() == item_name.lower()), None)
    
    if not target_item or target_item["id"] not in inventory:
        await ctx.send(f"❌ You don't have any '{item_name}' in your bag.")
        return

    inventory.remove(target_item["id"])
    profile["gold"] += target_item["gold_value"]
    save_data(USER_DATA)

    await ctx.send(f"💰 Sold 1x **{target_item['name'].upper()}** for **{target_item['gold_value']} Gold**. Bag space: `{len(inventory)}/{MAX_SLOTS}`")

@bot.command()
async def leaderboard(ctx):
    if not USER_DATA:
        await ctx.send("The leaderboard is currently empty.")
        return

    # Sort users by gold value descending
    sorted_users = sorted(USER_DATA.items(), key=lambda x: x[1].get("gold", 0), reverse=True)[:10]
    
    leaderboard_text = ""
    for index, (uid, data) in enumerate(sorted_users, 1):
        try:
            user = await bot.fetch_user(int(uid))
            name = user.name
        except Exception:
            name = f"Unknown User ({uid})"
        leaderboard_text += f"{index}. **{name}** - 💰 {data.get('gold', 0)} Gold
"

    embed = discord.Embed(
        title="🏆 Global Wealth Leaderboard",
        description=leaderboard_text,
        color=0xf1c40f
    )
    await ctx.send(embed=embed)

bot.run("MTU1MDEwOTYwMTk0NzQ1NTY0OA.G2t4jD.cJD9vg5qJLyT3JFKg7eL7w2dEW94wnUSt6iYLY")

@loot.error
async def loot_error(ctx, error):
    """Catches the 2-hour cooldown trigger and handles it gracefully."""
    if isinstance(error, commands.CommandOnCooldown):
        # Convert the remaining cooldown seconds into hours and minutes
        minutes, seconds = divmod(int(error.retry_after), 60)
        hours, minutes = divmod(minutes, 60)
        
        # Build out a funny, chaotic rejection message matching your bot's theme
        if hours > 0:
            time_left = f"{hours}h {minutes}m"
        else:
            time_left = f"{minutes}m {seconds}s"
            
        unhinged_replies = [
            f"❌ **Back off!** Your hands are trembling from brainrot. Wait another `{time_left}`.",
            f"🛑 **DENIED.** Hein's ballz aren't ready to drop yet. Try again in `{time_left}`.",
            f"⚠️ **Woah there, speedrunner.** Go touch some grass or look for Larry in your closet. `{time_left}` remaining."
        ]
        
        await ctx.send(random.choice(unhinged_replies))
    else:
        # If it's a completely different error, raise it normally so you can debug it
        raise error
