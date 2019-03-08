# Blackjack
# See cards_writeup.txt for details on game construction

from cards import *

def setup_hand(deck, discard_pile, dealer, player):

    # Generate hands
    dealer_hand = cardStack()
    player_hand = cardStack()

    # Adds a round to each player's round count
    dealer.add_round()
    player.add_round()

    print "\nDealing..."

    # Deals hands
    deck.deal_stack(dealer_hand,2)
    deck.deal_stack(player_hand,2)

    # Deals Player and tallys hand; displays hand and point value to player
    print "\nYou were dealt:"
    player_hand.print_stack()
    print "\nYour point value is {}".format(player_hand.tally_stack())

    # After initial hand is dealt, lets players actually play hand
    play_hand(deck, discard_pile, dealer_hand, player_hand, dealer, player)

    dealer_hand.deal_stack(discard_pile, dealer_hand.count_stack())
    player_hand.deal_stack(discard_pile, player_hand.count_stack())
    print "Printing discard pile..."
    discard_pile.print_stack()
    #print player_hand.count_stack()



def play_hand(deck, discard_pile, hand1, hand2, dealer, player):

    # Locally defines hands
    dealer_hand = hand1
    player_hand = hand2

    # Sets initial player hand point values
    dealer_hand_score = dealer_hand.tally_stack()
    player_hand_score = player_hand.tally_stack()

    # Sets starting conditions that may help trigger end of hand if flipped
    hand_active = True
    dealer_stand = False
    player_stand = False

    while hand_active:

        # Player plays
        action = raw_input("\nWhat would you like to do?\
                            \n[A] Hit \
                            \n[B] Stand \n> ").upper()
        if action == 'A':
            deck.deal_stack(player_hand,1)
            player_hand_score = player_hand.tally_stack()
        elif action == 'B':
            player_stand = True
        else:
            # For lack of a better thing to do, we default to mistype = stand
            print "Sorry, I couldn't hear you. Did you say 'stand'?"
            player_stand = True

        # NPC plays - simple ruleset hits on 16, stands on 17
        if dealer_hand_score < 17:
            deck.deal_stack(dealer_hand,1)
            dealer_hand_score = dealer_hand.tally_stack()
        else:
            dealer_stand = True

        # Displays output of round
        print "\nYour hand is now:"
        player_hand.print_stack()
        print "\nGriph's hand is now:"
        dealer_hand.print_stack()
        print "\nYour point value is {}".format(player_hand_score)
        print "Griph's point value is %d" % (dealer_hand_score)

        # Assess winner of hand and display appropriate results

        # NPC and player both bust
        if player_hand_score > 21 and dealer_hand_score > 21:
            print "\nYou both went bust!"
            hand_active = False

        # NPC busts, player is ok
        elif player_hand_score <=21 and dealer_hand_score > 21:
            print "\nGriph when bust! You win this hand!"
            player.add_win()
            hand_active = False

        # NPC is ok, player busts
        elif player_hand_score > 21 and dealer_hand_score <= 21:
            print "\nYou went bust! Griph wins this one, kiddo."
            dealer.add_win()
            hand_active = False

        # NPC and Player both haven't bust yet...
        # ... and stand
        elif player_hand_score <= 21 and dealer_hand_score <= 21:
            if dealer_stand == True and player_stand == True:
                print "\nYou both stand. Griph has %d points. You have %d points." \
                % (dealer_hand_score, player_hand_score)
                if dealer_hand_score > player_hand_score:
                    print "Dealer wins!"
                    dealer.add_win()
                elif dealer_hand_score < player_hand_score:
                    print "You win!"
                    player.add_win()
                elif dealer_hand_score == player_hand_score:
                    print "You and Griph have the same score! Tie goes to the dealer."
                    dealer.add_win()
                hand_active = False
        # ... and want to keep playing
            else:
                print "You're both still in it."
                play_hand(deck, discard_pile, hand1, hand2, dealer, player)
                hand_active = False

def main():

    # Generates and shuffles game deck
    game_deck = cardStack()
    game_deck.generate_standard_deck()
    game_deck.shuffle_stack()

    # Generates discard pile
    discard_pile = cardStack()

    # Generates players
    dealer = Player("Griph")
    player = Player("Ace")

    # Displays welcome message and initial choice
    print "\nWecome to the blackjack table!"
    print "\nMy name is Griph. I'll be your dealer."

    game_active = True
    round_counter = 1


    # Generates top-level player choice menu
    while game_active:

        # Per casino rules, with 1 player, cards are shuffled every 5 rounds.
        round_counter +=1

        if round_counter >= 5:
            print "\nReshuffling deck..." % (round_counter)
            discard_pile.deal_stack(game_deck,discard_pile.count_stack())
            game_deck.shuffle_stack()
            round_counter = 1

        action = raw_input("\nWhat would you like to do? \n \
                            \n[A] Play a hand \
                            \n[B] Check scores \
                            \n[C] Exit \n > ").upper()

        if action == 'A':
            setup_hand(game_deck, discard_pile, dealer, player)
        elif action == 'B':
            dealer.print_score()
            player.print_score()

        elif action == 'C':
            print "\nBye now!"
            game_active = False
        else:
            print("Bitch, please enter a valid command.")


main()


'''
Casino shuffling rules:
- Every 5 rounds with 1 person
- Every 4 rounds with 2 ppl
- Every 3 rounds with 3 ppl
- Every 2 rounds with 4+ ppl


'''
