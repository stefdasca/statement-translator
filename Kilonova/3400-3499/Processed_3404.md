In a distant galaxy, General Coba has a new fleet of $n$ spaceships with which he wishes to conquer the entire galaxy. Each spaceship is represented by a code. The significance of the spaceship codes is that each divisor of the code represents the ID of a crew member on board. Thus, each spaceship has a number of people on board equal to the number of divisors. Some ships benefit from a set of state-of-the-art laser weapons. These ships can be identified by the property that the sum of the crew members' IDs is odd.

# Task

To conquer the galaxy, General Coba needs your help. He needs to know:
1. The **total number of members** from all the crews of the fleet.
2. The number of **ships with laser weapons** in his fleet.

# Input data

The first line contains the number of the task $C$, which can be 1 or 2.  
The second line contains the number $n$ as described in the statement, and the third line contains $n$ numbers.

# Output data

For either of the two tasks, a single natural number will be printed, representing the answer to the task.

# Constraints and clarifications

* $C \in \{1, 2\}$;
* For $C=1$, $1 \leq n \leq  25\ 000$;
* For $C=2$, $1 \leq n \leq  200\ 000$;
* $1 \leq a_i \leq 5\ 000\ 000$, where $a_i$ represents the $i$-th term of the array, $1 \leq i \leq n $;
* For fast reading and displaying, it is recommended to use these lines of code at the beginning of the `main` function:
```cpp
ios::sync_with_stdio(false);  
cin.tie(NULL);  
cout.tie(NULL);  
```

| # | Score |                    Constraints                    |
| - |:-----:|:------------------------------------------------:|
| 1 | 10    |    $C = 1 $ and $n \leq 1\ 000$                  |
| 2 | 20    |    $C = 1$ and no additional constraints         |
| 3 | 10    |    $C = 2 $ and $n \leq 1\ 000$                  |
| 4 | 40    |    $C = 2$ and  $n \leq 50\ 000$                 |
| 5 | 20    |    $C = 2$ and no additional constraints         |

# Example 1

`stdin`
```
1
7
9 10 5 2 72 32 6 
```

`stdout`
```
33
```

## Explanation

The ships have in order: $3$, $4$, $2$, $2$, $12$, $6$, $4$ members on board. In total there are $33$ members in the crews of the fleet.

# Example 2

`stdin`
```
2
7
9 10 5 2 72 32 6 
```

`stdout`
```
4
```

## Explanation

The ships that have laser weapons on board are: $9$, $2$, $72$, $32$.