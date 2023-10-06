#Define the base class Player
class Player:
    def play(self):
      print("The player is playing cricket.")

#Define the base class Batsman
class Batsman(Player):
    def play(self):
      print("The batsman is batting.")

#Define the derived class Bower
class Bowler(Player):
    def play(salf):
      print("The bowler is bowling.")
      
#create objects of Batsman and Bowler classes 
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()

