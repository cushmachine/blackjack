# Blackjack
# See cards_writeup.txt for details on game construction

from cards import *

def setup_hand(deck):

    # Generate hands
    npc1_hand = Hand()
    player_hand = Hand()

    print "\nDealing..."

    # Deals NPC 1 and tallys hand
    npc1_hand.add_cards(deck.deal_cards(2))
    npc1_hand_score = npc1_hand.tally_hand()

    # Deals Player and tallys hand; displays hand and point value to player
    player_hand.add_cards(deck.deal_cards(2))
    player_hand_score = player_hand.tally_hand()
    print "\nYou were dealt:"
    player_hand.print_hand()
    print "\nYour point value is {}".format(player_hand_score)

    # After initial hand is dealt, lets players actually play hand
    play_hand(deck, npc1_hand, player_hand)

def play_hand(deck, hand1, hand2):

    # Locally defines hands
    npc1_hand = hand1
    player_hand = hand2

    # Sets initial player hand point values
    npc1_hand_score = npc1_hand.tally_hand()
    player_hand_score = player_hand.tally_hand()

    # Sets starting conditions that may help trigger end of hand if flipped
    hand_active = True
    npc1_stand = False
    player_stand = False

    while hand_active:

        # Player plays
        action = raw_input("\nWhat would you like to do?\
                            \n[A] Hit \
                            \n[B] Stand \n> ").upper()
        if action == 'A':
            player_hand.add_cards(deck.deal_cards(1))
            player_hand_score = player_hand.tally_hand()
        elif action == 'B':
            player_stand = True
        else:
            # For lack of a better thing to do, we default to mistype = stand
            print "Sorry, I couldn't hear you. Did you say 'stand'?"
            player_stand = True

        # NPC plays - simple ruleset hits on 16, stands on 17
        if npc1_hand_score < 17:
            npc1_hand.add_cards(deck.deal_cards(1))
            npc1_hand_score = npc1_hand.tally_hand()
        else:
            npc1_stand = True

        # Displays output of round
        print "\nYour hand is now:"
        player_hand.print_hand()
        print "\nGriph's hand is now:"
        npc1_hand.print_hand()
        print "\nYour point value is {}".format(player_hand_score)
        print "Griph's point value is %d" % (npc1_hand_score)

        # Assess winner of hand and display appropriate results

        # NPC and player both bust
        if player_hand_score > 21 and npc1_hand_score > 21:
            print "\nYou both went bust!"
            hand_active = False

        # NPC busts, player is ok
        elif player_hand_score <=21 and npc1_hand_score > 21:
            print "\nGriph when bust! You win this hand!"
            hand_active = False

        # NPC is ok, player busts
        elif player_hand_score > 21 and npc1_hand_score <= 21:
            print "\nYou went bust! Griph wins this one, kiddo."
            hand_active = False

        # NPC and Player both haven't bust yet...
        # ... and stand
        elif player_hand_score <= 21 and npc1_hand_score <= 21:
            if npc1_stand == True and player_stand == True:
                print "\nYou both stand. Griph has %d points. You have %d points." \
                % (npc1_hand_score, player_hand_score)
                if npc1_hand_score > player_hand_score:
                    print "Griph wins!"
                elif npc1_hand_score < player_hand_score:
                    print "You win!"
                elif npc1_hand_score == player_hand_score:
                    print "You and Griph tie!"
                hand_active = False
        # ... and want to keep playing
            else:
                print "You're both still in it."
                play_hand(deck, npc1_hand, player_hand)
                hand_active = False


def main():

    # Generates and shuffles game deck
    game_deck = Deck()
    game_deck.shuffle_deck()

    # # Generates discard pile
    # discard_pile = Deck()

    # # Sets player starting scores at default of zero
    # npc1_game_score = 0
    # player_game_score = 0

    # Displays welcome message and initial choice
    print "\nWecome to the blackjack table!"
    print "\nYou're sitting with 1 other player: Griph."

    game_active = True

    # Generates top-level player choice menu
    while game_active:

        action = raw_input("\nWhat would you like to do? \n \
                            \n[A] Play a hand \
                            \n[B] Check scores \
                            \n[C] Exit \n > ").upper()

        if action == 'A':
            setup_hand(game_deck)
        elif action == 'B':
            print "\nGriph's score is %d" % (npc1_game_score)
            print "Your score is %d" % (player_game_score)

        elif action == 'C':
            print "\nBye now!"
            game_active = False
        else:
            print("Bitch, please enter a valid command.")


main()