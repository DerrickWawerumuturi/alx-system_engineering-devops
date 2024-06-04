import praw

client_id = 'TpI4h2fDHqPBITulD7ztMg'
secret = 'Micd7Q5Rpi72KCUJPZGmRt9imWWkbg'
agent='utd_trey by /u/dw_mt'

r = praw.Reddit(
    client_id=client_id,
    client_secret=secret,
    user_agent=agent
    )

page = r.subreddit('programming')
top_post = page.hot(limit=None)
for post in top_post:
    print(post.title, post.ups)