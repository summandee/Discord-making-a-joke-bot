import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

bye_statements =["bye","Bye", "cya" , "Cya"]

hello_statements = ["hello","Hello","wsp","sup",'Hi',"Sup"]

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing","depression"]

starter_encouragements = [
        "It's ok man relax and just watch some hentai lol im joking",
    "Cheer up man!!", "Time will pass dont worry" , "Never give up","Go and watch some anime that will cheer you up :)","Haha keep crying like a girl"
]

def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=religious&type=twopart")
  json_data = json.loads(response.text)
  joke = json_data["joke"]
  return(joke)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("joke"):
    joke = get_joke()
    await message.channel.send(joke)

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
  
  if any(word in message.content for word in(hello_statements)):
    await message.channel.send('Hey there,I hope you are doing well :)')

  if message.content.startswith("hi"):
    await message.channel.send("Hey there,I hope you are doing well :)")
    
  if message.content.startswith("!list"):
    await message.channel.send(starter_encouragements)
  
  if message.content.startswith('sus'):
   await message.channel.send('sussy baka')
  
  if any(word in message.content for word in bye_statements):
     await message.channel.send("Bye, see you later!")
  
  if message.content.startswith("lol"):
    await message.channel.send("lol")
  
  if message.content.startswith("stfu"):
    await message.channel.send("no")
    
  
  
keep_alive()
client.run(os.environ['TOKEN'])
