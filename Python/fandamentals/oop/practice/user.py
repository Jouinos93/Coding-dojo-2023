class User:
    def init (self,first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points=0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        self.is_rewards_member=False
        self.gold_card_points=200

    def spend_points(self, amount):
        self.gold_card_points -= amount

user1=User("Souha","karoui","karoui.souha18@gmail.com",20)
user1.display_info()
user1.enroll()
user2=User("Mariem","joueni","jouinimariem05@gmail.com",30)
user3=User("Mariem","cherif","cherif.13@gmail.com",19) 
user1.spend_points(50)
user2.enroll()
user2.spend_points(80)
user1.display_info()
user2.display_info()
user3.display_info()
user1.enroll()
user3.spend_points(40)



