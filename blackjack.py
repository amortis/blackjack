import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_score(list):
    summ = sum(list)
    if summ == 21:
        return 0
    elif summ > 21 and 11 in list:
        list.remove(11)
        list.append(1)
        return sum(list)
    else:
        return sum(list)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return 'Draw'
    elif computer_score==0:
        return 'Lose, opponent has a Blackjack'
    elif user_score == 0:
        return 'Win, you got a Blackjack'
    elif user_score>21:
        return 'Lose, you went over 21'
    elif computer_score>21:
        return "Win! Opponent went over 21"
    elif user_score > computer_score:
        return "You win, you got more than computer"
    else:
        return "You lose, you got less than computer"
def blackjack():
    print(logo)
    user_cards= []
    computer_cards = []
    gameover = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not gameover:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or comp_score ==21 or user_score>21:
            gameover = True
        else:
            user_choise = input("Type 'y' to get another card, 'n' to pass: ")
            if user_choise=='y':
                user_cards.append(deal_card())
            else:
                gameover = True
    while comp_score != 0 and comp_score <17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)
    print('')
    print(f"Your final hand: {user_cards}, your total score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's total score: {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play a game? Type 'y' for yes, 'n' fo no. ")=='y':
    blackjack()


