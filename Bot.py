import pprint
from time import sleep
#from time import time
from InstagramAPI import InstagramAPI

user = "Enter your account user name"
password = "Enter your account password"
users_list = []
following_users = []
follower_users = []

class InstaBot:
    def __init__(self):
        self.api = InstagramAPI(user, password)

    def get_likes_list(self,username):
        api = self.api
        api.login()
        api.searchUsername(username) #Gets most recent post from user
        result = api.LastJson
        username_id = result['user']['pk']
        user_posts = api.getUserFeed(username_id)
        result = api.LastJson
        media_id = result['items'][0]['id']

        api.getMediaLikers(media_id)
        users = api.LastJson['users']
        for user in users:
            users_list.append({'pk':user['pk'], 'username':user['username']})
        bot.follow_users(users_list)

    def follow_users(self,users_list):
        count = 0
        api = self.api
        api.login()
        api.getSelfUsersFollowing()
        result = api.LastJson
        for user in result['users']:
            following_users.append(user['pk'])
        for user in users_list[50:-50]:
            #print(f"count: {count}")
            if count != 0 and count % 50 == 0:
                print(f"\nSleeping for 2 minutes...count: {count}\n")
                #sleep(120)
                count +=1
                quit()
            if not user['pk'] in following_users:
                print('Following @' + user['username'])
                api.follow(user['pk'])
                # set this really long to avoid from suspension
                count += 1
                sleep(32)
            else:
                print('Already following @' + user['username'])
                sleep(16)
            print(f"count: {count}")

    def unfollow_users(self):
        count = 0
        api = self.api
        api.login()
        api.getSelfUserFollowers()
        result = api.LastJson
        for user in result['users']:
            follower_users.append({'pk':user['pk'], 'username':user['username']})

        api.getSelfUsersFollowing()
        result = api.LastJson
        for user in result['users']:
            following_users.append({'pk':user['pk'],'username':user['username']})

        for user in following_users:
            if count != 0 and count % 60 == 0:
                print(f"That is enough for now, count: {count}")
                #print(f'Time taken to execute: {time.strftime("%c")}')
                quit()
            if not user['pk'] in [user['pk'] for user in follower_users]:
                print('Unfollowing @' + user['username'])
                api.unfollow(user['pk'])
                # set this really long to avoid from suspension
                count +=1
                sleep(31)
            #else:
                #count += 1
            print(f"count = {count}")

bot =  InstaBot()
name = "instagram"
# change the name ('instagram') to your target username

# To follow users run the function below
bot.get_likes_list(name)

# uncomment to unfollow users
#bot.unfollow_users()
