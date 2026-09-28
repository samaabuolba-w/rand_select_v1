from rand_select_v1.data import name_list, questions
from rand_select_v1.selector import random_selection



def main():
    while True:
        resp = input("Press 'Y' to continue, any other key to exit:")
        if resp.upper() != 'Y':  # .upper makes resp case-insensitive
            break
        else:
            chosen_name, chosen_question = random_selection(name_list, questions)
            print(f"{chosen_name}, please answer: {chosen_question}\n")
            