names = ["Bella", "Nelly", "Andrew", "Poppy", "Jimmy", "Drake", "Mr. Foster", "Kelly", "Fiola", "Fionna"]
results = ["Happy", "Angry", "Sad", "Tired"]
i = 0
import random
class Dog():
    def __init__(self, name):
        self.name = name
        print(f"Your dog's name is {name}")
    def Walk(self, walk_mins):
        self.mins = walk_mins
        print(f"You took {Yourdog.name} for a walk for {walk_mins} minutes.")
    def Give_food(self, food):
        self.food = food
        print(f"You gave {YourDog.name} {food}.")
    def Play(self, play_mins, result):
        self.play_mins = play_mins
        self.result = result
        print(f"You played with {YourDog.name} for {play_mins} minutes. Your dog is now {result}")

YourDog = Dog(random.choice(names))
while i == 0:
    choice = input("Do you want to walk, give food or play with your dog(choose with the words walk, give and play): ")
    if choice.lower() == "walk":
        YourDog.Walk(random.randint(10,60))
    elif choice.lower() == "give":
        food_sel = input("What do you want to give to you pet: ")
        YourDog.Give_food(food_sel.lower())
    elif choice.lower() == "play":
        YourDog.Play(random.randint(5,60), random.choice(results))
    else:
        print("You can't do that yet!")


