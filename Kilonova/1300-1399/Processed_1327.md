```markdown
$N$ friends are sitting around $N$ urns containing balls. The friends and the urns are numbered from $0$ to $N-1$. Each urn $i$  $(0 \leq i \leq N-1)$ contains $S_i$ balls. Friends want to extract balls from urns and put them in their pockets. Due to the arrangement, only friends $i$ and $((i+1)$ mod $N)$ can extract balls from urn $i$. Each friend $i$  $(0 \leq i \leq N-1)$ has a pocket capacity of $P_i$ balls (i.e., they cannot extract more than $P_i$ balls in total). Friend $0$ is their leader and asks the question: if I extract exactly $x$ balls from urn $0$, what is the maximum number of balls that all the friends together can extract in total, using an appropriate strategy and considering the problem constraints? An appropriate strategy determines how many balls each friend extracts from each urn from which they can extract balls, considering that friend $0$ necessarily extracts $x$ balls from urn $0$.

# Task
For each possible value of $x$ (from $0$ to $min \{ S_0, P_0 \}$), determine the maximum number of balls that the $N$ friends can extract in total from the $N$ urns.

# Input data
The first line of the `bile.in` file contains the number of tests $T$ described below. The first line of each test contains the number $N$ of friends. Then follow $N$ lines. Line $i$ among these $(0 \leq i \leq N-1)$ contains the integers $S_i$ and $P_i$, separated by a space.

# Output data
In the output file `bile.out`, you will print the answers for each test, in the order in which they are given in the input file. For each possible value of $x$ (considering the ascending order of the values) for the respective test, you will print a line containing the maximum total number of balls that the friends can extract from the urns.

# Constraints and clarifications
* $1 \leq T \leq 10$
* $2 \leq N \leq 15000$
* $1 \leq S_i \leq 16000$
* $1 \leq P_i \leq 16000$
* $40\%$ of the tests have $N \leq 500$ and $max \{ S_0, P_0 \}  \leq 500$  $(0 \leq i \leq N-1)$
* $A \ \text{mod} \ B$ represents the remainder of the integer division of $A$ by $B$.
* A ball can only be extracted once, by a single friend.

# Example

`bile.in`
```
2
4
5 5
3 4
8 6
3 4
4
2 3
6 5
2 4
3 1
```

`bile.out`
```
17
18
19
19
19
18
13
13
12
```

## Explanation
For the first test $x$ can take values between $0$ and $min\{ S_0, P_0 \}=5$.
For $x=0$, the $4$ friends can extract a total of $17$ balls.
For $x=1$, the $4$ friends can extract a total of $18$ balls.
For $x=2$, the $4$ friends can extract a total of $19$ balls.
For $x=3$, the $4$ friends can extract a total of $19$ balls.
For $x=4$, the $4$ friends can extract a total of $19$ balls.
For $x=5$, the $4$ friends can extract a total of $18$ balls.
The value of $x$ was included each time in the total number of balls that the $4$ friends could extract.
```