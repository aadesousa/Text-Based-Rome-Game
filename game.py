import time
import random
from pyfiglet import Figlet
class rome():
    def __init__(self):
        print("\n" * 100)
        f = Figlet(font='univers')
        print(f.renderText("Julius Caesar"))
        input("press Enter to start")
        caesar = Caesar()
    def ip(self, tx, one, two, three):
        f = Figlet(font='univers')
        print(f.renderText("Julius Caesar"))
        x = 0
        print("\n" * 100)
        print(" ", "_"* 70, " ")
        print("_"*75)
        print(tx)
        print("1:", one)
        print("2:", two)
        if three != " ":
            print("3:", three)
        x = int(input())
        return x
    

class Caesar():
    def __init__(self):
        self.CC = 0
        self.j = 0
        self.MarriedToCornelia = 0
        self.jbip = rome.ip("self", "The year is 85 BC. Your father has died and you are head of the family. Your uncle, Marius, is fighting a War with Lucius Cornelius Sulla. It is your choices that will shape the future of your familial legacy and The Roman Republic. Cinna, a close ally of your uncle, wamts you to marry his daughter, Cornelia to solidify the alliance.", "Marry her", "Marry a Peasant", "Marry no one")
        
        
        if self.jbip == 1:
            input("Your uncle is very proud of you. soon, she will grant you a child. \n \n Press enter to continue")
            self.MarriedToCornelia = 1
            self.two()
        
        
        if self.jbip == 2:
            print('Your Uncle, The Senate, as well as the Roman people see you as foolish and you soon find yourself with no allies and pushed out of public life. (you have lost the game.)')
        
        
        if self.jbip == 3:
            input('By not choosing sides, you secure your position to be an ally of whoever wins the war. You also run the risk of you uncle being unforgiving upon his return. \n Press Enter to continue.')
            self.j = 1
        
        if self.j == 1:
            self.two()
        else:
            return None
    def two(self):
        if self.MarriedToCornelia == 0:
            input("It is 2 years  after you have declined to marry Cornelia. Sulla has been named Dictator for life, and you are welcomed in the senate as his ally. \nPress Enter to continue.")
            self.sulla()
        else:
            self.j = rome.ip("self", "2 years after you marry Cornelia, Sulla occupies Rome and becomes Dictator for life. He demands you divorce her and break all ties to your uncle's faction.", "Divorce Cornelia", "Refuse, and be forced into hiding.", "Do nothing")
            if self.j == 1:
                self.MarriedToCornelia = 0
                self.divcor()
            elif self.j == 2:
                self.hiding()
            elif self.j==3:
                self.Sullas()
    def Sullas(self):
        print("Sulla's men find and kill you")
    def sulla(self):
        if rome.ip("self", "Being an ally of Sulla, you may choose to enter public life and begin your climb up the cursus honorum or enter the army as an officer.", "Enter the army", "Enter public life.", " ") == 1:
            self.army()
        else:
            self.ch()
    
    def divcor(self):
        self.j = rome.ip("self", "having divorced Cornelia, Sulla welcomes you in the Senate as you watch all your uncle's (and your) allies get assassinated.", "Flee to the nearby city of Corfinium, the former capital of Sulla's enemies in the social wars", "Wait for the right moment, when Sulla is weak or dies of old age.", "Support Sulla in these endeavors." )
        if self.j == 1:
            print('The people of Corfinium see you as too weak and send your head to Sulla in a gift basket to gain his favor.')
            return None
        if self.j == 2 or self.j == 3:
            input("Having attained favor with Sulla and his supporters, he gives you a chance to serve as a Quaestor or Tribune. Press Enter to proceed.")
            self.ch()
    def hiding(self):
        self.j = rome.ip("self", "Sulla puts a high price on your head and wishes to see you dead as you support his enemies. Luckily, the family of your mother are allies to Sulla, and secure your safety. Sulla says he sees your uncle in you. Despite all this, you fear the political situation in Rome, seeing that it might prove detrimental to your health.", "Join the Army to secure your safety", "Plot to assassinate Sulla", "Do nothing")
        if self.j == 1:
            self.army()
        if self.j == 2:
            self.Sullas()
            return None
        if self.j == 3:
            print('Sulla has his men find you and has you executed.')
    def army(self):
        self.j = rome.ip("self", "you enter in the army at the bottom, starting as an officer. Your superiors see something in you but have said nothing of promoting you. At the seige of a walled city you are placed in the front line. You have the privilage of being able to be the first man over the wall, which will earn you fame back home.", "Rally a group of men and lead them over the wall", "Be the first over the wall alone, being able to attain all the glory for yourself.", "play it safe and don't go near the wall")
        if self.j==1:
            input("Your superiors think highly of you, promoting you to centurion. Press Enter to continue")
            self.bir()
        if self.j == 2:
            self.CC=1
            self.k = random.choice([0,1])
            if self.k == 0:
                print("rushing into battle, you are quickly surrounded and killed.")
                return "X"
            else:
                input("You are quickly surrounded but your fellow men see your effort and save you. Press Enter to continue.")
                self.bir()
        if self.j == 3:
            self.bir()
    def bir(self):
       self.j=rome.ip("self", "You hear news of Sulla's death from Rome.", "Stay in the Army", "Return to Rome", " " )
       if self.j==2:
           self.re()
       if self.j == 1:
           self.stay()

    def stay(self):
        input("your superiors put you at the front line, and time after rime you lead your men to victory press Enter to continue.")
        input("The war ends in a Roman Victory and you are sent back to Rome.")
        self.re()
    def re(self):
        if self.MarriedToCornelia == 1:
            self.j = rome.ip("self", "Returning to Rome, your inheritance is gone and you are forced to live modestly.", "Enter public life and begin the climb up the cursus honorum", "retire with your wife and continue your modest life", "voice your discontent regarding your inheritance to Sulla's supporter's in the Senate")
            if self.j == 1:
                self.ch()
            if self.j == 2:
                print("You retire with your wife, however in the next year she dies. you have nothing to live for and live the rest of your life in despair.")
        else:
            self.j = rome.ip("self", "Returning to Rome, you have the choice of retiring with your wife or entering public life, climbing up the cursus honorum.", "Retire", "Enter Public life")
            if self.j == 1:
                self.ch()
            if self.j == 2:
                print("You retire with your wife, however in the next year she dies. you have nothing to live for and live the rest of your life in despair.")
                return None
        if self.j== 3:
            print("sulla's supporters have you killed")
            time.sleep(99)
    def ch(self):
        if rome.ip("self", "You begin your climb up the cursus honorum, however you must choose wether to run for Quaestor or Tribune.", "Run for Tribune", "Run for Quaestor", " ") == 1:
            self.tribune()
        else:
            self.qu()
    def tribune(self):
        if rome.ip('self', "your official job as tribune is to protect the interests of the plebs(the poor).", "Placate the people", "Serve to the benefit of the rich.", " ") == 1:
            input("The people see you as a good leader, and you gain their support and trust. Press Enter to continue.")
            self.toqu()
        else:
            print("the people yell in the streets, calling you a tyrant, and graffiti riddles the streets of you staling from the poor and giving the money to the rich. You soon find your head dislodged.")
            return None
    def toqu(self):
        if self.MarriedToCornelia ==0:
            input("your term as Tribune is over. Press enter to use your inheritance to secure your position as Queastor")
        else:
            input("Your term as Tribune ends. The unexpected death of one of the Quaestors occurs, and you are appointed in his place. Press Enter to continue")
        self.qu()
    def qu(self):
        if rome.ip("self", "Serving as Quaestor, you are sent to Spain to supervise the treasury. There, you observe a statue of Alexander the Great, and you recall that when he was your age, he was supreme ruler. What you have accomplished is nothing compared to what he has done. You reach an important decision in your life in which you must choose to chase glory or take the easy path.", "Chase glory as Alexander did.", "Choose the easy path.", " ") == 1:
            self.glory()
        else:
            print("you serve your post in Spain with laziness, and your public life ends.")
            return None
    def glory(self):
        if self.MarriedToCornelia == 1:
            rome.ip('self', 'You serve your post in Spain with distinction, and upon returning to Rome you discover your wife is dead and  you are given the option to marry Pompeia, the granddaughter of Sulla.', "Marry her", "Remain a bachelor", ' ')
            self.cae()
        else:
            self.j =rome.ip('self', 'You serve your post in Spain with distinction, and upon returning to Rome you discover that your friends as well as your enemies mock your celibacy and you are given the option to marry Pompeia, the granddaughter of Sulla.', "Marry her", "Remain celibate", " ")
        if self.j == 1:
            input('having regained favor with your peers, you are appointed curule aedile. Press Enter to continue.')
            self.cae()
    def cae(self):
        if rome.ip("self", "As Aedile, you are in charge of issuing edicts on markets(economic manipulation) as well as organization of games that will garner support from the people", "Organize many lavish games and festivals", "Organize nothing, and pocket the money.", " ") == 1:
            input("you gather support for yourself and you are slowly becoming more and more influental. Press Enter to continue")
            self.Pont()
        else:
            print("People begin to resent you and you are prosecuted for the money you took. You are proven guilty and are sentenced to life inprisonment.")
            return None
    def Pont(self):
        self.j = rome.ip('self', 'Serving eith distinction as Aedile, you see the possibility of being able to attain the office on  Pontifex Maximus, Head Priest of Rome. To do this, you must take out many loans to be able to bribe voters, as all other canidates do.', "Take out the loans and bribe voters", "Don't take out any loans, but run for the position", "Don't run")
        if self.j==1:
            self.k=random.choice([1,1,1,0])
        elif self.j == 2:
            self.k = random.choice([0,0,0,1])
        elif self.j == 3:
            self.PontMax= 0
            self.consul()
        if self.k == 1:
            self.PontMax=1
            input("you are now Pontifex Maximus.")
            self.consul()
        if self.k == 0:
            input("you lost the election. Press Enter to continue.")
            self.consul()

    def consul(self):
        self.lis=[0, 1]
        if rome.ip('self', 'Having a taste for elections, it is likely that you can attain the consulship if you bribe the right people.', "Bribe the voters", "Don't Bribe the voters.", " ") ==1:
            if self.PontMax == 1:
                self.lis.append(1)
                if self.CC == 1:
                    self.lis.append(1)
            self.k = random.choice(self.lis)
        else:
            self.lis.append([0, 0])
            if self.PontMax == 1:
                self.lis.append(1)
            if self.CC == 1:
                self.lis.append(1)
            self.k == random.choice(lis)
        self.end()
        
    def end(self):
        if self.k ==1:
            print("You have won the game!")
        else:
            print("you have failed to climb up the cursus honorum. You have failed your family faction, your father and your uncle.(You have lost the game)")
Rome = rome()