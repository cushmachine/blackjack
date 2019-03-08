# Cards module
# See cards_writeup.txt for details on game construction

import random

class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def return_card(self):
        '''
        Returns a card of a given rank and suit
        '''
        card = (self.rank, self.suit)
        return card

    def card_value(self):
        value_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9, \
                      '10':10,'Jack':10,'Queen':10,'King':10 ,'Ace':11}

        card_value = value_dict[self.rank]
        return card_value

    def print_card(self):
        '''
        Prints the rank and suit of the card
        '''
        print("The %s of %s") % (self.rank, self.suit)


class Deck(Card):

    def __init__(self):
        self.deck = []

        RANKS = ('2', '3', '4', '5', '6', '7','8','9','10','Jack','Queen','King','Ace')
        SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank,suit))

    def print_deck(self):
        '''
        Prints out a sequential list of all cards in the deck. Note that
        we consider the last card on the list to be the "top."
        '''
        for i in range(0,len(self.deck)):
            self.deck[i].print_card()

        print "There are %d cards in the deck." % len(self.deck)

    def shuffle_deck(self):
        '''
        Shuffles the deck.
        '''
        random.shuffle(self.deck)

    def deal_cards(self,count):
        '''
        Pops a given number of cards off the top of the deck and returns them
        as a list. Note that we consider the last card on the list to be the "top."
        '''

        i = 0
        dealt_cards = []

        if len(self.deck)>count:
            while i < count:
                dealt_cards.append(self.deck.pop())
                i += 1

            return dealt_cards

        else:
            print "Your deck doesn't have enough cards, yo."

    def add_cards_top(self,cards):
        '''
        Adds card(s) to the top of the deck. Note that we consider the last
        card on the list to be the "top."
        '''

        # Should probably add some guardrails to prevent object of the wrong
        # type from being added
        self.deck.extend(cards)


class Hand(Deck):

    def __init__(self):
        self.hand = []

    def add_cards(self,cards):
        '''
        Takes a list of Cards and adds a list of other Cards
        '''
        self.hand.extend(cards)

    def print_hand(self):
        '''
        Prints out the contents of the current hand.
        '''
        for i in range(0,len(self.hand)):
            self.hand[i].print_card()

    def tally_hand(self):
        '''
        Sum the points value of all cards in a hand (using blackjack values)
        '''

        tally = 0

        for i in range(0,len(self.hand)):
            tally += self.hand[i].card_value()

        return tally

class Player(object):

    def __init__(self, name="DefaultName", wins=0, rounds=0):
        self.name = name
        self.wins = wins
        self.rounds = rounds

    def add_round(self):
        '''
        Tallies that the player has engaged in a round of the game
        '''
        self.rounds +=1

    def add_win(self):
        '''
        Tallies that the player has won a round of the game
        '''
        self.wins += 1

    def print_score(self):
        '''
        Prints out player's win rate
        '''
        print "%s has won %d out of %d rounds" % (self.name, self.wins, self.rounds)


p1 = Player("Griph")

p1.print_score()



''''
# TODO #
- Create Player class with name and score
- Make it so cards played go into the discard pile, which gets shuffled and re-
added to the deck when the deck runs low.


- Make it so the game can be played with an arbitrary number of AI players
- Implement error handling when user types in an incorrect option when playing
a hand (i.e. doesn't just default to 'stand')


# RESOURCES #
https://www.youtube.com/watch?v=ZDa-Z5JzLYM

'''
