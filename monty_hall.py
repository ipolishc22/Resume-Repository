import random

class Simulation():
    """Simulation takes an attribute, an integer,
    which represents the amount of doors that the
    simulation will use to play the game.
    """

    # python3 monty_hall.py

    def __init__(self, numdoors):
        """Set an attribute named numdoors
        that will be the number of doors that 
        will be used to play the game.
        """
        self.numdoors = numdoors


    def set_random_doors(self):
        """Uses numdoors number to create a list 
        containing zonk strings. It then replaces 
        one of those items in the list to the 
        string “car” at random. Returns this list.
        
        Args:
            self

        Returns:
        zonk_list(list) - list containing "zonk"s
        """
        zonk_list = []
        i = 0
        while i < self.numdoors:
            zonk_list.append("zonk")
            i += 1

        r = random.randint(0,self.numdoors-1)
        zonk_list[r] = "car"
        return zonk_list


    def choose_doors(self):
        """Chooses two random numbers
        and removes the values from 
        the doors list at those 
        indexes and saves them. 

        Args:
            self

        Returns:
            userdoor, altdoor - tuple containing
            two string values either "car" or
            "zonk"
        """
        var = self.set_random_doors()
        # choosing a random door and removing it 
        ran = random.randint(0, len(var)-1)
        userdoor = var.pop(ran)
        var.remove("zonk")
        # choosing another door, which is the first door 
        alt = random.randint(0, len(var)-1)
        altdoor = var.pop(alt)
        # returning a tuple with those two doors
        return userdoor, altdoor
    

    def play_game(self, switch=False, iterations=1):
        """Playes a game a certain number of times
        by repeatedly calling on the choose_doors()
        function. Every time adding +1 to the wins.
        Calculates the percentage of wins to the total
        number of iterations.

        Args:
            switch - defaults to False
            whether a player switched doors

            iterations - defaults to 1. Number of
            games played consequetively. 

        Returns:
            percentage - wins / iterations
        """
        i = 0
        win = 0
        loss = 0

        while i < iterations:
            tup = self.choose_doors()
            if switch==False and tup[0]=="car":
                win+=1
            elif switch==True and tup[1]=="car":
                win+=1
            else:
                loss += 1
            i += 1

        percentage = win / iterations
        return percentage


if __name__ == "__main__":
    sim = Simulation(3)
    sim.play_game(True, 1_000)
