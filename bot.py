# Twitter Bot Test 1
# Star Trek Episode Generator
# Lucy Kull

import tweepy
import random
import os
from secrets import *
from time import gmtime, strftime


bot_username = 'SpamsLot'
logfile_name = bot_username + ".log"


# list of characters for bot to draw from
character = ["Captain Kirk", "Commander Spock", "James T Kirk", "Spock", "Bones", "Leonard McCoy", "Doctor McCoy",
              "Montgomery Scott", "Scotty", "Lt. Commander Scott", "Hikaru Sulu", "Sulu", "Lt. Sulu", "Chekov",
              "Lt. Chekov", "Pavel Chekov", "Uhura", "Lt. Uhura", "Nyota Uhura", "Nurse Chapel", "Christine Chapel",
              "the USS Enterprise", "the Enterprise"]

# list of series for the bot to draw from
series = ["Star Trek", "Star Trek: The Original Series"]


# list of plot-building events to make the tweet amusing
plot = ["contracted a disease that makes them speak exclusively in limericks", "technobabel",
        "find the meaning of life", "initiates first contact with a strange planet",
        "get their can opener stolen by gremlin", "get ransomed for one cheese cracker",
        "enlist a small militia of raccoons", "is only able to eat spaghetti for rest of their life",
        "must peel every grape they encounter", "gets strange looks from birds",
        "is only able to open water bottles upside down", "gets strange urge to follow the butterflies",
        "finds a door to a strange dimension but only once"]

# list of solutions to the strange plot
solution = ["bargain for a pair of ceremonial underpants", "kill it", "get drunk", "dance it off", "licks it",
            "swear off cheese", "make a grass crown", "fight a tree"]

random.seed()  # we're doing some randomization
series_choice = random.randint(0, len(series) - 1)   # variable to choose which series to tweet
character_choice = random.randint(0, len(character) - 1)  # variable to choose which character to tweet
plot_choice = random.randint(0, len(plot) - 1)  # variable to choose which plot to tweet
solution_choice = random.randint(0, len(solution) - 1)  # variable to choose which solution to tweet



def create_tweet():
    """Create the text of the tweet you want to send."""

    # TWEET STRUCTURE
    # in this episode of <series> <character>
    # <plot> and <have to> <solution>


    text = "In this episode of " + series[series_choice] + " " + character[character_choice] + " " + plot[plot_choice] + " and has to " + solution[solution_choice]
    return text


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
