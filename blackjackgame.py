import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


#this class is for creating deck and suffling cards and getting card and calculating card value
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(suit+" of "+rank)     #list bngyi sbhi combination di
    def shuffle(self):
        random.shuffle(self.cards)          #cards shuffle krte
    
    def deal(self):    
        
        self.temp=random.choice(self.cards)       #choice from cards list
        self.cards.remove(self.temp)                #remove element from list
        self.temp2=self.temp.split()
        
        self.temp3=values[self.temp2[2]]       #got numerical value of the card
        
        return self.temp
        
    def calc(self):
        return self.temp3

#..........end of this class................
        
    
def bit(balance,amount):
    if(balance>=amount):
        return True
    else: return False

def win(bal1,bal2):
    if(bal1>bal2):
        return True
    else: return False

def lose(bal):
    if(bal>21):
        return False
    else: True




max_bal=100
while(True):
    print("Welcome to BlackJack Game")
    print(f'Your Balance is {max_bal}')
    print("Enter your Bit: ")
    
    while True:
        biit=int(input())
        if(bit(max_bal,biit)==False):
            print('Enter a valid Bit')
        else:
            max_bal=max_bal-biit
            break
    game_start=input("Enter YES if your ready else NO: ")
    
    if(game_start.lower()[0]=='y'):
        start=True
    else: start=False    
    
    
    while start:
        deck=Deck()
        deck.shuffle()
        
        player=[]
        player.append(deck.deal())
        add=0
        temp=deck.calc()
        add=temp
        player.append(deck.deal())
        add=add+deck.calc()
        
        for i in range(1):
            if(deck.calc==11):
                add=add+input('What value you want to take 1 or 11: ')-deck.calc()
            if(temp==11):
                add=add+input('What value you want to take 1 or 11: ')-temp
        
        dealer=[]
        deal_add=0
        dealer.append(deck.deal())
        deal_add=deck.calc()
        temp2=False
        if(deck.calc()==11):
            temp2=True
        
        print('Cards of Playter1: ',player)
        print('Cards of Dealer: ',dealer)
        turn=input('For Hit type YES for Stand NO: ')
        if(turn.lower()[0]=='y'):
            while True:
                player.append(deck.deal())
                add=add+deck.calc()
                print(player)
                turn2=input('For Hit type YES for Stand NO: ')
                if(turn2.lower()[0]!='y'):
                    break
        if(lose(add)==False):
            print("YOU BLOODY LOSER")
            break
        while deal_add<17:
            dealer.append(deck.deal())
            deal_add=deal_add+deck.calc()
            if(deal_add > 21):
                if(temp2):
                    deal_add = deal_add-10
                if(deck.calc==11):
                    deal_add = deal_add-10
                    
        print('Cards of Playter1: ',player)
        print('Cards of Dealer: ',dealer)
        if(lose(deal_add)==False):
            print("YOU WIN UNFORTUNATELY :)")
            if(add==210):
                max_bal=max_bal+2.5*biit
            else:
                max_bal=max_bal+2*biit
            break
        if(deal_add==add):
            print("Game Draw")
        elif(win(deal_add,add)):
            print("YOU BLOODY LOSER")
            break
        else:
            print("YOU WIN UNFORTUNATELY :)")
            if(add==210):
                max_bal=max_bal+2.5*biit
            else:
                max_bal=max_bal+2*biit
            break
    rest=input("PLay Again type YES else NO: ")
    if(rest.lower()[0]!='y'):
        break
        