#Attributes:
#On instantiation of a user, the following attributes should be passed in as arguments:

#first_name
#last_name
#email
#age
#Also include default attributes:

#is_rewards_member - default value of False
#gold_card_points = 0
class user:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
#display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f"first_name:{self.first_name} \n")
        print(f"last_name:{self.last_name} \n")
        print(f"email:{self.email} \n")
        print(f"age:{self.age} \n")
        print(f"Members:{self.is_rewards_member} \n")
        print(f"card:{self.gold_card_points } \n")
        print("************************************************")
#enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        if self.is_rewards_member:
            print("User is already member.\n")
            return False


        self.is_rewards_member = True
        self.gold_card_points = 400
#spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print("You had a few points!!!")
            return #exit function!!!
        self.gold_card_points = self.gold_card_points - amount
my_user = user("Yaya", "DEMBELE", "ydembele@gmail.com", 30)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(400)
my_user.display_info()

