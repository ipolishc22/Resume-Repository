import monty_hall
import pandas as pd
import seaborn 

class Plot():
    """This class stores the data for 
    a particular instance of a simulation 
    of the monty hall problem. It 
    contains functionality to export 
    a visualization of the win percentages.

    Atributes:
        doors - number of doors to choose from

        iterations - number of times the game is played

        sequence - a list of the results of every played game 
    """

    # python3 visualization.py

    def __init__(self, doors=3, iterations=200):

        """Using the play_game() function
        this function playes the game and 
        makes a plot using the make_plot()
        function.

        Args:
            doors - defaults to 3. number of 
            doors the player chooses from

            iterations - number of games the player
            plays. 
        """
        self.sequence = []
        i=1
        switched = False
        self.doors = doors
        self.iterations = iterations
        
        while i <= iterations:

            if i%2 == 0:
                sim = monty_hall.Simulation(doors)
                switched = True
                per = sim.play_game(switched, i)
            elif i%2 == 1:
                sim = monty_hall.Simulation(doors)
                switched = False
                per = sim.play_game(switched, i)

            # per = sim.play_game(switched, i)

            dict = {"iterations" : i, 
                    "percentage" : per, 
                    "doors" : doors,
                    "switched" : switched}
            
            self.sequence.append(dict)
            i += 1

        self.make_plot()


    def make_plot(self):
        """Makes a plot using seaborn
        and saves it into the directory 
        you are currently working in right now. 
        """
        df = pd.DataFrame(self.sequence)
        plot = seaborn.lmplot(data=df, x="iterations", y="percentage", hue="switched")
        plot.savefig(f"{self.doors}doors_and_{self.iterations}iterations.png")

if __name__ == "__main__":
    plot = Plot(3, 400)
