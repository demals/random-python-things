import random
def all_cards():
    all_cards_list = []
    for i in range(2,11):
        for j in range(4):
            all_cards_list.append(i)
    for i in range(4):
        all_cards_list.append("J")
        all_cards_list.append("Q")
        all_cards_list.append("K")
        all_cards_list.append("A")
    return all_cards_list

def full_hand_pop(deck,user,computer):
    for i in user:
        deck.remove(i)
    for i in computer:
        deck.remove(i)
    return deck

def dealers_hand(deck):
    hand = []
    hand.append(random.choice(deck))
    hand.append(random.choice(deck))
    return hand

def players_hand(hand,turn,deck):
    if turn == 1:
        hand.append(random.choice(deck))
        hand.append(random.choice(deck))
        return hand
    else:
        hand.append(random.choice(deck))
        return hand

def score(user):
    total = 0
    for card in user:
        if card == "A":
            if total > 21:
                total += 1
            else:
                total += 11
        else:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            else:
                total += card
    return total

def game():
    user = []
    turn = 0
    full_hand = all_cards()
    computer = dealers_hand(full_hand)
    while True:
        turn += 1
        user = players_hand(user,turn,full_hand)
        user_score = score(user)
        full_hand = all_cards()
        full_hand = full_hand_pop(full_hand, user, computer)
        if user_score == 21:
            print("black jack")
            break
        if user_score > 21:
            print("BUST!!!!")
            break
        print(str(computer[0]) + "_")
        print(*user)
        hit_stand = input("hit or stand?")
        if hit_stand == "hit":
            continue
        else:
            dealer_score = score(computer)
            if dealer_score > user_score:
                print("you lost")
                break
            else:
                print("you won!")
                break

game()
