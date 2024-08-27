# Fines

Ion is a policeman in a large city. The city has $N$ intersections connected by $M$ streets that can be traveled in both directions. For each street, the time $C_i$ required to traverse it is known. Informed by a reliable source, Ion knows that $K$ crimes will occur the next day. For each crime $i$, the following data are known: $T_i$ - the time the crime occurs, $A_i$ - the intersection where the crime occurs, $S_i$ - the fine Ion can issue if he is at intersection $A_i$ at time $T_i$. He knows that during the next day he has to meet his wife, but he does not remember the exact place or time for the meeting. All he remembers are $P$ pairs in the form of $X_i$, $Y_i$ which signify that he might need to meet his wife at time $Y_i$ at intersection $X_i$. Given all this data, help Ion find the maximum total value of fines he can issue for each of the $P$ pairs he remembers. From the moment he meets his wife, Ion will not issue any more fines.

## Input data

The first line of the input file `amenzi.in` contains four integers $N$, $M$, $K$, and $P$ with the meanings described above. The following $M$ lines contain three numbers $a$, $b$, and $c$ meaning there is a street connecting intersections $a$ and $b$ which can be traversed in $c$ units of time. The next $K$ lines contain three numbers $a$, $b$, and $c$ meaning there will be a crime at intersection $a$ at time $b$ for which a fine of $c$ monetary units will be issued. Then follows $P$ lines with two numbers $a$ and $b$ indicating that Ion might meet his wife at intersection $a$ at time $b$.

## Output data

The output file `amenzi.out` will contain $P$ lines containing the maximum total value Ion will obtain from fines for each of the $P$ cases described in the input file. If Ion cannot reach the respective intersection at the designated time, print $-1$ for that test case.

## Constraints and clarifications

- Initially, Ion is at intersection $1$ at time $0$.
- The times at which crimes occur and the times when Ion can meet his wife are in the interval $[0, 3500]$
- $0 \leq K \leq 12000$
- $0 \leq P \leq 8000$
- $1 \leq N \leq 150$
- $1 \leq M \leq 1500$
- The time required to traverse a street is a strictly positive integer
- The cost of a fine will be an integer in the interval $[1, 10000]$

## Example

`amenzi.in`
```
5 7 4 2
5 4 4
4 3 5
2 3 7
3 1 3
5 2 3
4 1 10
4 2 1
2 6 5736
2 20 2567
5 6 1530
3 3 4067
1 50 3
15 6634
```

`amenzi.out`
```
4067
4067
```

## Explanation

For the first case, Ion will go to intersection $3$ where he will arrive at time $3$, exactly in time to issue a fine of $4067$. Then he goes to intersection $2$ where he arrives at time $10$. Here he waits until time $20$ to issue the fine of $2567$. He then goes to intersection $1$ where he waits for his wife until time $50$. 

For the second case, Ion goes to intersection $3$ where he arrives at time $3$, issues a fine of $4067$, and then waits for his wife until time $15$.