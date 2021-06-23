import time
import random

class player:
    '''
    The verdict and total functions are for determineing hand values and such
    the display hand fucntion server no purpose other than debugging, once the 
    script is complete then it will be removed
    '''

    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def total(self):
        temp = 0
        for i in self.hand:
            temp+=int(i[1:])
        return temp
    
    
    def display_hand(self): #this function
        for i in self.hand:
            print(i, end = " ")
        print("\n")
        
    def verdict(self):
        if self.total() == 21:
            return 0
            
        elif self.total() > 21:
            return 1
        elif self.total() < 21:
            return 2

def deal(d, p, n):
    for i in range(n):
        card = random.choice(d)
        p.hand.append(card)
        d.remove(card)
    
def shuffle(d): #this is a simple shuffle function which returns a shuffled deck
    temp = []
    for i in range(len(d)):
        picked = random.choice(d)
        temp.append(picked)
        d.remove(picked)
    return temp


def setup():
    global deck, players
    deck = []
    suits = "shdc" #these are all the suits in a deck
    for i in range(4):
        for e in range(1, 13):
            deck.append(suits[i]+str(e))
    deck = shuffle(deck)
    CPU1 = player("cpu1")
    CPU2 = player("cpu2")
    players = [CPU1, CPU2]


def main_game(trial):
    global players, deck, wins_for_stop_16, wins_for_stop_17, draws, test
    
    for i in players:
        deal(deck, i, 2)
    
    # the next two while statements are to draw cards for each players up until its limit
    while players[0].total() < 17:
        deal(deck, players[0], 1)
        
    while players[1].total() < trial:
        deal(deck, players[1], 1)
    '''
    The following is to make sure that the game is throwing out any hand over 21 as loses
    before making this change there was some unbelievable reults when testing 18 against 17
    because the 18 would yield higher results on average and would not filter out those hands 
    which went bust
    '''
        
    if players[0].verdict() == 1 and players[1].verdict() == 1:
        draws+=1
    elif players[0].verdict() == 1 and players[1].verdict() != 1:
        trial_number+=1
    elif players[0].verdict() != 1 and players[1].verdict() == 1:
        regular_number += 1
    else:
        '''
        this determines who won the hand, so long as no hands went bust
        '''
        if players[0].total() == players[1].total():
            draws += 1
        elif players[0].total() > players[1].total():
            regular_number+=1
        elif players[1].total() > players[0].total():
            trial_number+=1
    '''
    if test < 100000:
        pass
        
    else:
        print(f'stop {trial} won {trial_number} times')
        print(f'stop 17 won {regular_number} times')
        print(f'they drew {draws} times')
        
        
    this did not need to be inside the main function which will be called over 100000 times
    two useless if else statements did not make sense
    '''
        
    
regular_number,trial_number, draws,test = 0,0,0,0 # this is just initializing some variables to be used throughout the entire test

def main():
    setup()
    main_game(16) #this passes 16 as the alternative number
    
    
if __name__ == "__main__":
    for i in range(100000):
        main()
    print(f'stop {trial} won {trial_number} times')
    print(f'stop 17 won {regular_number} times')
    print(f'they drew {draws} times')
