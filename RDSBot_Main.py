import nest_asyncio
nest_asyncio.apply()
import config
import asyncpraw
import RedditFiles

async def main():
    reddit = await RedditFiles.bot_login()
    subreddit = await reddit.subreddit("wallstreetbets")
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
    return


if __name__ == "__main__":
    loop = nest_asyncio.events.get_event_loop()
    loop.run_until_complete(main())