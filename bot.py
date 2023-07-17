import discord
import responses

# Needed in order to start the client
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#function to send a message and uses responses.py
async def send_message(message, user_message, is_private):
	try:
		response = responses.get_response(user_message)
		if is_private:
			await message.author.send(response)
		else:
			await message.channel.send(response)
			
	except Exception as e:
		print(e)

# Message for when the client is ready
@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')
	
# On message from the discord server
@client.event
async def on_message(message):
	if message.author == client.user:
		return
		
	username = str(message.author)
	user_message = str(message.content)
	channel = str(message.channel)
	
	print(f"{username} said: '{user_message}' ({channel})")
	
	if user_message[0] == '?':
		user_message = user_message[1:]
		await send_message(message, user_message, is_private=True)
		
	else:
		await send_message(message, user_message, is_private=False)

# Run the client with the bot tokenh		
client.run('MTEyOTU2MDYzODg4NTIwODE2NQ.GhzPC5.PzuJ9qDpdiyYzXx6M4iTgFeQQvTVGC3udHSxiM')
