#this code is to post to multiple subbredits 
import praw
import time
import re

reddit = praw.Reddit(
    client_id="**************",
    client_secret="*********",
    password="******",
    user_agent="stablecoin by /u/**********",
    username="******",
)

print(reddit.read_only)  # Output: False

subreddits = ['books', 'ethereum', 'selfpublish', 'writing', 'cryptotrading', 'altcoin', 'CryptoTechnology', 'business', 'Entrepreneur', 'smallbusiness', 'marketing', 'Accounting', 'consulting', 'scifi', 'bookclub', 'suggestmeabook', 'HistoryBooks', 'sciencefiction']

title = "Let's Talk Stablecoins: The Future of Finance?"
selftext = '''
Hey Redditors!

Has anyone had the chance to read "The Stablecoin Book: Exploring the Cryptoverse's Untold Stories" by Dr. Christopher William Smithmyer? I stumbled upon it recently and found it quite intriguing. The book delves into the fascinating realm of stablecoins, their role in the cryptocurrency ecosystem, and their potential impact on financial freedom.

I'd love to hear your thoughts on stablecoins and their significance in the ever-changing cryptoverse. How do you see stablecoins contributing to the future of finance and wealth accessibility? Let's share our insights and engage in an exciting discussion! 🌐💡

(Note: This is not a promotion, just a genuine curiosity to discuss the topic!)


'''

count = 0
submission_ids = []  # List to store submission IDs
blocked_subreddits = []  # List to store blocked subreddits

for subreddit in subreddits:
    try:
        count += 1
        submission = reddit.subreddit(subreddit).submit(title=title, selftext=selftext, flair_id=None, flair_text= None, send_replies=False)
        submission_ids.append(submission.id)  # Add submission ID to the list
        print("The submission id is:", submission.id)
        print("Posted to", subreddit, "- Post", count, "of", len(subreddits))
    except praw.exceptions.RedditAPIException as exception:
        for subexception in exception.items:
            if subexception.error_type == "SUBREDDIT_NOTALLOWED":
                print("Blocked subreddit:", subreddit)
                blocked_subreddits.append(subreddit)
                break
            elif subexception.error_type == "RATELIMIT":
                wait = re.search(r"\d+", subexception.message).group()  # Extract the waiting time from the error message
                wait = int(wait) * 60
                print("Waiting for", wait, "seconds due to rate limit")
                time.sleep(wait)  # Pause the script for the required duration
                break
        else:
            submission = reddit.subreddit(subreddit).submit(title=title, selftext=selftext, flair_id=None, flair_text=None, send_replies=False)
            submission_ids.append(submission.id)  # Add submission ID to the list
            print("The submission id is:", submission.id)
            print("Posted to", subreddit, "- Post", count, "of", len(subreddits))

print("Blocked subreddits:", blocked_subreddits)
print("All submission IDs:", submission_ids)
