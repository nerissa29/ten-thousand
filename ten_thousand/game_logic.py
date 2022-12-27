from collections import Counter
from random import randint
class GameLogic:
    @staticmethod
    def roll_dice(dice):
        values = []
        for i in range(dice):
            value = randint(1, 6)
            values.append(value)

        return tuple(values)

    # @staticmethod
    # def user_prompt():
    #     print("Welcome to Ten Thousand!")
    #     while True:
    #         count = 0
    #         user_response = input("y(es) to play or n(o) to decline")
    #         if user_response.lower() == "y" or "yes":
    #             count += 1
    #             print(f"Starting round {count}")
    #             dice_roll = roll_dice()
    #             return dice_roll
    #
    #         elif user_response.lower() == "n" or "no":
    #             print("Thank you! Goodbye!")
    #             return
    #
    #         else:
    #             print("Please enter y(es) or n(o)!")
    #
    #         dice_keep_quit = input("Enter dice to keep or (q)uit")
    #         if dice_keep_quit.lower() == "q" or "quit":
    #             return
    #         else:
    #             values_to_keep = []


    @staticmethod
    def calculate_score(tuple_int):
        int_dict = Counter(tuple_int)

        score = 0
        for i in int_dict:
            if i == "1":
                """
                ((1,), 100),
                ((1, 1), 200),
                ((1, 1, 1), 1000),
                ((1, 1, 1, 1), 2000),
                ((1, 1, 1, 1, 1), 3000),
                ((1, 1, 1, 1, 1, 1), 4000),
                """
                if int_dict[i] == 1: score += 100
                if int_dict[i] == 2: score += 200
                if int_dict[i] == 3: score += 1000
                if int_dict[i] == 4: score += 2000
                if int_dict[i] == 5: score += 3000
                if int_dict[i] == 6: score += 4000
            if i == "2":
                """
                ((2,), 0),
                ((2, 2), 0),
                ((2, 2, 2), 200),
                ((2, 2, 2, 2), 400),
                ((2, 2, 2, 2, 2), 600),
                ((2, 2, 2, 2, 2, 2), 800),
                """
                if int_dict[i] == 1: score += 0
                if int_dict[i] == 2: score += 0
                if int_dict[i] == 3: score += 200
                if int_dict[i] == 4: score += 400
                if int_dict[i] == 5: score += 600
                if int_dict[i] == 6: score += 800
            if i == "3":
                """
                ((3,), 0),
                ((3, 3), 0),
                ((3, 3, 3), 300),
                ((3, 3, 3, 3), 600),
                ((3, 3, 3, 3, 3), 900),
                ((3, 3, 3, 3, 3, 3), 1200),
                """
                if int_dict[i] == 1: score += 0
                if int_dict[i] == 2: score += 0
                if int_dict[i] == 3: score += 300
                if int_dict[i] == 4: score += 600
                if int_dict[i] == 5: score += 900
                if int_dict[i] == 6: score += 1200
            if i == "4":
                """
                ((4,), 0),
                ((4, 4), 0),
                ((4, 4, 4), 400),
                ((4, 4, 4, 4), 800),
                ((4, 4, 4, 4, 4), 1200),
                ((4, 4, 4, 4, 4, 4), 1600),
                """
                if int_dict[i] == 1: score += 0
                if int_dict[i] == 2: score += 0
                if int_dict[i] == 3: score += 400
                if int_dict[i] == 4: score += 800
                if int_dict[i] == 5: score += 1200
                if int_dict[i] == 6: score += 1600
            if i == "5":
                """
                ((5,), 50),
                ((5, 5), 100),
                ((5, 5, 5), 500),
                ((5, 5, 5, 5), 1000),
                ((5, 5, 5, 5, 5), 1500),
                ((5, 5, 5, 5, 5, 5), 2000),
                """
                if int_dict[i] == 1: score += 50
                if int_dict[i] == 2: score += 100
                if int_dict[i] == 3: score += 500
                if int_dict[i] == 4: score += 1000
                if int_dict[i] == 5: score += 1500
                if int_dict[i] == 6: score += 2000
            if i == "6":
                """
                ((6,), 0),
                ((6, 6), 0),
                ((6, 6, 6), 600),
                ((6, 6, 6, 6), 1200),
                ((6, 6, 6, 6, 6), 1800),
                ((6, 6, 6, 6, 6, 6), 2400),
                ((1, 2, 3, 4, 5, 6), 1500),
                ((2, 2, 3, 3, 4, 6), 0),
                ((2, 2, 3, 3, 6, 6), 1500),
                ((1, 1, 1, 2, 2, 2), 1200),
                """
                if int_dict[i] == 1: score += 0
                if int_dict[i] == 2: score += 0
                if int_dict[i] == 3: score += 600
                if int_dict[i] == 4: score += 1200
                if int_dict[i] == 5: score += 1800
                if int_dict[i] == 6: score += 2400

        return score





