# Tribal Council

The Kazooba tribe consists of $N$ people who wish to gather for a tribal council. All the people are descendants of a single person, who is the tribe leader. Since all people of this tribe live long lives, the ancestors of each person, including the tribe leader, are alive and will attend the council. People arrive at the council in a specific order and sit at tables as they arrive. They sit in a row of parallel tables. The first table is placed at the base of the Sacred Mountain, and the row extends infinitely to the west (opposite side of the mountain). On the other hand, each person would like to be as close to the divinity as possible, so when they arrive, they sit at the closest table to the Sacred Mountain that none of their children or their father has sat at. As usual, the tribe gods have a particular inclination for beauty. They would like to ask the tribe members to arrive at the council in an order that maximizes the number of occupied tables. Unfortunately, they have no programming inclination, so they asked you to write a program for this.

## Task

Write a program that determines the maximum number of tables that can be occupied at the council.

## Input data

The first line of the file `trib.in` contains an integer $N$, representing the number of people in the tribe. People are numbered from $1$ to $N$; their leader is number $1$. Each of the following lines contains two numbers $A$, $B$ meaning "there is a direct kinship between persons $A$ and $B$". The relationships described in the input file are correct (for example, there are no cycles, and each person is one of the leader's descendants).

## Output data

The file `trib.out` contains a single line that contains the maximum number of tables that can be occupied.

## Constraints and clarifications

$1 < N \leq 100,000$

for 30% of the tests $N \leq 1,000$

any table has unlimited capacity

## Example

`trib.in`
```
5
1 4
3 2
1 3
3 5
3
```

`trib.out`
```
3
```

## Explanation

If people arrive in the order $2$, $4$, $1$, $5$, $3$, they sit as follows:
- 2 sits at the first table
- 4 sits at the first table
- 1 has a son (4) at the first table, so he sits at the 2nd table
- 5 sits at the first table
- 3 has 2 sons at the first table (2 and 5) and his father (1) at the 2nd table, so he sits at the 3rd table