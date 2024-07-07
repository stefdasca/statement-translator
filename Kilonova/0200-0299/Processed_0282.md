
In the city of programmers, there is a famous place where people can have fun as much as they want, at any hour. The mayor of the city of programmers has built, starting from this place, several roads to the houses of all citizens, houses coded with numbers from $2$ to $n$, the place being coded with $1$. If there are no other houses between a house and the place, then the road is built directly between the two buildings, but if there are other houses between the house and the place, then the road will be formed by the road from the place to the first house, then the road from the first house to the second house, then from the second house to the third house and so on until it reaches the current house.

The city is coded as an array $t[\\ ]$, where $t[i] = 0$ if the building $i$ is exactly the place where the people of the city can have fun or $t[i] = y$, with $y \\neq 0$, meaning that from house $i$ you can reach the house/building $y$ which is between the place and the current house.

Andrei and Alexandru are residents of this city. They live in houses coded with $x_1$ and $x_2$ respectively. They want to meet on the way to the place where they will have fun, so they want to find out which is the first house where they can both arrive, on the way to the place.

# Task
For $q$ questions in the form "which is the first house where Andrei and Alexandru can meet if they live in houses $x_1$ and $x_2$?", find the answer to these questions.

# Input data
The first line contains numbers $n$ and $q$. The second line contains the array $t[\\ ]$, with the meaning from the statement, for all indices from $2$ to $n$. For $i = 1$, it is considered that $t[i] = 0$.
The next $q$ lines contain two numbers $x_1$ and $x_2$ each, with the meaning from the statement.

# Output data
Print the answer for each question, on different lines.

# Constraints and clarifications
* $1 \\leq n \\leq 100 \\ 000$;
* $1 \\leq q \\leq 4 \\ 000 \\ 000$;
* There is exactly one road from the place to each house in the city of programmers.
* It is recommended to use fast input reading with these lines of code at the beginning of the `main()` function: `cin.tie(0)->sync_with_stdio(0);`.

# Example
`stdin`
```
5 2
1 1 2 2
1 2
4 5
```

`stdout`
```
1
2
```
