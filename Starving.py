from libdw import sm
import random



class Hero():
    def __init__(self,name,HP=0,satiety=0,gend=None):
        self.name=name
        self.HP=HP
        self.satiety=satiety
        self.gend=gend
        self.saved=False
    def gender(self,gender):
        if gender=="M":
            self.HP=4
            self.satiety=1
            self.gend="Male"
        elif gender=="F":
            self.HP=3
            self.satiety=2
            self.gend="Female"
    def __str__(self):
        str1="Hero:   {0}".format(self.name)
        str2="Gender: {0}".format(self.gend)
        str3="HP:     {0}".format(self.HP)
        str4="satiety:{0}".format(self.satiety)
        return str1+"\n"+str2+"\n"+str3+"\n"+str4
    def Event(self):
        destiny=random.random()
        if destiny>=0 and destiny<0.1:
            print("Congratulations! You were found by the passing boat and get saved!")
            self.saved=True
            if self.HP==0:
                print("But unfortunately, you were so starving that you died before getting on the boat!")
        elif destiny>=0.1 and destiny<0.4:
            print("You had been busy for a whole day but had found nothing and got hungry.")
            if self.satiety>0:
                self.satiety-=1
        elif destiny>=0.4 and destiny<0.6:
            print("OOps! You were attacked by the beast and got injured!")
            self.HP-=1
        
        elif destiny>=0.6 and destiny<1.0:
            print("You found the precious food and had a full meal!")
            if self.gend=="Male":
                self.satiety=1
            else:
                self.satiety=2
        if self.satiety==0:
            print("STARVING! You need to find some food to live!")
            self.HP-=1










class Game(sm.SM):
    def __init__(self):
        self.start_state=['0',1,None]
        self.next_state=['0',1,None]

    def get_next_values(self,state,inp):
        if inp=="R" and state[0]=='0':
            print("Please print your hero's name here.")
            name=input("➢➢➢")
            YourHero=Hero(name)
            print("Please press M/F choose your hero's gender.")
            gender=input("➢➢➢")
            if gender!='M' and gender!='F':
                print('That is not a gender!Please choose M/F.')
                gender=input("➢➢➢")
            YourHero.gender(gender)
            print(("Oops!A new hero {0} got lost in a strange island".format(YourHero.name)))
            print(YourHero)
            output=("It's day{0} now, press S to explore this island.".format(str(state[1])))
            days=state[1]+1
            self.next_state=['1',days,YourHero]
            return self.next_state,output
        elif inp=="S" and state[0]!='0':
            state[2].Event()
            print(state[2])
            if state[2].saved:
                self.next_state=['4',state[1]-1,state[2]]
                output=''
            elif state[2].HP>0:
                output=("It's day{0} now, press S to explore this island.".format(str(state[1])))
                days=state[1]+1
                self.next_state=['1',days,state[2]]
            else:
                if state[2].HP<0:
                    state[2].HP=0
                output=("SADLY! You had died!")
                self.next_state=['3',state[1]-1,state[2]]
            return self.next_state,output
        elif inp=="P" and state[0]=='0':
            self.next_state=['2',state[1]-1,state[2]]
            output="You have quited this game, see you!"
            return self.next_state,output
        else:
            output=("That's invalid text, please try again.")
            return state,output
    def quit(self):
        if self.state[0]=="2":
            return True
        else:
            return False
    def dead(self):
        if self.state[0]=="3":
            return True
        else:
            return False
    def saved(self):
        if self.state[0]=="4":
            return True
        else:
            return False
    def run(self):
        self.start()
        print("Welcome to the mysterious island! How long can you live?")
        print("Press R to start, press P to quit.")
        while(True):
            if self.quit():
                break
            elif self.dead() or self.saved():
                print("You have lived for {0}days in this island".format(str(self.next_state[1])))
                break
            else:
                i=input("➢➢➢")
                print(self.step(i))
 
MyGame=Game()
MyGame.run()
           
        
