Several mountain-loving friends are having a true adventure during one day of their winter vacation. Surprised by the difficulty of the chosen route and the rapid worsening of weather conditions (snow and blizzard), they realize as night falls that it would be better to take shelter for the night and head back to the cabin the following morning. Luck seems to favor them in the end. On the other side of the abyss at whose edge they are standing, they spot a shelter... Upon exploring the surroundings, they find a wooden bridge that could help them cross the abyss. After a closer evaluation, they realize that crossing will not be easy, as there are several missing planks, and the condition of the bridge allows at most 2 people to cross at a time. Visibility is extremely limited and there is only one functional flashlight that will have to be used judiciously to ensure the safe crossing of all group members. The crossing will be done alternately in both directions to be able to bring the flashlight back to those who haven't crossed yet.

# Task

Knowing the number of group members, the crossing time for each of them (expressed in seconds), and knowing that, in a crossing involving two members, the time is given by the crossing time of the slowest among them, find an appropriate strategy so that all group members can cross the abyss in the shortest possible time. If there are multiple solutions with the same minimum crossing time, determine only one, any of them.

# Input data

The input data is taken from the file `prieteni.in`. This contains on the first line the value $n$, the number of friends, and on the next $n$ lines, a number per line, the number $t_i$ found on the line $i+1$ from the file, representing the time (expressed in seconds) in which person $i$ from the group can cross the bridge alone.

# Output data

The solution will be written in the file `prieteni.out`. The first $n$ lines will describe the strategy followed to achieve this minimum time: each line $i$ will contain one or two values, indicating the person or persons crossing the bridge at step $i$. Each person is indicated by their crossing time, as specified in the input data file `prieteni.in`. 
On the last line, the value representing the total minimum time (expressed in seconds) required for all $n$ members of the group to cross the abyss will be printed.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$;
* At any moment, at most $2$ group members can cross the bridge;
* $ 1 \leq  t_i  \leq 1\ 000$;
* There may be multiple people with the same crossing time, but in specifying the solution, it does not matter to whom the respective time belongs.

# Example

`prieteni.in`
```
3
2
3
5
```

`prieteni.out`
```
2 3
2
2 5
10
```

## Explanation

First, persons $1$ and $2$ cross, with times $2$ and $3$ seconds, respectively. The crossing time for this trip is given by the longest time: $3$ seconds. Then person $1$ returns with the flashlight, the crossing time being $2$ seconds. In the third crossing, persons $1$ and $3$ cross, with times $2$ and $5$ seconds, respectively. This time, the crossing time for this trip is given by the longest time: $5$ seconds. Total time: $3+2+5=10$ seconds.

This is one of the possible strategies. Another correct solution: first person $1$ crosses with person $3$, returns person $1$, and then person $1$ crosses with person $2$, and in this case the same minimum time of $10$ seconds is obtained.