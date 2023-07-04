import praw

reddit = praw.Reddit(
    client_id="zZduCWLpVkrIFi1LME395A",
    client_secret="vAysRgcLKUgoLsv9D05NKAEw-zyBjA",
    password="EliteIntern@23",
    user_agent="stablecoin by /u/cyptoddict2947",
    username="cyptoddict2947",
)

total_views = 0
total_upvotes = 0
total_downvotes = 0
total_comments = 0

submission_ids = ['14o2ufd','14o2w1n','14o2w25','14o2w2j','14o2x1m','14o320t','14o321f','14o3224','14o3cjn','14o3ck2','14o3ckq','14o3dff','14o3e1l','14o3een','14o3fpn','14o3fq1','14o3fql','14o3hi6','14ol2xi', '14ol2xv', '14ol2y5', '14ol2yg', '14ol2yv', '14ol2zd', '14ol2zo', '14ol2zz', '14ol308', '14ol30v', '14ol31g', '14ol31r', '14ol32a', '14ol32q', '14ol335', '14ol33u', '14ol34b','14olkhc']

for submission_id in submission_ids:
    submission = reddit.submission(id=submission_id)
    submission.comments.replace_more(limit=None)  # Retrieve all comments (including nested comments)
    total_views += submission.upvote_ratio * submission.score
    total_upvotes += submission.score
    total_downvotes += submission.downs
    total_comments += len(submission.comments.list())
    
    print("Submission Title:", submission.title)
    print("Submission Upvotes:", submission.score)
    print("Submission Downvotes:", submission.downs)
    print("Submission Comments:", len(submission.comments.list()))
    print("--------------")
    for comment in submission.comments.list():
        print("Comment:", comment.body)
        print("Comment Upvotes:", comment.score)
        print("Comment Downvotes:", comment.downs)
        print("--------------")

print("Total Views:", total_views)
print("Total Upvotes:", total_upvotes)
print("Total Downvotes:", total_downvotes)
print("Total Comments:", total_comments)
