*“As you have gone, so shall you return!�*  
old Oltenian proverb*

The Gorj region consists of $N$ cities, connected by $M$ **one-way** roads. The roads are of two types: $\\text{\\textcolor{red}{trails}}$ (represented by $\\text{\\textcolor{red}{0}}$) and $\\text{\\textcolor{blue}{national roads}}$ (represented by $\\text{\\textcolor{blue}{1}}$). Nea Marin starts from a city and wants to create a route with the following properties:
* The route starts and ends in the same city.
* At each step, Nea Marin walks on one of the roads that have the current city as the source, following the direction of travel. Thus, he reaches the destination city of the road, from where the process repeats at the next step.
* To avoid getting bored, the scenery must **NOT** be monotonous. He considers the scenery of the route to be monotonous if the route consecutively passes through two $\\text{\\textcolor{red}{trails}}$ or through two $\\text{\\textcolor{blue}{national roads}}$.
* Additionally, the scenery must be balanced, meaning that the total number of roads traversed of each type must be equal.

You, renowned programmers, are now in a predicament – you must determine from which cities Nea Marin can start to create a route with the properties described above.

# Task
Given the $N$ cities in the Gorj region, numbered from $1$ to $N$, and the $M$ roads connecting the cities, each specified by the two cities it connects (i.e., the source and destination of the road) and the type of road, determine from which cities $x$ Nea Marin could start a balanced and non-monotonous route, as described above.

# Input data
The first line contains the natural numbers $N$ and $M$, separated by a space.

The next $M$ lines each contain a triplet of natural numbers $a\ b\ c$, with numbers separated by spaces and with the meaning that there exists a road $a \rightarrow b$ connecting cities $a$ and $b$, of type $c$ ($\\text{\\textcolor{red}{0}}$ for trails, $\\text{\\textcolor{blue}{1}}$ for national roads).

# Output data
The single line will print a string consisting of $N$ binary digits. The $i$-th digit for $1 \leq i \leq N$ is $1$ if and only if Nea Marin can create a balanced and non-monotonous route starting from city $i$, of the type described in the statement. Otherwise, the digit will be $0$. **The digits will be displayed without spaces between them!**

# Constraints and clarifications
* $1 \leq N \leq 40\ 000$
* $1 \leq M \leq 200\ 000$
* It is possible that some of the $M$ roads $a \rightarrow b$ have $a = b$, just as in an Oltenian road system. Also, for some pairs $(a, b)$, there may be multiple roads $a \rightarrow b$.
* Note that Nea Marin's route can pass through the same node multiple times (see examples).

## Subtask 1 (15 points)
* $N \leq 8, M \leq 22$
## Subtask 2 (17 points)
* $N \leq 600, M \leq 3\ 000$
## Subtask 3 (19 points)
* It is guaranteed that for any 51 distinct cities chosen from the N, there exists among them two cities $a$ and $b$ with the following property: if there is a route from $a$ to $b$ (regardless of the type of roads that compose it) then there is no route from $b$ to $a$.
## Subtask 4 (20 points)
* There are exactly $N$ national roads, namely $1\ \rightarrow 2, 2\ \rightarrow 3, ..., (N-1)\ \rightarrow N$ and $N \rightarrow 1$.
## Subtask 5 (29 points)
* No additional constraints.

# Examples
`stdin`
```
3 3
1 2 0
2 3 1
3 1 1
```
`stdout`
```
000
```
Explanation
---
There is a single route $1 \rightarrow 2 \rightarrow 3 \rightarrow 1$. Regardless of which city Nea Marin starts the route, it will not be balanced, being composed of two national roads and one trail.
~[sem1.jpg]

`stdin`
```
2 3
1 2 0
2 1 1
2 2 1
```
`stdout`
```
11
```
Explanation
---
Nea Marin can traverse the route $1 \rightarrow 2 \rightarrow 1$, which is both balanced and non-monotonous, regardless of whether it starts from city $1$ or city $2$.
~[sem2.jpg]

`stdin`
```
7 9
1 2 0
2 6 1
4 2 1
6 4 0
2 3 0
5 3 1
3 5 1
2 7 0
7 1 1
```
`stdout`
```
1101011 
```
Explanation
---
Nea Marin can traverse the route $1\rightarrow 2\rightarrow 6\rightarrow 4\rightarrow 2\rightarrow 7\rightarrow 1$, which is both balanced and non-monotonous. Thus, for cities $1, 2, 4, 6$, and $7$, the corresponding positions will print $1$. For cities $3$ and $5$, the answer is $0$ because there are no trails leading from them.
~[sem3.jpg]