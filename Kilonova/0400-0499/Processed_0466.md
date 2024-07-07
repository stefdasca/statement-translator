The Emperor Tiberius Claudius Caesar Augustus Germanicus, passionate about gladiator fights, decided to organize the biggest games ever held in Ancient Rome.

To organize these games, Tiberius called $N$ gladiators to Rome. Then, to arrange them, he decided to place the $N$ gladiators in the following manner: the first gladiator has gladiator $2$ on his right, and no one on his left, gladiator $2$ has gladiator $1$ on his left and gladiator $3$ on his right, ..., gladiator $N-1$ has gladiator $N$ on his right and gladiator $N-2$ on his left, and gladiator $N$ has gladiator $N-1$ on his left, and no one on his right.

The Emperor Tiberius can decide that two gladiators should have a fight only if they are next to each other. After this fight ends, the gladiator who wins returns to the line, and the gladiator who loses leaves the line. When a gladiator loses a fight and leaves the line, all the gladiators to his right move one position to the left.

Each gladiator has a fame level equal to a natural number, and to make the games more spectacular, the emperor decided that whenever two gladiators have a fight, the gladiator with a lower fame level will always win. If two gladiators have equal fame levels, then the one on the left will win.

To measure how spectacular the games are, the emperor invented a number called the "enthusiasm coefficient." This number is equal to $0$ before the games start. Following a fight, the enthusiasm coefficient increases by the difference between the fame levels of the two gladiators. For example, if two gladiators have a fight, and one of the gladiators has a fame level equal to $7$ and the other has a fame level equal to $5$, then the coefficient will increase by $7 - 5 = 2$.

The games end when there is only one gladiator left standing.

Help Emperor Tiberius and tell him what the maximum enthusiasm coefficient he can obtain when the games end.

# Input data

The first line of the console contains the number $N$, and the second line contains $N$ natural numbers separated by a space, representing the fame level of each gladiator.

# Output data

Print a single line with a natural number, which represents the maximum enthusiasm coefficient that can be obtained.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* The fame level of a gladiator is a natural number less than $10^9$;
* For tests worth 15 points, all gladiators have the same fame level;
* For tests worth another 25 points, the first gladiator has the smallest fame level, and the rest of the gladiators are arranged in descending order;
* For tests worth another 20 points, gladiators are arranged in ascending order by fame level;
* For tests worth 55 points, $N \leq 1\ 000$.

# Example 1

`stdin`
```
5
1 2 3 1 7
```

`stdout`
```
9
```

## Explanation

We can obtain the enthusiasm coefficient $9$ as follows:

- Initially, the enthusiasm coefficient is equal to $0$;
- We choose the first fight to be between gladiator $4$ and gladiator $5$. The enthusiasm level increases by $7-1=6$, becoming $6$, and gladiator $5$ leaves the line. Thus we are left with gladiators: $\\{1, 2, 3, 4\\}$;
- The second fight will be between gladiator $1$ and gladiator $2$. The enthusiasm level increases by $2-1=1$, becoming $7$, and gladiator $2$ leaves the line. Thus we are left with gladiators: $\\{1, 3, 4\\}$;
- The third fight will be between gladiator $1$ and gladiator $3$. The enthusiasm level increases by $3-1=2$, becoming $9$, and gladiator $3$ leaves the line. Thus we are left with gladiators: $\\{1, 4\\}$;
- The final fight will be between gladiator $1$ and gladiator $4$. The enthusiasm level increases by $1-1=0$, becoming $9$, and because the gladiators have equal fame levels and gladiator $1$ is on the left, gladiator $4$ leaves the line. Thus we are left with gladiator: $\\{1\\}$.

The way of choosing the fights is not necessarily unique.

# Example 2

`stdin`
```
5
1 2 5 6 8
```

`stdout`
```
17
