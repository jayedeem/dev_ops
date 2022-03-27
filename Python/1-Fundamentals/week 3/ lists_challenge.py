import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    options = input("Press enter to pick a card or Q then enter to quit: ")
    if options in ("q", "Q"):
        break
    random_card = random.choice(diamonds)
    hand.append(random_card)
    print("Your hand: ", hand)
    diamonds.remove(random_card)
    print("Remaining Cards: ", diamonds)
    if not diamonds:
        print("There are no more cards to pick")
        break
