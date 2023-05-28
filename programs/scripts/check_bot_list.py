# returns username
import requests
import sys

ALLOWLIST = ["CommanderRoot", "StreamElements", "Nightbot"]

bots_online_response = requests.get("https://api.twitchinsights.net/v1/bots/online")
bot_list = bots_online_response.json()['bots']

# list of viewers online
# print(users_online_list)

# list of bots names
bot_names_list = []
for bot in bot_list:
    bot_names_list.append(bot[0])
# print(bot_names_list)

# remove allowlist names from list
for good_bot in map(str.lower, ALLOWLIST):
    bot_names_list.remove(good_bot.lower())
# print(bot_names_list)

# for each user on list in bot_names_list, check if user is online bot list
if sys.argv[1].lower() in map(str.lower, bot_names_list):
    # check if user is in viewer bot list, if yes, return user
    print(1)
else:
    # do nothing
    print(0)