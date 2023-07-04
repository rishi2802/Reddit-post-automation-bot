import praw
#this file is to subscribe to different subreddits 
# Subreddits to follow
subreddits = ['CryptoMarkets','CryptoTrading','Altcoin','CryptoTechnology','CryptoCurrencyTrading','StockMarket','business','Entrepreneur','SmallBusiness','Startups','Marketing','Finance','Accounting','Economics','Consulting','bookporn','bookhaul','goodreads','scifi','bookclub','suggestmeabook','literature','FreeEBOOKS','sciencefiction','historybooks']

# Create a Reddit instance

reddit = praw.Reddit(
    client_id="zZduCWLpVkrIFi1LME395A",
    client_secret="vAysRgcLKUgoLsv9D05NKAEw-zyBjA",
    password="EliteIntern@23",
    user_agent="stablecoin by /u/cyptoddict2947",
    username="cyptoddict2947",
)
# Follow subreddits
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    subreddit.subscribe()

    print("Subscribed to:", subreddit.display_name)
