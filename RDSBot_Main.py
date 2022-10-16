import nest_asyncio
nest_asyncio.apply()
import config
import asyncpraw

async def main():
    reddit = asyncpraw.Reddit(
        user_agent="LMGTFY",
        client_id=config.client_id,
        client_secret=config.client_secret,
        username=config.username,
        password=config.password,
    )

    subreddit = await reddit.subreddit("wallstreetbets")
    print("Test")
    await subreddit.load()
    async for submission in subreddit.hot(limit = 5):
        print ("----------------------------------------")
        print(submission.title)
        await submission.load()
        for comment in submission.comments:
            if hasattr(comment,"body"):
                print("``````````")
                print(comment.body)


if __name__ == "__main__":
    loop = nest_asyncio.events.get_event_loop()
    loop.run_until_complete(main())