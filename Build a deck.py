class Card:
    def __init__(self, kind, trump):
        self.kind =kind
        self.trump =trump
    def same(self,b):
        if self.kind==b.kind:
            return (True)
        else:
            return (False)
    def compare(self,b):
        if self.same(b):
            if self.trump=="C":
                return(b)
            elif b.trump=="C":
                return(self)
            elif self.trump=="P":
                return (self)
            elif b.trump=="P":
                return (b)
            elif self.trump=="H":
                return (self)
            else:
                return (b)
        else:
            Comparison=["2","3","4","5","6","7","8","9","D","J","Q","K","A"]
            avalue=0
            for i in range(13):
                if Comparison[i]==self.kind:
                    avalue=i
            bvalue=0
            for i in range(13):
                if Comparison[i]==b.kind:
                    bvalue=i
            if avalue<bvalue:
                return (b)
            else:
                return (self)
    def Print(self):       
        print(self.kind+", "+self.trump)
        
class Deck(Card):
    def __init__(self,kind=None,trump=None,cards=[],size=0):
        Card.__init__(self,kind,trump)
        self.cards=cards
        self.size=size
    def Addcard(self,card):
        if self.size==52:
            return ("The deck is complete")
        for i in self.cards:
            if i.kind == card.kind and i.trump == card.trump:
                return ("the card was already added")
        self.cards.append(card)
        self.size=self.size+1
        return ("the card was added successfully")
    
    def createcard(self):
        a="14"
        types=["2","3","4","5","6","7","8","9","D","J","Q","K","A"]
        while a=="14":
            kind=input("write the kind of the card: ")
            for i in types:
                if kind==i:
                    a=i
            if a=="14":
                print("the kind is not valid")
                a="10"
        a="4"
        trumps=["C","D","H","P"]
        while a=="4":
            trump=input("write the trump of the card: ")
            for i in trumps:
                if trump==i:
                    a=i
            if a=="4":
                print("the trump is not valid")
        card=Card(kind,trump)
        print (self.Addcard(card))
        if self.Addcard(card)== "the kind is not valid" or self.Addcard(card)== "the trump is not valid":
            self.createcard()
    def CompareLast(self):
        a=self.cards
        i=len(a)
        z1=a[i-1]
        z2=a[i-2]
        return (z1.compare(z2))
    def PrintDeck(self):
        for i in self.cards:
            print(i.kind+","+i.trump)
        

    
