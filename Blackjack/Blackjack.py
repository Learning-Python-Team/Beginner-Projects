#General plan:
    # Give player two cards
    # Have 4 of each card, so if player or dealer gets one, they have less chance of getting same
    # Have "hit/stick" ability 
    # GIVE USER CHOICE OF HAVING ACE BE 1 OR 11!
    
# todo MAKE THIS CODE NEATER BY USING FUNCTIONS! (Maybe make a new branch for this)
# todo Allow dealer to draw fourth card.
# todo If player is dealt a card, that card should be removed from deck. So less chance of getting it next time!
# todo Ability to play again
# todo (ADVANCED FEATURE) Add ability to bet
# todo (ADVANCED FEATURE) Add suits

import numpy as np
    
deck = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,
        8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J',
        'Q','Q','Q','Q','K','K','K','K']

card1_index = np.random.randint(52)
card2_index = np.random.randint(52)  

#print('The randomly generated index for card 1 is {}'.format(card1_index))
#print('The randomly generated index for card 2 is {}'.format(card2_index))

card1 = deck[card1_index]
card2 = deck[card2_index]

print('First card is a {}'.format(card1))
print('Second card is a {}'.format(card2))

##ASSIGNING CARD 1 VALUE
#If the card is 2-10
if card1 in range(2,11):
    card1_value = card1
#If card is Ace, assign value to 11
# todo Give player choice of using Ace as 1 or 11
if card1 == 'A':
    card1_value = 11
#If card is J/Q/K
if card1 in ['J','Q','K']:
    card1_value = 10

##ASSIGNING CARD 2 VALUE 
#If the card is 2-10
if card2 in range(2,11):
    card2_value = card2
#If card is Ace, assign value to 11
if card2 == 'A':
    card2_value = 11
#If card is J/Q/K
if card2 in ['J','Q','K']:
    card2_value = 10

##VALUE OF YOUR HAND 
hand_value = card1_value + card2_value
print('The value of your hand is {}'.format(hand_value))

##DEALER HAND
dealer1_index = np.random.randint(52)
dealer2_index = np.random.randint(52)

dealer1 = deck[dealer1_index]
dealer2 = deck[dealer2_index]

##ASSIGNING DEALER CARD 1 VALUE
#If the card is 2-10
if dealer1 in range(2,11):
    dealer1_value = dealer1
#If card is Ace, assign value to 11
# todo Give player choice of using Ace as 1 or 11
if dealer1 == 'A':
    dealer1_value = 11
#If card is J/Q/K
if dealer1 in ['J','Q','K']:
    dealer1_value = 10

##ASSIGNING DEALER CARD 2 VALUE
#If the card is 2-10
if dealer2 in range(2,11):
    dealer2_value = card2
#If card is Ace, assign value to 11
if dealer2 == 'A':
    dealer2_value = 11
#If card is J/Q/K
if dealer2 in ['J','Q','K']:
    dealer2_value = 10

##VALUE OF DEALER HAND
dealer_hand_value = dealer1_value + dealer2_value
print('Dealer hand value (just here for debugging) is {}'.format(dealer_hand_value))

#Dealer drawing a third card
if dealer_hand_value <15:
    print('dealer is drawing a third card (just here for debugging)')
    dealer3_index = np.random.randint(52)
    dealer3 = deck[dealer3_index]

    ##ASSIGNING DEALER 3 VALUE
    # If the card is 2-10
    if dealer3 in range(2, 11):
        dealer3_value = dealer3
    # If card is Ace, assign value to 11
    # todo Give player choice of using Ace as 1 or 11
    if dealer3 == 'A':
        dealer3_value = 11
    # If card is J/Q/K
    if dealer3 in ['J', 'Q', 'K']:
        dealer3_value = 10

    ##NEW VALUE OF DEALER HAND
    dealer_hand_value += dealer3_value
    print('New dealer hand value is {}'.format(dealer_hand_value))

    if dealer_hand_value >21:
        print('Dealer is bust!')
        print('You win!')
        quit() #this makes the program end as soon as dealer loses

#HIT OR STICK 
print('Hit, or stick?')
user_input = input()

if user_input in ['hit','Hit','HIT']:
    print('Ok partner, third card coming up')
    card3_index = np.random.randint(52) 
    card3 = deck[card3_index]
    print('Third card is a {}'.format(card3))
    
    ##ASSIGNING CARD 3 VALUE 
    if card3 in range(2,11):
        card3_value = card3
    if card3 == 'A':
        card3_value = 11 # todo again, here add a printout like ('you got an ace! Do you want it as 1 or 11?')
    if card3 in ['J','Q','K']:
        card3_value = 10
        
    hand_value += card3_value
    print('The value of your hand is now {}'.format(hand_value))
    if hand_value >21:
        print('Bust! Too bad.')

    if hand_value <= 21:
        print('Hit, or stick?')
        user_input = input()

        if user_input in ['hit', 'Hit', 'HIT']:
            print('Ok partner, fourth card coming up')
            card4_index = np.random.randint(52)
            card4 = deck[card4_index]
            print('Fourth card is a {}'.format(card4))

            ##ASSIGNING CARD 4 VALUE # todo There is probably a much neater and more concise way of doing this with a loop, rather than copying and pasting my code over and over
            if card4 in range(2, 11):
                card4_value = card4
            if card4 == 'A':
                card4_value = 11  # todo again, here add a printout like ('you got an ace! Do you want it as 1 or 11?')
            if card4 in ['J', 'Q', 'K']:
                card4_value = 10

            hand_value += card4_value
            print('The value of your hand is now {}'.format(hand_value))
            if hand_value > 21:
                print('Bust! Too bad.')
    elif user_input in ['Stick', 'stick', 'STICK']:
        print('Stick, got it')
        print('The value of your hand is {}'.format(hand_value))
        print('The value of the dealer\'s hand is {}'.format(dealer_hand_value))
        if hand_value > dealer_hand_value:
            print('You win!')
        else:
            print('Dealer wins!')

elif user_input in ['Stick','stick','STICK']:
    print('Stick, got it')
    print('The value of your hand is {}'.format(hand_value))
    print('The value of the dealer\'s hand is {}'.format(dealer_hand_value))
    if hand_value > dealer_hand_value:
        print('You win!')
    else:
        print('Dealer wins!')

