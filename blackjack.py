#Create Cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#putting ranks, Values, and suits as class "card" atributes 
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
        
##prints str of cards    
    def __str__(self):
        
        return self.rank + ' of ' + self.suit + ' # ' + str(self.values) 


import random
class Deck():
   #Adding cards to deck class
    def __init__(self):        
        self.deck = []
        for suit in suits:
            for rank in ranks:
                    self.deck.append(Card(suit,rank))
    #prints cards in deck                
    def __str__(self):
        d_comp = ''
        for card in self.deck:
            d_comp += '\n' + card.__str__()
        return 'the deck has:' + d_comp     
  
    #Shuffles the deck                
    def shuffle(self):
        
        random.shuffle(self.deck)
        
    def deal(self):
        delt_card = self.deck.pop()
        
        return delt_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    
    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank] 
        
    # track aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_ace(self):
        if self.value > 21 and self.aces > 0:
            self.value -10
            self.aces -1        
                

class Chips():
    def __init__(self,total = 100):
        self.total = total  # Can be changed later in program or by user input
        self.bet = 0 #starting of at = to zero
        
        
    def win_(self):
        self.total =+ self.bet
            
    def lose_(self):
        self.total -= self.bet
            

def take_bet(chips):

    while True:
        
        try:
            chips.bet =int(input('How many chips are you betting? :'))
        except:
            print('Enter a number!')
        else:
            if chips.bet > chips.total:
                print(f'Amount entered is more than total chips {chips.total}')
            
            else:
                break

#Function hit when called removes card from deck.
def hit(deck,hand):
    hand.add_cards(deck.deal())
    hand.adjust_ace()


def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input('Hit Or Stand?: Enter H or S ').upper()
        
        if x == 'H' :
            hit(deck,hand)
            
        elif x == 'S':
            print('Player has passed. Dealers turn')
            playing = False
        else:
            print('Wrong selection enter H or S')
            continue
        break
       

def show_some(player,dealer):
    print("\n Dealers Card")
    print('-Hidden Card-')
    print(dealer.cards[1])
    
    print(f"\n Players Card and value: {player.value}")
    for cards in player.cards:
        print(cards)
        
def show_all(player,dealer):
    print(f"\n Players Card and value: {player.value}")
    for cards in player.cards:
        print(cards)
        
    print(f"\n Dealers Card and value: {dealer.value}")
    for cards in dealer.cards:
        print(cards)
        

def player_busts(player,dealer,chips):
    print('Player Busted!!')
    chips.lose_()
    
def player_wins(player,dealer,chips):
    print('Player Won!!')
    chips.win_()
    
def dealer_busts(player,dealer,chips):
    print('Player Won! Dealer Busted!')
    chips.win_()
    
def dealer_wins(player,dealer,chips):
    print('Dealer Won!')
    chips.lose_()

def push(player,dealer,chips):
    print('Tied! its a Push!')

#Game starts
playing = True
while True:
    
    print('Black Jack')
    
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    
    
    #add cards to players
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
    
    #add card to dealer hand
    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
    
    #set up player chips
    player_chips = Chips()
    
    #take players bet
    take_bet(player_chips)
    
    #show player and one of dealers cards
    show_some(player_hand,dealer_hand)
    
    while playing:
        hit_or_stand(deck,player_hand)
        
        #showing players card and one of dealers
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break  
            
    if player_hand.value <= 21:
       
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        show_all(player_hand,dealer_hand)
            
            
            
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
                
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand,player_chips)
                
                
    print(f'player total chips: {player_chips.total}')
         
    new_game = input('Do u want to play again?: Y or N').upper()
    
    if new_game == 'Y':
        playing = True
        continue
        
    else:
        print('Game Over!')
        break    
