```markdown
# Task

JellyTheOctopus just bought the game City Skylines! The goal of the game is to create a prosperous city. So far, Jelly's city has $N$ districts (numbered from $1$ to $N$) connected by $M$ different roads (two districts have at most one undirected road between them).

There are three types of districts: industrial, business, and residential. An industrial district is where the city gets its resources (e.g., mining, forestry, agriculture, etc.). Nobody wants to deal with coal mines, so each industrial district contributes $-1$ point to Jelly's city's total prosperity. A business district is where the city's companies and jobs are located. Since this part helps the city get money, each business district contributes $1$ point to Jelly's city's total prosperity. A residential district is where all the houses and apartments are located. These are just a basic necessity, so each residential district contributes $0$ points to the city's total prosperity.

Not only does Jelly care about the general _prosperity_ of his city, but he also wants his city to be _balanced_. The definition of a _balanced city_ is as follows: for each district $a_i$, the _prosperity_ of district $a_i$ must be equal to the sum of the _prosperities_ of all the adjacent districts (i.e., all districts connected to $a_i$ by a single road). It is possible that the current state of Jelly's city is not _balanced_. For this reason, he asks you to help make his city _balanced_. You can add new districts as follows: take any district already in Jelly's city, then connect a completely new district (of any type) with a road. Once you add a new district, it becomes part of Jelly's city (so you can add another new district connected to the one you just created). Additionally, you can only add one district at a time.

Help Jelly find the minimum number of new districts needed to create a _balanced_ city.

# Input data

The first line contains two natural numbers, $N$ and $M$, representing the number of districts and the number of roads that initially connect them.

The next line contains $N$ integer values, $a_i$, representing the type of each district (a $-1$, $0$, or $1$).

The next $M$ lines contain two values, $u$ and $v$, representing an undirected road between $u$ and $v$.

# Output data

The first line will contain $K$, the minimum number of districts Jelly needs to add to build a _balanced_ city.

# Constraints and clarifications

* $1 \leq N \leq 10^5$;
* $1 \leq M \leq \min(10^5, \frac{N \cdot (N-1)}{2})$;
* $-1 \leq a_i \leq 1$;
* Each pair of districts has at most one road connecting them.
* If $k$ new districts are added, there must be exactly $k$ new roads between districts.

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|40|$N \leq 100$|
|2|60|No additional constraints|

# Example

`stdin`
```
3 2
0 1 -1
1 2
1 3
```

`stdout`
```
2
```

## Explanation

Additional clarifications related to adding new districts. If, for example, Jelly has a city with $5$ districts, you can add a new district to district $5$. (Thus, we now have a road between districts $5$ and $6$, and now, Jelly's city has $6$ districts. District $6$ is now part of Jelly's city and **you cannot** create a road from district $6$ to one of the first $5$ districts. However, since $6$ is now part of the city, you can add a new road from $6$ to another district (e.g., a road between districts $6$ and $7$).
```
