## Rabbits

Zaharel has developed a new passion: he wants to have rabbits! Thus, one day (we will call it day $0$), he went to the store and bought $X$ rabbits. It is known that rabbits multiply every day so that on day $1$ he had $Y$ rabbits, and on day $2$ he had $Z$ rabbits. A sharp observer, Zaharel noticed that starting from day $3$, the number of rabbits each day depends on the number of rabbits in the last three days as follows: $A$ times the number of rabbits one day ago, $B$ times the number of rabbits two days ago, and $C$ times the number of rabbits three days ago.

## Task

Determine the remainder when the number of rabbits Zaharel will have on day $N$ is divided by $666013$.

## Input data

The input file `iepuri.in` contains multiple data sets. The first line will contain an integer $T$ representing the number of data sets for which an answer is required. The following $T$ lines will each contain seven integers, in the following order: $X$ $Y$ $Z$ $A$ $B$ $C$ $N$.

## Output data

The output file `iepuri.out` will contain $T$ lines, each containing a single integer representing the answer for a data set. The answer on line $i$ must correspond to the data set on line $i+1$ from the input file.

## Constraints and clarifications

$0 \leq T \leq 100$

$1 \leq X \leq Y \leq Z \leq 10\ 000$

$1 \leq A$, $B$, $C \leq 1\ 000$

$3 \leq N \leq 2\ 000\ 000\ 000$

Points for a test are awarded only if the correct answers have been given for all data sets.

## Example

`iepuri.in`
```
2
1 1 2 1 1 1 5
1 2 3 1 2 3 4
```

`iepuri.out`
```
13
22
```

## Explanation

First data set:
On day $3$ he will have $1*2+1*1+1*1=4$ rabbits

On day $4$ he will have $1*4+1*2+1*1=7$ rabbits

On day $5$ he will have $1*7+1*4+1*2=13$ rabbits

Second data set:
On day $3$ he will have $1*3+2*2+3*1=10$ rabbits

On day $4$ he will have $1*10+2*3+3*2=22$ rabbits