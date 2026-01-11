class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'{self.username}')
        for licz,i in enumerate(self.posts, start=1):
            print(f'{licz}. {i}')

def main():
    profile = SocialMediaProfile("johndoe")

    profile.add_post("Hello, world")
    profile.add_post("Had a great day at the park!")
    profile.add_post("What's up, Natalie? How are you?")

    profile.display_timeline()


if __name__ == "__main__":
    main()