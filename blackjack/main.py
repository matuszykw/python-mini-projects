from logo import logo
import random
import os

def deal_card():
    '''return a random card from a deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score(cards):
    '''return score calculating from the cards '''
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0
    if 11 in cards and score > 21:
        cards.append(1)
        cards.remove(1)
        score = sum(cards)
    return score

def who_win(user_score, computer_score):
    if user_score == computer_score or (computer_score > 21 and user_score > 21):
        return "It's a draw"
    elif user_score == 0:
        return "You have a Blackjack. You win!"
    elif computer_score == 0:
        return "Computer has a Blackjack. You win!"
    elif user_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return"Computer went over 21. You win."
    elif user_score > computer_score:
        return"You win!"
    elif computer_score > user_score:
        return"You lose."

def blackjack():
    os.system('cls')
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while True:
        user_score = score(user_cards)
        computer_score = score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            break
        else:
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card {computer_cards[0]}")
            still_playing = input("Type 'y' to get another card, type 'n' to pass: ")
            if still_playing == 'y':
                user_cards.append(deal_card())
                user_score = score(user_cards)
            else:
                break
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = score(computer_cards)
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(who_win(user_score, computer_score))
    wanna_play = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if wanna_play == 'y':
        blackjack()
    else:
        exit()

wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if wanna_play == 'y':
    blackjack()
else:
    exit()