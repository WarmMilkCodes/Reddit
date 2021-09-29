import praw

reddit = praw.Reddit(

)


subreddit = reddit.subreddit('Purdue')

print('Checking r/' + str(subreddit) + ' for keywords.') #Verifying subreddit

bot_phrase = "Do you have a moment to talk about Purdue Global?"

keywords = ['online classes', 'enroll online']


for submission in subreddit.hot(limit=15):
    n_title = submission.title.lower()
    for i in keywords:
        if i in n_title:
            print('Bot replying to: ')
            print('Title: ', submission.title)
            print('Message: ', submission.selftext)
            print('Score: ', submissions.score)
            print('-----------------------------')
            print('Bot replying: ', bot_phrase)
            print()
            submission.reply(bot_phrase)
        else:
            print()
            print('No posts found with those keywords.')

