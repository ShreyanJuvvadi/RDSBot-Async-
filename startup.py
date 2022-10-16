import asyncpraw
import config

async def bot_login():
	print ("Logging in...")
	reddit = asyncpraw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "Rando Test Bot")
	print ("Logged in!")
	return reddit