import random

class Card:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def show(self):
        print('{} of {}'.format(self.value,self.name))

class Deck:
    def __init__(self):
        self.card_deck = []
        self.generate()

    def generate(self):
        species = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        value = range(1,14)
        for s in species:
            for v in value:
                card = Card(s,v)
                self.card_deck.append(card)
        return self.card_deck
        
    def show_deck(self):
        for c in self.card_deck:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.card_deck)-1,0,-1):
            r = random.randint(0,i)
            self.card_deck[i] , self.card_deck[r] =self.card_deck[r] ,self.card_deck[i] 

    def drawCard(self):
        return self.card_deck.pop()
           
class Player:
    def __init__(self,name):
        self.name = name
        self.hand= []

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for c in self.hand:
            print("{} of {}".format(c.name,c.value))



deck = Deck()
deck.shuffle()
Kristian = Player('Kristian')
Kristian.draw(deck).draw(deck).draw(deck)
Kristian.showHand()

