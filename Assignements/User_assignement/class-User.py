class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(f"First name : {self.first_name} \nLast name : {self.last_name}") 
        print(f"Email : {self.email}")        
        print(f"Age : {self.age}")        
        print(f"Is reward member : { 'No' if self.is_rewards_member == False else 'Yes' }")
        print(f"Gold card points : {self.gold_card_points}")
        
    def enroll(self):
        if (self.is_rewards_member == True):
            print("User already a member !")
            return False
        else :
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
        
    def spend_points(self, amount):
        if(self.gold_card_points >= amount):
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("The amount of points is not enough !")
        

user_1 = User("Sarra", "Ben Brahim", "email@gmail.com", 32)

user_1.enroll()    

user_1.display_info() 

user_2 = User("Nour", "Hajjaji", "email@gmail.com", 4)
user_3 = User("Oumayma", "Ben Brahim", "email@gmail.com", 26)

user_1.spend_points(50)


user_2.enroll()

user_2.spend_points(80)

user_1.display_info()

user_2.display_info()

user_1.enroll()  

user_3.enroll()  

user_3.display_info()

user_3.spend_points(250)






  