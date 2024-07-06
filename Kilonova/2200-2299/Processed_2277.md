Preparing for their participation in the famous Petrozavodsk camp, The-Winner and the rest of their team (who are irrelevant, the only important one being The-Winner) spend a lot of time at the university, solving various algorithm problems. They like pizza very much, so much so that when they get pizza, the team's productivity doubles. More precisely, when they don't have pizza, the team solves one problem per hour, and when they receive pizza they solve $2$ problems per hour.

For each of the last $Z$ days, the time spent at the university by The-Winner's team is known as well as whether they received pizza or not. If they receive pizza, they get it at the beginning of the day and its effects last throughout the day.

# Task

However, since pizza is not free, their coach wants to see if it was worth paying for the food. To be convinced of this, he wants to know how many problems the team has solved in the last $Z$ days.

# Input data

The first line contains a single natural number, $Z$ (with the significance mentioned in the statement). On the next $Z$ lines there are three natural numbers: $h_1$, $h_2$ and $pizza$. The first two represent the starting and ending hours of solving problems on that day, and the third number is either $0$, meaning they didn't receive pizza on that day, or $1$, meaning their coach bought them pizza on that day.

# Output data

The first line will contain a single natural number, representing the number of problems solved by the team in the last $Z$ days.

# Constraints and clarifications

* $1 \leq Z \leq 100\ 000$;
* $0 \leq h_1 \leq h_2 \leq 24$;
* $pizza \in \{0, 1\}$.

# Example

`stdin`
```
7
10 15 0
8 20 1
13 14 0
13 14 1
10 12 0
10 17 1
0 0 1
```

`stdout`
```
48
```

## Explanation

On days $1$, $3$, and $5$ they did not receive pizza, so $5 + 1 + 2 = 8$ will be added to the answer. On the remaining days, they receive pizza, so $12 \cdot 2 + 1 \cdot 2 + 7 \cdot 2 + 0 \cdot 2 = 40$ will be added to the answer. In total, The-Winner and their team solved $48$ problems.

