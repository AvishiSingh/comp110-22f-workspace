"""My progress on EX06 assignment!"""

from random import randint


player: str = ""
points: int = 0 
points_green: int = 0 
user_guess: str = ""
pizza: str = "\U0001F355"
sad_face: str = "\U0001F622"
angry_face: str = "\U0001F621"
happy_face: str = "\U0001F9D0"
scared_face: str = "\U0001F615"
party: str = "\U0001F973"
phone: str = "\U0001F4F1"
kitty: str = "\U0001F36A"
heart: str = "\U00002764"


def greet() -> None: 
    """This will greet the player and store their name as a variable."""
    player = input("Hi! Welcome to the quiz what is your name?")
    print(f"Hello, {player}!")


def entry() -> None:
    """This function will enter the main sequence of the game!"""
    global points
    user_guess: str = input("Do you wish to continue to look at your red or green flags?\nType \"no\" to exit. Otherwise type \"red\" for the red flags quiz or \"green\" for the green flags quiz!")
    while user_guess != "no" and user_guess != "red" and user_guess != "green":
        user_guess = input("We are not sure what you mean! Please try again!")
    if user_guess == "no":
        print(f"You accumulated 0 red flags/greenflags. Aw {sad_face} we hops to see you again soon!")
    elif user_guess == "red":
        red()
    elif user_guess == "green":
        user_a: int = int(input("How many green flags do you think you have? INPUT A NUMBER!"))
        points = green_flags(user_a)


def red() -> None: 
    """This is a quiz that will determine your total number of red flags based on a series of questions!"""
    global points
    answer_1: str = input(f"Do you, {player} like pinapple on pizza? {pizza}(Please type in the capital letter of the answer you choose) \n A. Sometimes but it is not my favorite\n B. NEVER EW\n C.YES OMG my favvvv\n D.I literally dont care this is a stupid question")
    while answer_1 != "A" and answer_1 != "B" and answer_1 != "C" and answer_1 != "D": 
        answer_1 = input("We are not sure what you mean, please try again")
    if answer_1 == "B": 
        points = points + 1 
    answer_2: str = input(f"What is your reaction to getting a bad grade {player}? (Please type in the capital letter of the answer you choose) \n A. Sit an cry for a little while{sad_face} \n B. Throw your phone at the wall{angry_face}\n C.Idk I have never gotten a bad grade\n D.Go to the professor to see what you can improve on\n")
    while answer_2 != "A" and answer_2 != "B" and answer_2 != "C" and answer_2 != "D": 
        answer_2 = input("We are not sure what you mean, please try again")
    if answer_2 == "C": 
        points = points + 1 
    if answer_2 == "B": 
        points = points + 1 
    answer_3: str = input(f"How often do you drink water? Be honest {player}! (Please type in the capital letter of the answer you choose) \n A. Way too much I am borderline dying from hypertension \n B. NEVER EW\n C.A balanced healthy amount\n D.Occasionally")
    while answer_3 != "A" and answer_3 != "B" and answer_3 != "C" and answer_3 != "D": 
        answer_3 = input("We are not sure what you mean, please try again")
    if answer_3 == "B": 
        points = points + 1
    if answer_3 == "A": 
        points = points + 3
    answer_4: str = input(f"How often do you procrastinate. Be honest {player}, we can tell when you are lying{happy_face}\nA. More often than I should\nB. Its so bad its not even funny\n C. My crippling anxiety keeps me from procrastinating\n D. I submit all of my assignmnets a week before they are due")
    while answer_4 != "A" and answer_4 != "B" and answer_4 != "C" and answer_4 != "D": 
        answer_4 = input("I am not sure what you mean, please try again")
    if answer_4 == "D": 
        points = points + 1 

    if points >= 3:
        print(f"I am a computer and I am still scared of you. {player}, you have {points} red flags{scared_face} Please come back and try again after you work on yourself a little{heart}")
    elif points > 0:
        print(f"My expert assesment tells me you only have {points} red flags and are not a threat to the UNC community! Have a great day {player}{happy_face}")
    elif points < 0: 
        print(f"You dont have any red flags {happy_face}")


def green_flags(a: int) -> int: 
    """This function will take the green flags you think you have and adjust them based on yoru answers to a couple questions."""
    starting_green_flags: int = 10
    randomizer: int = randint(0, 10)
    questionare_points: int = 0 
    answer_1: str = input(f"What is your song of choice before a night out?{party}\nA.Mr. Brightside\nB.Money by Cardi B\nC.Teletubbies theme song\nD.No music\n")
    while answer_1 != "A" and answer_1 != "B" and answer_1 != "C" and answer_1 != "D": 
        answer_1 = input("I am not sure what you mean, please try again!")
    if answer_1 == "D": 
        questionare_points = questionare_points - 3
    if answer_1 == "C": 
        questionare_points = questionare_points - 1
    answer_2: str = input(f"How often have you broken your phone?{phone}\nA.Never\nB.Once\nC.Twice\nD.Three or more times\n")
    while answer_2 != "A" and answer_2 != "B" and answer_2 != "C" and answer_2 != "D": 
        answer_2 = input("I am not sure what you mean, please try again!")
    if answer_2 == "A": 
        questionare_points = questionare_points - 2
    if answer_2 == "D": 
        questionare_points = questionare_points - 1
    answer_3: str = input(f"Are you a cat person?{kitty}\nA. Ew no\nB. I am indifferent\nC.I {heart} cats and they love me\nD.I {heart} cats and they hate me")
    while answer_3 != "A" and answer_3 != "B" and answer_3 != "C" and answer_3 != "D": 
        answer_3 = input("I am not sure what you mean, please try again!")
    if answer_3 == "D": 
        questionare_points = questionare_points - 2
    if answer_3 == "B": 
        questionare_points = questionare_points - 1 
    return starting_green_flags - randomizer - questionare_points


def main() -> None:
    """This function will enter the main body of the game!""" 
    entry()
    if points < 0:
        print(f"You have {points} green flag(s) through this assesment!")
    if points > 0:
        print(f"You have {points} red flag(s) based on this assement")
    end_choice: str = input("Do you wish to go again? Please type \"no\" or \"yes\"!")
    while end_choice == "yes":
        entry()
        end_choice = input("Do you wish to go again? Please type \"no\" or \"yes\"!")
    if end_choice == "no": 
        print(f"Thanks for playing {player}")
    while end_choice != "yes" and end_choice != "no": 
        end_choice = input("I am not sure what you mean please try again!")


if __name__ == "__main__":
    main()
