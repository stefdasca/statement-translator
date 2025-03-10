
# Task
Boghy the Frog was challenged by Zoly the Meerkat to a 100-meter race. The frog can only jump forward, 2 meters at a time.

To maximize her chances of winning, Zoly tried to simulate the frog's jumps in a program, which measures the distance from the initial position at each step. Since Zoly is too busy with her training, she could not finish the program and asks you to help her. You can find the program [here](bad_source.cpp) or in the "Attachments" section on the side.

# Input data
Nothing is provided as input.

# Output data
The screen should display the distance from the initial position at each step, with each distance being separated by a space from the next.

# Constraints and clarifications
The distances will only be displayed for the first 100 meters.

# Example
`stdout`
```
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 
```
## Explanation
In the 100 meters, the frog will jump 2 meters forward at each step. Thus, initially it has jumped 0 meters (it has not jumped yet and the distance from the initial step is 0), then 2 meters, 4 meters, 6 meters, etc.
