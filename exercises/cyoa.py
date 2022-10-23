"""EX06 Buzzfeed pie quiz."""

__author__ = "730575054"

from random import randint

points: int = 0
player: str = ""

SMILE_FACE: str = "\U0001f600"
LAME_FACE: str = "\U0001F612"


def greet() -> None:
    """Greets player."""
    global player
    print("Hello, these short quizes will determine which pie or ice cream you would be if you were a pie or ice cream.")
    player = input("Enter your name: ")
    print(f"You may begin, {player}!")


def pie_qs() -> None:
    """Adds points from questions to global points."""
    global points
    seasons_q: str = input("True or False: Fall is the best season? ")
    if seasons_q == "True":
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
        return f"Congratulations, You are a Pumpkin-pie {SMILE_FACE}"
    elif point < 20: 
        return f"Congratulations, You are an Apple-pie {SMILE_FACE}"
    elif point < 30:
        return f"Congratulations, You are a Chicken pot-pie {SMILE_FACE}"
    elif point < 40:
        return f"Sorry, You are a Cranberry-pie {LAME_FACE}"
    elif point < 50:
        return f"Sorry, You are a Pecan-pie {LAME_FACE}"


def cream_qs(ice_points: int) -> int:
    """Returns user's score for ice cream evalutaion."""
    global player
    fav_mat: str = input(f"Do you, {player}, prefer a leather couch to a cotton one? Respond with \"Yes\" or \"No\": ")
    if fav_mat == "Yes":
        ice_points += 10
    fav_clothe: str = input("What percentage of winter days do you wear a hoodie(no zipper) as opposed to a jacket? A) <25% B) 25-50% C) >50%. Enter corresponding letter: ")
    if fav_clothe == "A":
        ice_points += 10
    if fav_clothe == "B":
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
        return f"Sorry, {player}, unfortunately you are Strawberry ice-cream {LAME_FACE}"
    else:
        if randint(1, 2) == 2:
            return f"Congrats!!! {player}, you are Vanilla ice-cream {SMILE_FACE}"
        else:
            return f"Congrats!!! {player}, you are Chocolate ice-cream {SMILE_FACE}"


def main() -> None:
    """Begins the program."""
    global points
    i = 0
    greet()
    exp_route: str = input("Enter \"1\" if you would like to find your pie-type, \"2\" for your ice-cream type, or \"3\" to end your experience: ")
    while i < 1:
        if exp_route == "1":
            points = 0
            pie_qs()
            print(pie_type(points))
            print(f"Total Quiz Points: {points}")
            exp_route = input("Press \"1\" to retake the pie quiz, \"2\" to take the ice-cream quiz, or \"3\" to end your experience: ")
        if exp_route == "2":
            points = 0
            points += cream_qs(points)
            print(cream_type(points))
            print(f"Total Quiz Points: {points}")
            exp_route = input("Press \"1\" to take the pie quiz, \"2\" to retake the ice-cream quiz, or \"3\" to end your experience: ")
        if exp_route == "3":
            print(f"Goodbye {player}, you accumulated a total of {points} quiz points throughout your experience.")
            i = 1
    print(f"Thank you for playing, {player}.")


if __name__ == "__main__":
    main()
