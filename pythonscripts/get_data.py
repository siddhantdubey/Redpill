import praw
import pandas as pd

reddit = praw.Reddit("bot1", user_agent="bot1 user agent")

sub = ['ApplyingToCollege']  # make a list of subreddits you want to scrape the data from

for s in sub:
    subreddit = reddit.subreddit(s)   # Chosing the subreddit


########################################
#   CREATING DICTIONARY TO STORE THE DATA WHICH WILL BE CONVERTED TO A DATAFRAME
########################################

#   NOTE: ALL THE POST DATA AND COMMENT DATA WILL BE SAVED IN TWO DIFFERENT
#   DATASETS AND LATER CAN BE MAPPED USING IDS OF POSTS/COMMENTS AS WE WILL 
#   BE CAPTURING ALL IDS THAT COME IN OUR WAY

# SCRAPING CAN BE DONE VIA VARIOUS STRATEGIES {HOT,TOP,etc} we will go with keyword strategy i.e using search a keyword
    query = ['Harvard']

    
    post_dict = {
        "title" : [],
        "score" : [],
        "id" : [],
        "url" : [],
        "comms_num": [],
        "created" : [],
        "body" : []
    }
    comments_dict = {
        "comment_id" : [],
        "comment_parent_id" : [],
        "comment_body" : [],
        "comment_link_id" : []
    }
    for submission in subreddit.hot(limit=100):
        post_dict["title"].append(submission.title)
        post_dict["score"].append(submission.score)
        post_dict["id"].append(submission.id)
        post_dict["url"].append(submission.url)
        post_dict["comms_num"].append(submission.num_comments)
        post_dict["created"].append(submission.created)
        post_dict["body"].append(submission.selftext)
        
        ##### Acessing comments on the post
        submission.comments.replace_more(limit=100)
        for comment in submission.comments.list():
            comments_dict["comment_id"].append(comment.id)
            comments_dict["comment_parent_id"].append(comment.parent_id)
            comments_dict["comment_body"].append(comment.body)
            comments_dict["comment_link_id"].append(comment.link_id)
    
    post_comments = pd.DataFrame(comments_dict)

    post_comments.to_csv(s+"hot_comments_" +"subreddit.csv")
    post_data = pd.DataFrame(post_dict)
    post_data.to_csv(s+"hot_" +"subreddit.csv")