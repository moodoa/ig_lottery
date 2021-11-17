import random
import instaloader

class IGlottery:
    def __init__(self, account, password, article_id):
        self.account = account
        self.password = password
        self.article_id = article_id
    
    def get_all_followers(self):     
        all_followers = []
        insta = instaloader.Instaloader()
        insta.login(self.account, self.password)
        post = instaloader.Post.from_shortcode(insta.context, self.article_id)
        post_comments = post.get_comments()
        for comment in post_comments:
            if comment.owner.username not in all_followers:
                all_followers.append(comment.owner.username)
        return all_followers
    
    def random_pick(self):
        number = input("how many people you wanna pick?")
        all_followers = self.get_all_followers()
        return random.sample(all_followers, int(number))
    
if __name__ == "__main__":
    print("welcome to the instagram lottery")
    account = input("please key your account : ")
    password = input("please key your password : ")
    article_id = input("please key your article id : ")
    lottery = IGlottery(account, password, article_id)
    print(lottery.random_pick())
    input("key ENTER to leave")