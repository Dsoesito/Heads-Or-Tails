import random

class Player:
    
    def __init__(self, name):
        self.name = name
        self.heads = 0
        self.tails = 0
           
    def coin_flip(self):
        
        play_on = True 
        while play_on == True: # keep palying until player opts out
        
            flip = random.randint(0,1) # flip coin
            
            if (flip == 0): # result is heads
                self.heads += 1
                print("Heads!")
                print("You have", self.heads, "heads.") # recap totals
                print("You have", self.tails, "tails.")
                response = input("Would you like to play again? Y or N: ") # ask to paly again
                
                if response.upper() == "Y": # play again
                    play_on = True
                    
                else:
                    print("Thank you for playing!") # end game
                    play_on = False

            else: # result is tails
                self.tails += 1
                print("Tails!")
                print("You have", self.heads, "heads.") # recap totals
                print("You have", self.tails, "tails.")
                response = input("Would you like to play again? Y or N: ") # aak to play again
                
                if response.upper() == "Y": # play again
                    play_on = True
                    
                else:
                    print("Thank you for playing!") # end game
                    play_on = False

user1 = Player("Daniel")

user1.coin_flip()
