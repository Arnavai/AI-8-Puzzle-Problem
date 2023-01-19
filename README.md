# AI-8-Puzzle-Problem
**IMPORTANT** - numpy module must be installed to run the following source code

To execute the file, the following command should be entered into the terminal, after changing current directory to the directory 
containing q2.py : python3 q2.py

Input must be entered as a space separated string of 9 values for both initial state and final state.
Explanation of Source Code :

First we import the math and the numpy library 
Then we take the initial state and final state as input, and reshape them to a 3*3 matrix using numpy.reshape()
Then we define a function, that computes and stores the next states out of the 4 possible ones, and returns a list containing them.
Next we define a function that computes heuristic value as the number of misplaced tiles from the final state.
In the main function, we use a while loop that makes the current state as the one with the least heuristic value.
If the number of steps performed so far are greater than 100, then we break out of the loop, and display error message that
puzzle cannot be solved in less than 100 steps.
Else, we then check if the current state is same as the final state, if yes, we break out of the loop,
else, we go to the next 4 possible states, and increase the steps performed by 1.
