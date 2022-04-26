import praw

reddit = praw.Reddit(
    client_id = '',
    client_secret = '',
    user_agent = '',
    username = '',
    password = ''
)

# Sets environment for multiple functions / subs
DEV = ''


# Purdue Global // Purdue Sub
def Purdue():
    if DEV == 'Purdue':
        subreddit = reddit.subreddit('Purdue')

        print('Checking r/' + str(subreddit) + ' for keywords.') #Verifying subreddit

        bot_phrase = "Do you have a moment to talk about Purdue Global?"

        keywords = ['online classes', 'enroll online']


        for submission in subreddit.hot(limit=1):
            n_title = submission.title.lower()
            for i in keywords:
                if i in n_title:
                    print('Bot replying to: ')
                    print('Title: ', submission.title)
                    print('Message: ', submission.selftext)
                    print('Score: ', submission.score)
                    print('-----------------------------')
                    print('Bot replying: ', bot_phrase)
                    print()
                    submission.reply(bot_phrase)
                else:
                    print()
                    print('No posts found with those keywords.')
    else: 
    print('\n\n*****************************************')
    print("Check environment before running the bot!")
    print('*****************************************')
