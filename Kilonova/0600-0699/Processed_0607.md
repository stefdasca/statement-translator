```markdown
# Statement
RAU-Gigel nostalgically remembers his early moments in programming, when he made mistakes such as declaring a name of type `int`... thus, the following problem appeared: Let's imagine the political map of the future world, divided into countries whose names are actually non-zero natural numbers. There are certain relationships between them: two countries are allied if they have the same digits in their names (the number of occurrences does not matter), while two countries are in conflict if they have no common digit in their names. Interested in politics, RAU-Gigel would like to know a few things:
- Type $1$ question: how many countries are politically neutral, in the sense that they are not allied with any other country?
- Type $2$ question: for each country in a list of preferred countries, find out: how many countries it is allied with and how many it is in conflict with?

# Task
Help RAU-Gigel find the answer to his two types of questions!

# Input data
The input file `conflicte.in` contains on the first line the type $T$ of the question, with values $1$ or $2$. If $T = 2$, the next line contains a non-zero natural number representing the number $Q$ of preferred countries, then, separated by a space, those countries. On the following lines are the names of the countries on the map, that is, distinct non-zero natural numbers placed two by two, one on each line, or more on a line and separated by a space, in total $N$ numbers.

# Output data
If the question is of type $1$, the output file `conflicte.out` will contain a single line on which there is a single number representing the answer to the type $1$ question. If the question is of type $2$, the output file `conflicte.out` will contain $Q$ rows: on each row $i$ there will be two numbers separated by a space, representing the number of countries allied respectively in conflict with the $i$-th country from the input file.

# Constraints and clarifications
* $1 \leq N \leq 10^5, 1 \leq Q \leq 1 \ 000, Q \leq N$;
* Tests worth $40$ points contain a question of type $1$;
* Tests worth $20$ points contain a question of type $2$ and $N \leq 1 \ 000, Q \leq 10$;
* The names of the countries are non-zero natural numbers, have between $1$ and $9$ digits (inclusive) and do not contain insignificant zeros (on the left);
* The countries on the map are distinct two by two; for questions of type $2$, the list of RAU-Gigel's preferred countries does not contain duplicates and is included in the list of countries on the map;
* All countries that have the same set of digits in their names form an alliance.

# Example 1
`conflicte.in`
```
1
1133 123456789
3131 13
1331 2444
678 42 133
```
`conflicte.out`
```
2
```
## Explanation
For question of type $1$ we have: the countries $1133, 3131, 13, 1331$ and $133$ form an alliance, the countries $2444$ and $42$ form another alliance, while $123456789$ and $678$ are politically neutral.

# Example 2
`conflicte.in`
```
2
2 13 123456789
1133 123456789
3131 13
1331 2444
678 42 133
```
`conflicte.out`
```
4 3
0 0
```
## Explanation
For question of type $2$ we have: the country $13$ is allied with $4$ countries: $1133, 3131$ and $1331, 133$. Country $13$ is in conflict with 3 countries: $2444, 678$ and $42$. The second preferred country of RAU-Gigel, country $123456789$ is not allied with any other country, nor in conflict.
```