import nest_asyncio
nest_asyncio.apply()
import config
import asyncpraw
import RedditFiles
import time
import datetime

loopnumber = 1      #global variable for infinite while loop
endcondition = 0    #endcondtion for the infinite while loop to terminate the program
OldTime = int(round(time.time()*1000))

print(OldTime)

while (endcondition != 1):
    CurrentTime = int(round(time.time()*1000))
    if OldTime < CurrentTime - 5000:
        if __name__ == "__main__":
            loop = nest_asyncio.events.get_event_loop()
            loop.run_until_complete(RedditFiles.main())
        OldTime = int(round(time.time()*1000))
    time.sleep(1)
    print(loopnumber)
    loopnumber = loopnumber + 1