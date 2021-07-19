import praw

reddit = praw.Reddit("bot1", user_agent="bot1 user agent")

print(reddit.user.me())

subreddit = reddit.subreddit("ApplyingToCollege")

print(subreddit.description)

for submission in subreddit.top(limit=100):
    print(submission.title)

    print(submission.score)

    print(submission.selftext)

    print()