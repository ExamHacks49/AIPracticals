import random

# Create a list of tuples, where each turple contains the Face card and its suits.
face_cards = [(i, s) for i in ["Ace", "King", "Queen", "Jack"] for s in [" spades", "hearts", "diamonds", "clubs"]]
# Create a list of tuples, where each tuple contains the card number and its suits.
normal_cards = [(i, s) for i in range(2, 10) for s in [" spades", "hearts", "diamonds", "clubs"]]
# merge the above 2 list to make a deck of cards
deck = face_cards + normal_cards
# Shuffle the deck.
random.shuffle(deck)

# Print the first 5 tuples of the list.
print(deck[:5])