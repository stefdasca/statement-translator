# Por Costel and the Game

One day, Por Costel was bored, sitting alone in his garden and eating corn. So he decided to call his best friend, Por Cătălin. Not being a sporty type, Por Cătălin asked Por Costel to find a game that did not require movement, allowing him to continue eating. Por Costel, the smartest of the pigs, took an empty box from FCK and put $N$ notes in it, each with a number on it. Then he proposed the following game to his friend: “You (Por Cătălin) pick a note from the box, look at it, and put it back, then I (Por Costel) will do the same. If the numbers on our notes are **coprime**, you win, otherwise, I win.” Por Cătălin, being a bit paranoid and cunning, suspected that the chance to win was usually lower, so he asked Por Costel what the probability of him (Por Cătălin) winning was. The notes, being torn by the hoof, had different sizes, hence different probabilities of being chosen. Now Por Costel says to you: “Por Cătălin doesn't know how to calculate, I am in the garden. You calculate it!”.

## Task

Knowing the number $N$ of notes, as well as the pairs of values $(V_i, P_i)$ (value and size) for each note, calculate the probability of Por Cătălin winning (in the form of an irreducible fraction).

## Input data

The input file `porcjoc.in` will contain on the first line the natural number $N$, and on the next $N$ lines, pairs of non-zero natural numbers $(V_i, P_i)$ representing the number written on the $i$-th note and its size (thus, the probability that the $i$-th note will be chosen will be equal to $P_i/S$, where $S$ is the sum of the sizes of the $N$ notes).

## Output data

The output file `porcjoc.out` will have the format “$A/B$”, where $A$ and $B$ are natural numbers **coprime**.

## Constraints

 $1 \leq N \leq 100,000$

 $1 \leq V_i \leq 500,000$ 

 $1 \leq P_i \leq 10,000$

 For $30\%$ of the tests, $N \leq 5,000$

## Example

`porcjoc.in`
```
3
1 25
4 25
8 25
```

`porcjoc.out`
```
5/9
```

## Explanation

The possible selections of notes are as follows: $(1,1)$, $(1,4)$, $(1,8)$, $(4,1)$, $(4,4)$, $(4,8)$, $(8,1)$, $(8,4)$, $(8,8)$. All have equal probability, namely (the bold ones are the games where Por Cătălin wins). So his probability of winning is: $5/9$.