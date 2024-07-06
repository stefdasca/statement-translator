Now that Ghiță is the president of the new country Ainamor, he wants to invest in transportation infrastructure. However, he will try to use as little money as possible to save the budget.

Ainamor consists of $N$ cities ($N \leq 1\ 000$) in a Cartesian plane, each city having two coordinates $x$ and $y$. A road can be built between any two cities, and its cost is equal to the square of the distance between them.

# Task
Since Ghiță is very busy with press conferences, he asks you to calculate the minimum cost to build roads in Ainamor such that, starting from any city, we can reach all other cities.

# Input data
The first line contains a natural number $N$.
The next $N$ lines each contain 2 integers representing the $x$ coordinate and the $y$ coordinate of a city.

# Output data
Print a number representing the minimum cost to build roads in Ainamor, considering the specifications from the task.

# Constraints and clarifications
* $1 \leq N \leq 1\ 000$;
* The coordinates of any city are integers and belong to the interval $[-10\ 000, 10\ 000]$.

# Example
`stdin`
```
4
1 1
2 2
5 1
1 3
```
`stdout`
```
14
```

## Explanation
In the image below, the way the cities in the example will be connected is described.
The cost of building these roads is $AD^2 + BD^2 + CD^2 = \sqrt{2}^2 + \sqrt{2}^2 + \sqrt{10}^2 = 2 + 2 + 10 = 14$
~[ainamor_exemplu.png]