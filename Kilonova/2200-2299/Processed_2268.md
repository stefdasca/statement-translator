Beyond nine seas and nine countries, in a great empire, Princess Alexandra has fallen deeply in love with Făt-Frumos, the strongest and bravest man. Unfortunately for her, many years ago, during a battle against Gefghev, the tyrannical emperor of that time, Făt-Frumos drastically lost karma and, because of this, he is no longer allowed to approach public institutions. Therefore, whenever the two want to meet, Făt-Frumos sends Alexandra a note through a carrier pigeon. On the note, Făt-Frumos writes the nearest train station to the forest where he is hiding. Thus, Alexandra has to go to the nearest train station and from there get to the station indicated by Făt-Frumos. Here comes Alexandra’s mother who will not let her daughter abandon her princely responsibilities so easily. Every time the girl wants to meet Făt-Frumos, she has to tell her mother the exact time the train will take from the departure station to the station indicated by Făt-Frumos. Alexandra knows the railway system of the empire very well and knows the following:

* Between any two stations, there is a unique route that does not go through the same station twice.
* For any two stations directly connected by a railway line, Alexandra knows the distance between the stations and the maximum speed at which a train can travel on that line.

# Task

Alexandra does not feel comfortable doing calculations, especially since the empire is very large and the calculations can become quite complicated. For this reason, she asks you to make a program that receives the configuration of the railway system and answers questions of the form $x \; y \; v$, with the following meaning: *“How much time will a train that can travel at a maximum speed $v$ need to go from station $x$ to station $y$�*.

# Input data

The first line of the input file `trenuri.in` contains two numbers: $N$ and $M$, representing the number of stations in the railway system, and the number of questions Alexandra asks, respectively. On the next $N - 1$ lines, there are $4$ numbers each $x \; y \; d \; v$ meaning that there is a direct railway line from station $x$ to station $y$ with length $d$, which cannot be traveled at a speed higher than $v$. The next $M$ lines contain three numbers: $x \; y \; z$, representing the questions asked by Alexandra, with the meaning described in the statement.

# Output data

The output file `trenuri.out` will contain $M$ numbers, one per line, representing the answers to Alexandra’s questions with a precision of three decimals.

# Constraints and clarifications

* $3 < N, M < 100 \; 000$
* For $30\%$ of the tests $M < 100$
* The length of a route will be a natural number less than $100 \; 000$
* The maximum speed a train can reach is a natural number less than or equal to $1 \; 000$
* For each question, it is known that the train will take the minimum path between station $x$ and station $y$
* Any train travels at the minimum of the maximum speed it can reach and the maximum speed allowed on the railway line it is on.
* The maximum difference by which the final result can vary from the correct one is $0.001$

# Example

`trenuri.in`
```
4 2
1 2 4 2
1 3 6 5
3 4 2 10
1 4 7
2 3 4
```

`trenuri.out`
```
1.485
3.500
```

## Explanation

The first train will travel the route from station $1$ to station $3$ at speed $5$, and the route from station $4$ to station $4$ at speed $7$. Thus, the total time will be: $\\frac{6}{5} + \\frac{2}{7} = 1.485714286$