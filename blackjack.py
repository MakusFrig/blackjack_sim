import time
import random

class player:

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


def main_game():
    global players, deck, wins_for_stop_16, wins_for_stop_17, draws, test
    
    for i in players:
        deal(deck, i, 2)
    
    #this is where the test comes in 
    while players[0].total() < 17:
        deal(deck, players[0], 1)
        
    while players[1].total() < 16:
        deal(deck, players[1], 1)
    if players[0].verdict() == 1 and players[1].verdict() == 1:
        draws+=1
    elif players[0].verdict() == 1 and players[1].verdict() != 1:
        wins_for_stop_16+=1
    elif players[0].verdict() != 1 and players[1].verdict() == 1:
        wins_for_stop_17 += 1
    else:
        if players[0].total() == players[1].total():
            draws += 1
        elif players[0].total() > players[1].total():
            wins_for_stop_17+=1
        elif players[1].total() > players[0].total():
            wins_for_stop_16+=1
    test +=1
    if test < 100000:
        pass
        
    else:
        print(f'stop 16 won {wins_for_stop_16} times')
        print(f'stop 17 won {wins_for_stop_17} times')
        print(f'they drew {draws} times')
        
    
wins_for_stop_16, wins_for_stop_17, draws,test = 0,0,0,0

def main():
    setup()
    main_game()
    
    
if __name__ == "__main__":
    for i in range(100000):
        main()