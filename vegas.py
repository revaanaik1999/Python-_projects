"""
CSCI-603: Lab 6
Author: Disha Revandkar (dr6742@rit.edu)
Author: Revaa Naik      (rn7416@rit.edu)

This program solves the card game

"""
from cs_queue import Queue
from cs_stack import Stack
import random


def deck(total_cards):
    """
     This function takes total number of cards as parameter and creates a deck of cards accordingly
     :return: shuffled_deck
     """
    original_deck = Queue()
    shuffled_deck = Queue()
    for i in range(1, total_cards + 1):
        original_deck.enqueue(i)
    for i in range(total_cards):
        temp, original_deck = shuffle_deck(original_deck, total_cards)
        shuffled_deck.enqueue(temp)
    return shuffled_deck


def shuffle_deck(shuffle_cards, total_cards):
    """
    This function shuffles the cards.
    :return: temp
    :return: shuffle_cards
    """
    times = random.randint(1, total_cards)
    for i in range(times):
        shuffle_cards.enqueue(shuffle_cards.peek())
        shuffle_cards.dequeue()
    temp = shuffle_cards.peek()
    shuffle_cards.dequeue()
    return temp, shuffle_cards


def strategy1(shuffled_deck, n):
    """

    :return: flag
    """
    i = 0
    victory_pile = Stack()
    # ascending
    discard_pile1 = Stack()
    # dumpster
    discard_pile2 = Stack()

    flag = 0
    while i < n:
        card = shuffled_deck.peek()
        shuffled_deck.dequeue()
        if card == (flag + 1):
            victory_pile.push(card)
            flag += 1
        if discard_pile1.is_empty() and card > flag:
            discard_pile1.push(card)
        else:
            while not discard_pile1.is_empty() and discard_pile1.peek() == flag + 1:
                victory_pile.push(discard_pile1.peek())
                flag += 1
                discard_pile1.pop()
            if not discard_pile1.is_empty() and discard_pile1.peek() > card > flag:
                discard_pile1.push(card)
            elif card > flag:
                discard_pile2.push(card)
        if not discard_pile2.is_empty():
            while not discard_pile2.is_empty() and discard_pile2.peek() == flag + 1:
                victory_pile.push(discard_pile2.peek())
                flag += 1
                discard_pile2.pop()
        i += 1
    return flag


def strategy2(shuffled_deck, n):
    """
    This function divides the total number of cards into two parts.
    It the puts the cards in the two discard piles on the basis of the partition made.
    Then it checks for the first element of each pile and if it satisfies the given condition
    adds it to the victory pile and increases the count and then checks for the next card in the
    discard pile. This iteration continues until it matches the number requested by the user.
    :return: numb
    """
    c = 0
    victory_pile = Stack()
    discard_pile1 = Stack()
    discard_pile2 = Stack()

    cards_no = n // 2
    numb = 0
    for i in range(cards_no):
        card = shuffled_deck.peek()
        shuffled_deck.dequeue()
        discard_pile1.push(card)
    numb += 1

    for i in range(cards_no + 1, n + 1):
        card = shuffled_deck.peek()
        shuffled_deck.dequeue()
        discard_pile2.push(card)
    numb += 1

    card1 = discard_pile1.peek()
    card2 = discard_pile2.peek()

    while c < n:
        if card1 == (numb + 1):
            victory_pile.push(card1)
            numb += 1
            discard_pile1.pop()
        if card2 == (numb + 1):
            victory_pile.push(card2)
            numb += 1
            discard_pile2.pop()

        if discard_pile1.peek() == numb + 1:
            victory_pile.push(discard_pile1.peek())
            numb += 1
            discard_pile1.pop()

        else:
            if discard_pile2.peek() == numb + 1:
                victory_pile.push(discard_pile2.peek())
                numb += 1
                discard_pile2.pop()
        if discard_pile1.is_empty() or discard_pile2.is_empty():
            return numb
        c += 1
    return numb


def main():
    """
    This is the main function
    """
    while True:
        n = input("Enter number of cards to use: ")
        try:
            n = int(n)
            break
        except ValueError:
            print("Value must be an int. You entered"+str(n))

    m = int(input("Enter number of games to simulate: "))
    minimum = n
    maximum = 0
    total = 0
    for i in range(m):
        shuffled_deck = deck(n)
        count = strategy1(shuffled_deck, n)
        maximum = max(count, maximum)
        minimum = min(count, minimum)
        total += count

    print("Simulating games applying strategy 1...")
    print("Average victory size pile: ", total / m)
    print("Minimum victory pile size: ", minimum)
    print("Maximum victory pile size: ", maximum)

    for i in range(m):
        shuffled_deck = deck(n)
        count2 = strategy2(shuffled_deck, n)
        maximum = max(count2, maximum)
        minimum = min(count2, minimum)
        total += count2
    print("Simulating games applying strategy 2...")
    print("Average victory size pile: ", total / m)
    print("Minimum victory pile size: ", minimum)
    print("Maximum victory pile size: ", maximum)


if __name__ == '__main__':
    main()
