class User:

    def __init__(self, first_name: str, last_name: str, password: str):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.password = password
        self.followers = 0
        self.following = 0

    def print_user_details(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def add_follower(self, user):
        self.followers += 1
        print(
            f"Congrats!!! You have a new follower 🎉.\nFollowers are now {self.followers} {'follower' if self.followers == 1 else 'followers'}.")

    def user_following(self):
        self.following += 1
        print(
            f"Congrats!!! You have followed someone 🎉.\nYou are now following {self.following} {'person' if self.following == 1 else 'people'}.")


user_1 = User(first_name="tsvetan", last_name="markov", password="this is some password")
user_1.print_user_details()
user_1.add_follower(user_1)
user_1.user_following()
user_1.user_following()
