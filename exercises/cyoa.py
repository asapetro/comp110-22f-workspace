"""Buzzfeed pie quiz."""


points: int = 0
player: str = ""
from random import randint


def greet() -> None:
    """Greets player."""
    global player
    print("Hello, these short quizes will determine which pie or ice cream you would be if you were a pie or ice cream.")
    player = input("Enter your name: ")
    print(f"You may begin, {player}!")

def pie_qs() -> None:
    """Returns the user's score."""
    global points
    seasons_q: str = input("True or False: Fall is the best season? ")
    if seasons_q is "True":
        points += 200
    food_q: str = input("Waffles or Pancakes? ")
    if food_q == "Waffles":
        points += 3
    activity_q: str = input("What's your main activity for the Day? Apple picking(1), A misty hike(2), Buying cranberries(3), or Drinking coffee at the pecan orchard(4). Enter the number corresponding with your choice:")
    if activity_q == "1":
        points += 10
    if activity_q == "2":
        points += 20
    if activity_q == "3":
        points += 30
    if activity_q == "4":
        points += 40


def pie_type(point: int) -> str:
    """Returns user's pie-type."""
    if point > 200:
        return "Congratulations, You are a Pumpkin-pie!!!"
    elif point < 20: 
        return "Congratulations, You are an Apple-pie!!!"
    elif point < 30:
        return "Congratulations, You are a Chicken pot-pie!!!"
    elif point < 40:
        return "Sorry, You are a Cranberry-pie."
    elif point < 50:
        return "Sorry, You are a Pecan-pie."

def cream_qs(ice_points: int) -> int:
    """Returns user's score for ice cream evalutaion."""
    global player
    fav_mat: str = input("Do you prefer a leather couch to a cotton one? Respond with \"Yes\" or \"No\": ")
    if fav_mat == "Yes":
        ice_points += 10
    fav_clothe: str = input("What percentage of winter days do you wear a hoodie(no zipper) as opposed to a jacket? A) <25% B) 25-50% C) >50%. Enter corresponding letter: ")
    if fav_clothe == "A":
        ice_points += 10
    if fav_clothe  == "B":
        ice_points += 30
    if fav_clothe == "C":
        ice_points += 60
    slush_points: int = int(input("On a scale from 1 - 10, how much do you like gas station slushies? "))
    if slush_points > 5:
        ice_points += 60
    return ice_points

def cream_type(points: int) -> str:
    """Returns correct ice cream type."""
    global player
    if points > 100:
        return f"Sorry, {player}, unfortunately you are Strawberry ice-cream."
    else:
        if randint(1, 2) == 2:
            return f"Congrats!!! {player}, you are Vanilla ice-cream!!"
        else:
            return f"Congrats!!! {player}, you are Chocolate ice-cream!!"


def main() -> None:
    global points
    greet()
    exp_route: str = input("Enter \"1\" if you would like to find your pie-type, \"2\" for your ice-cream type, or \"3\" to end your experience: ")
    if exp_route == "1":
        pie_qs()
        print(pie_type(points))
    if exp_route == "2":
        print(cream_type(cream_qs(points)))
    if exp_route == "3":
        print(f"Goodbye {player}, your accumulated a total of {points} quiz points throughout your experience.")
        
        


if __name__ == "__main__":
    main()
