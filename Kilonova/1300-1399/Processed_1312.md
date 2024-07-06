In the forest with hazelnuts, there were $n$ dwarfs with houses numbered from $1$ to $n$, a squirrel comes and says, "I want to stay here too!".

The $n$ houses are arranged in a line and each house is identified by a sign with a number. The first house belongs to the dwarf numbered $1$ and has the sign with number $1$, the second house belongs to the second dwarf and has the sign with number $2$, and so on, the last house belongs to the dwarf with number $n$ and has the sign with number $n$. Hearing that the squirrel wants to enter a house, no dwarf wants to receive it into their house.

One day, after the dwarfs left home, the upset squirrel took the signs off the houses, mixed them up, and placed each sign on a different house. Upon returning, the dwarfs see that their houses no longer have signs and each of them must retrieve the sign of their own house. Each dwarf enters their house, finds the sign there, and moves to the house with the number equal to the number written on the found sign. Then, they continue in the same way with the new sign found until the dwarf discovers the sign of their own house. During the search for a sign, it can happen that a dwarf, due to the found sign, moves from the house they are in to a house located to the left. This is considered a backtrack during the search.

# Task

Write a program to determine:

1. How many dwarfs find their own signs in their houses;
2. What is the largest number of houses visited by a dwarf until they find their own sign (counted starting from their own house to the house containing the sought sign, including it);
3. The dwarf who visited the most houses and made the fewest backtracks. If there are multiple dwarfs who meet these conditions, display the dwarf with the smallest number.

# Input data

From the input file `case.in` read the first line containing the number $n$ which represents the number of houses. From the second line, read $n$ numbers, separated by a space, which represent the numbers of the signs placed by the squirrel in the houses.

# Output data

In the output file `case.out` print on the first line a single number representing how many dwarfs find their own signs in their houses. The second line will contain a single natural number representing the largest number of houses visited by a dwarf until they find their own sign. The third line will contain a single number which represents the dwarf who visited the most houses and made the fewest backtracks; if there are multiple dwarfs who meet these conditions, display the dwarf with the smallest number.

# Constraints and clarifications

* $1 \leq n \leq 10 \ 000$
* Partial scores are awarded: $30\%$ of the score for requirement $1$, $40\%$ of the score for requirement $2$, and $30\%$ of the score for requirement $3$.

# Example

`case.in`
```
4
3 2 4 1
```

`case1.out`
```
1
3
1
```

## Explanation

There are 4 houses:
~[case1.png|align=center] 
After the squirrel hides the signs in the houses:
~[case2.png|align=center]
Signs found by dwarf $1$: $3 - 4 - 1$, visited $3$ houses, backtracks $0$
Signs found by dwarf $2$: $2$, visited $1$ house, backtracks $0$
Signs found by dwarf $3$: $4 - 1 - 3$, visited $3$ houses, backtracks $1$
Signs found by dwarf $4$: $1 - 3 - 4$, visited $3$ houses, backtracks $1$
The largest number of houses visited by a dwarf is $3$. Among dwarfs $1$, $3$, and $4$ who visited exactly $3$ houses, only dwarf $1$ has $0$ backtracks.