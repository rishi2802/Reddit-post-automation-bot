import praw
import time
import re

reddit = praw.Reddit(
    client_id="zZduCWLpVkrIFi1LME395A",
    client_secret="vAysRgcLKUgoLsv9D05NKAEw-zyBjA",
    password="EliteIntern@23",
    user_agent="stablecoin by /u/cyptoddict2947",
    username="cyptoddict2947",
)

print(reddit.read_only)  # Output: False

subreddits = ['NoRules']

title = "Beyond Bitcoin: Discover the Hidden Gems of Stablecoin - Your Key to Thriving in the Cryptoverse!"
image_path = "C://Users//rishi//Pictures//Screenshots//stablecoin.png" #place the path to the image here.
selftext = '''
Place the head comment here. this comment will be marked as OP. It is important to note that if the post contains a picture then the body of the post can not contain text and vice versa
'''

count = 0
submission_ids = []  # List to store submission IDs



for subreddit in subreddits:
    
    try:
        count += 1
        submission = reddit.subreddit(subreddit).submit_image(title=title, image_path=image_path, flair_id=None, flair_text=None, send_replies=False)
        submission.reply(selftext)
        submission_ids.append(submission.id)  # Add submission ID to the list

        print("The submission id is:", submission.id)
        print("Posted to", subreddit, "- Post", count, "of", len(subreddits))
       
    except praw.exceptions.RedditAPIException as exception:
        for subexception in exception.items:
            if subexception.error_type == "RATELIMIT":
                wait = re.search(r"\d+", subexception.message).group()  # Extract the waiting time from the error message
                wait = int(wait) * 60 
                print("waiting for ",wait + 60, "seconds")
                time.sleep(wait)  # Pause the script for the required duration
                wait = 1
                time.sleep(wait*60)
              
        submission = reddit.subreddit(subreddit).submit_image(title=title, image_path=image_path, flair_id=None, flair_text=None, send_replies=False)
        submission.reply(selftext)
        print("The submission id is:", submission.id)
        print("Posted to", subreddit, "- Post", count, "of", len(subreddits))  

print("All submission IDs:", submission_ids)

