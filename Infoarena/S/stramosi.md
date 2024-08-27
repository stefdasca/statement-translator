# Ancestors

Gigel's family is very large, having exactly $N$ members. Each member knows who their direct ancestor is, except for a few very old members who do not even remember who their direct ancestor was. Gigel, being a curious person, made an inventory of his family, meaning that he numbered each member with a distinct number between $1$ and $N$, and he also knows for each member who their direct ancestor is (if they exist). His curiosity is even greater, as he asks himself $M$ questions of the form: "Who is the $P$-th ancestor of the member numbered $Q$?"

## Task

Write a program that correctly answers all of Gigel's $M$ questions.

## Input data

The first line of the file `stramosi.in` contains the numbers $N$ and $M$. The second line contains $N$ integers, representing the ancestors of all members, starting with member $1$ and ending with member $N$. If a member does not have an ancestor, then the file will contain the number $0$. The following $M$ lines contain pairs of numbers $Q$ and $P$, representing a question of the form: "Who is the $P$-th ancestor of the member numbered $Q$?"

## Output data

Each of the $M$ lines of the file `stramosi.out` will contain the answers to the questions, that is, the order numbers of the ancestors (or $0$ if the identity of the ancestor is not known).

## Constraints

$1 \leq N \leq 250\ 000$ 

$1 \leq M \leq 300\ 000$ 

The order number of any member's ancestor is less than or equal to the order number of that member.

## Example

`stramosi.in` 
```
13 7 
0 1 2 2 4 1 6 0 8 8 10 10 12 
5 2 
3 2 
7 1 
1 3 
13 3 
9 2 
11 1 
```

`stramosi.out`
```
6 
0 
8 
0 
10 
2 
10 
```