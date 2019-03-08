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


class cardStack(object):
    '''
    A cardStack is a collection of Cards. Special cases of a cardStack might
    include a "hand", a "deck", a "discard pile", and so on. We think of all of
    these things as having similar properties, such as the ability to shuffle,
    add cards, deal cards, merge, etc..
    '''

    def __init__(self):
        self.stack = []

    def generate_standard_deck(self):

        RANKS = ('2', '3', '4', '5', '6', '7','8','9','10','Jack','Queen','King','Ace')
        SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

        for suit in SUITS:
            for rank in RANKS:
                self.stack.append(Card(rank,suit))

    def shuffle_stack(self):
        '''
        Shuffles the deck.
        '''
        random.shuffle(self.stack)

    def count_stack(self):
        '''
        Returns the number of cards in the stack.
        '''
        return len(self.stack)

    def print_stack(self):
        '''
        Prints out a sequential list of all cards in the deck. Note that
        we consider the last card on the list to be the "top."
        '''
        for i in range(0,len(self.stack)):
            self.stack[i].print_card()

    def deal_cards(self,target_stack,count):
        '''
        Pops a given number of cards off the top of the deck and returns them
        as a list. Note that we consider the last card on the list to be the "top."
        '''

        i = 0

        if len(self.stack)>=count:
            while i < count:
                target_stack.add_cards_top((self.stack.pop()))
                i += 1
        else:
            print "Your deck doesn't have enough cards, yo."

    def add_cards_top(self,cards):
        '''
        Taking CARDS as input, adds card(s) to the top of the deck. Note that we
        consider the last card on the list to be the "top."
        '''

        # Should probably add some guardrails to prevent object of the wrong
        # type from being added
        self.stack.append(cards)

    def tally_stack(self):
        '''
        Sum the points value of all cards in a stack (using blackjack values)
        '''

        tally = 0

        for i in range(0,len(self.stack)):
            tally += self.stack[i].card_value()

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



''''
# TODO #

- Turn Griph into a dealer who wins ties.

- Make it so cards played go into the discard pile, which gets shuffled and re-
added to the deck when the deck runs low.

- Fix handling of Ace scoring

- Allow game to be played with 1 to 5 NPC players

- Use decorators (?) to create a special "Dealer" player who wins ties.

- Implement error handling when user types in an incorrect option when playing
a hand (i.e. doesn't just default to 'stand')

- Implement blackjack casino rules (cut cards,doubling down, etc.)

- [MAYBE] Implement betting system

# DONE #
- Merged concepts of "hand" and "deck" for simplicity
-- Make it so that the cardStack method "deal" takes another cardStack as an
input. You shouldn't be able to just deal cards into oblivion / as currently
implemented, it's not clear what you are supposed to do with dealt cards.



# RESOURCES #
https://www.youtube.com/watch?v=ZDa-Z5JzLYM

'''
