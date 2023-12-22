This program is meant to simulate the Monty Hall problem. 

This program consists of two scripts. The first one is monty_hall.py which simulates the Monty Hall problem, given the different conditions that we determine (number of times that we play the game, whether or not we switch doors and how many doors there are). The other script is visualization.py which runs the simulations and uses the conditionsof the simulations that we runm as well as the percentage of times that we won in  order to create a visualization where the x axis is how many times we played the game and the y axis is the win percentage. 

What we should be seeing is that as we play the game more and more times, the win percentage starts to approach the statistical probability of a certain condition being met. Essentially, through this exercise we will be demonstrating a proof of the “Central Limit Theorem”. 

The Monty Hall game is should be simulated 400 times where half of those times the simulation is switching doors and half of those times it is not switching doors. Each simulation is using 3 doors to play the game. We can see that as the amount of times that we play the game increases, the values cluster around the specific probabilities, where the probability of winning if we switch doors is 66 % and the probability of winning if we don’t switch doors is 33 %

This program outputs the result by saving an image onto the repository from which it is running. This image is a graph which showcases the outcomes of multiple games where the player switched the door and the ones where they did not. This program requires Seaborn package.
