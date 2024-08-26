## Task

In the hi6 social network, each of the $N$ users is associated with an id in the form of an integer. We say that two users are friends if there is a friendship relationship between them in the social network. To increase the popularity of the social network and boost user interaction, we need to implement a system where a user is shown a list of people they are very likely to know and who are suggested for them to add as friends. The first step to achieve this is to generate a list for each user of people they are not friends with but with whom they have at least one common friend.

## Input data

The input file `fof.in` contains on the first line two natural numbers $N$ and $M$, representing the number of users and the number of friendship relationships in the hi6 network, respectively. The next $M$ lines define the friendship relationships, one per line, in the form of pairs of ids.

## Output data

The output file `fof.out` will contain $N$ lines. On line $i$, $(1 \leq i \leq N)$ the suggestion list generated for the user with id $i$ will be displayed. The displayed list will be sorted in descending order by the number of common friends, and in case of a tie, in ascending order by id.

## Constraints and clarifications

$1 \leq N \leq 1000$  
$1 \leq M \leq 5000$  
All ids are distinct natural numbers between $1$ and $N$.

## Example

`fof.in`
```
3 2
2 1
2 3
```

`fof.out`
```
3
1
```