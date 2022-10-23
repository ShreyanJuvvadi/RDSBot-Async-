import asyncpraw
import config

async def main():
    reddit = await bot_login()  #logs in
    subreddit = await reddit.subreddit(config.UserSubreddit)
    print("Test")
    await subreddit.load()
    async for submission in subreddit.hot(limit = 1):
        print ("----------------------------------------")
        print(submission.title)
        await submission.load()
        async for comment in submission.comments:
            if hasattr(comment,"body"):
                print("``````````")
                print(comment.body)
    await reddit.close();   #logs out
    return

async def bot_login():
	print ("Logging in...")
	reddit = asyncpraw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = config.useragent)
	print ("Logged in!")
	return reddit