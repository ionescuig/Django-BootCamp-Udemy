#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle


class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play.
    Methods: shuffle(), half().
    """
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    cards = []
    for color in  SUITE:
        for num in RANKS:
            cards.append((num, color))

    def __init__(self, cards = cards):
        self.cards = cards

    def shuffle(self):
        """ Shuffles the deck """
        shuffle(self.cards)

    def half(self):
        """ Prepare the cards for each player and returns as lists """
        player_one = []
        player_two = []
        for el in range(0, len(self.cards)-1, 2):
            player_one.append(self.cards[el])
            player_two.append(self.cards[el+1])
        return player_one, player_two


class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand.
    Methods: add_cards(),remove_cards().
    '''

    def __init__(self, cards):
        self.cards = cards

    def add_cards(self, new):
        """
        Add cards to the original hand.
        (extends the list with the 'new' list)
        """
        self.cards.extend(new)


    def remove_card(self):
        """
        Removes a card from hand and returns that card.
        (removes the first element from list)
        """
        card = self.cards[0]
        del(self.cards[0])
        return card


class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.hand = hand
        self.name = name


def check_cards(a, b):
    """
    Checks if first hand is bigger than second one
    Returns: True or False
    """
    big = ['J', 'Q', 'K', 'A']
    if a[0] in big:
        new_a = (str(big.index(a[0])+11), a[1])
    else:
        new_a = a
    if b[0] in big:
        new_b = (str(big.index(b[0])+11), b[1])
    else:
        new_b = b
    if int(new_a[0]) > int(new_b[0]):
        return 'bigger'
    elif (int(new_a[0]) < int(new_b[0])):
        return 'smaller'
    else:
        return 'equal'


def display_turn(turn, test):
    print()
    print('Player:\t\t{}\t{}'.format(player_one.name, player_two.name))
    for i in range(len(turn)-1):
        if i % 2 == 0:
            print('Card:\t\t{} {}\t{} {}'.format(turn[i][0],turn[i][1],turn[i+1][0],turn[i+1][1]))
        else:
            print('Card:\t\t@ @\t@ @')
    print('Cards left:\t{}\t{}'.format(len(player_one.hand.cards), len(player_two.hand.cards)))

    input('\t\t'+ test)


######################
#### GAME PLAY #######
######################
print("\n\tWelcome to War!")
# prepare the deck
deck = Deck()
deck.shuffle()

# prepare the cards for each player
user, pc = deck.half()
player_one_hand = Hand(user)
player_two_hand = Hand(pc)
user_name = input('\nPlease enter your name(7 letters max): ')
print("\n\n\tLet's begin...")

# prepare players for WAR
player_one = Player(user_name, player_one_hand)
player_two = Player('PC', player_two_hand)

# game logic
turn =[]

while len(player_one.hand.cards)>0 and len(player_two.hand.cards)>0:
    player_one_card = player_one.hand.remove_card()
    player_two_card = player_two.hand.remove_card()
    turn.extend([player_one_card, player_two_card])
    test = check_cards(player_one_card, player_two_card)
    display_turn(turn, test)
    if test == 'bigger':
        player_one.hand.add_cards(turn)
        turn = []
    elif test == 'smaller':
        player_two.hand.add_cards(turn)
        turn = []
    else:
        player_one_card = player_one.hand.remove_card()
        player_two_card = player_two.hand.remove_card()
        turn.extend([player_one_card, player_two_card])

# Game Over
if len(player_one.hand.cards) == 0:
    print('You lost')
    input('\npress any key to continue ...')
else:
    print('YOU WIN')
    input('\npress any key to continue ...')
