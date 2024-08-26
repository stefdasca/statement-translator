Sobo

Petrica, tired of working on the construction site, wants to do something more suited to his intellectual capabilities. So, he took a box with $N$ rats and started experimenting on them. Among other things, he has extracted the genetic map of each rat, consisting of a binary sequence of length $L$. Among the rats, there is one special one, the smartest of them all, which Gigel, Petrica's friend, wants at any cost. However, Petrica does not want to give up the intelligent rat so easily and puts Gigel to the following test: he gives him the genetic maps of all the rats without telling him which one is special. Gigel is allowed to ask questions like: "What is the value of the intelligent rat's map at position $x$?" but the answer has a price, as Petrica gives him the list of prices for all positions. Therefore, Gigel will have to guess the smart rat based on Petrica's answers, which are in the form: "The intelligent rat's map at position $x$ has the value $y$" where $y$ is $0$ or $1$. Gigel wants to know the minimum cost he pays, considering the worst-case scenario (Petrica will choose the answers so that the cost is as high as possible).

## Task

Gigel will pay considerably (with $100$ points) to the one who will make a program to calculate this cost.

## Input data

The first line in the input file `sobo.in` contains the numbers $N$ and $L$ separated by a space, representing the number of rats and the length of their genetic maps. On the next $N$ lines, there is a string of $L$ bits (not separated by spaces) representing the map of a rat. On the last line, there are $L$ numbers separated by spaces representing the cost of the answer for each position.

## Output data

The first line of the output file `sobo.out` will contain an integer representing the minimum cost in the worst-case scenario for Gigel.

## Constraints and clarifications

$1 \leq N \leq 15$

$1 \leq L \leq 1000$

The costs of the answers are integers in the interval $[1, 11000000]$

There are no rats with identical genetic maps

## Example

`sobo.in`

```
4 3
101
000
011
010
2 6 7
```

`sobo.out`

```
13
```

## Explanation

The minimum cost $13$ (in the worst-case scenario) is obtained as follows: Gigel asks what is the value of the intelligent rat's map at position $2$ and Petrica answers $1$, this being the worst-case scenario (if Petrica's answer had been $0$, Gigel would have asked about the value at position $1$ and the rat would have been identified with a cost of $6 + 2 = 8$). Thus, none of the first two rats is the intelligent one. Gigel still needs to find out which of the last two rats is the intelligent one and asks for information about position $3$ from the intelligent rat's map. Regardless of the answer, the intelligent rat will be discovered.