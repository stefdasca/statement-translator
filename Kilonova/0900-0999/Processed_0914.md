```markdown
After receiving the project theme from his social studies teacher Simonet, the young Trevor came up with the idea of the game "Pay it forward." For those who do not know this game, it involves Trevor helping people in need. These people, in turn, will help other people, and so on.

Each participant (including Trevor) must perform $k$ good deeds by helping people. The elderly and the young accomplish this task in different ways. The elderly need $\\text{zv}$ days to bring another person into the game, while the young need $\\text{zt}$ days. So if an elderly person or a young person enters the game on day $i$, they will introduce the first person into the game on day $i+\\text{zv}$ for the elderly, respectively on day $i+\\text{zt}$ for the young, the second person on day $i+2*\\text{zv}$ for the elderly, respectively on day $i+2*\\text{zt}$ for the young, and so on. Therefore, the number of people participating in the game can vary depending on how elderly and young people are chosen. Trevor wants as many good deeds as possible to be performed in the game in total, but each participant should bring into the game at most $(k+1)/2$ young people and at most $(k+1)/2$ elderly people. Participants can bring fewer people of a certain type, but they must not exceed the number of $(k+1)/2$ people of the same type.

# Task

What is the number $\\text{fb}$ of good deeds yet to be completed, after $n$ days, by the people already in the game, so that the total number of expected good deeds (both completed and uncompleted) is maximized?

# Input data

The input file `pif.in` contains:
- the first line contains the natural number $n$,
- the second line contains the number $k$,
- the third line contains the numbers $\\text{zv}$ and $\\text{zt}$ separated by a space.

# Output data

The output file `pif.out` will contain the remainder of the division of $\\text{fb}$, with the meaning from the statement, by $1234567$ ($\\text{fb} \% 1234567$).

# Constraints and clarifications

* $1 \\leq n \\leq 10^6$;
* $1 \\leq k, \\text{zt}, \\text{zv} \\leq n$;
* For tests worth $30$ points $\\text{fb} \\leq 10^6$;
* For tests worth $30$ points $\\text{zv} = \\text{zt} = 1$;
* For tests worth $20$ points $\\text{zv} = \\text{zt} \\neq 1$;
* For tests worth $70$ points $k \\cdot n \\leq 10^6$;

# Example

`pif.in`
```
4
2
1 2
```

`pif.out`
```
7
```

## Explanation

$n=4$, $k=2$, $\\text{zv}=1$, $\\text{zt}=2$.

We have $16$ possible ways to choose elderly and young people.

Of these, only $5$ satisfy the condition that the number of elderly and young people should be at most 1. Of these $5$, only two obtain a maximum number of expected good deeds.

We denote with $T$ Trevor, with $V_n$ the elderly people, and with $T_n$ the young people. One of the $2$ cases with a maximum number of good deeds is as follows:
|Day|People who need to help|People helped|Explanation|
|-|-|-|-|
|$0$|$T$ | -    | $T$ starts the game (enters the game) |
|$1$|$T$ | -    | $T$ does not help anyone (2 days have not passed) |
|$2$|$T$ | $V_1$ | $T$ helps $V_1$ |
|$3$|$T$ | -    | $T$ does not help anyone (4 days have not passed) |
|$3$|$V_1$| $V_2$ | $V_1$ helps $V_2$ |
|$4$|$T$ | $T_1$ | $T$ helps $T_1$ |
|$4$|$V_1$| $T_2$ | $V_1$ helps $T_2$ |
|$4$|$V_2$| $V_3$ | $V_2$ helps $V_3$ |

In the following days:
- $V_2$ should help another young person.
- $V_3$ should help two more people, one young person and one elderly.
- $T_1$ should help two more people, one young person and one elderly.
- $T_2$ should help two more people, one young person and one elderly.

So, there are $7$ good deeds left to be accomplished.\
Another case with a maximum number of good deeds is as follows:
|Day|People who need to help|People helped|Explanation|
|-|-|-|-|
|$0$|$T$ | -    | $T$ starts the game (enters the game) |
|$1$|$T$ | -    | $T$ does not help anyone (2 days have not passed) |
|$2$|$T$ | $V_1$ | $T$ helps $V_1$ |
|$3$|$T$ | -    | $T$ does not help anyone (4 days have not passed) |
|$3$|$V_1$| $V_2$ | $V_1$ helps $V_2$ |
|$4$|$T$ | $T_1$ | $T$ helps $T_1$ |
|$4$|$V_1$ | $T_2$ | $V_1$ helps $T_2$ |
|$4$|$V_2$ | $T_3$ | $V_2$ helps $T_3$ |

In the following days:
- $V_2$ should help another young person.
- $T_1$ should help two more people, one young person and one elderly.
- $T_2$ should help two more people, one young person and one elderly.
- $T_3$ should help two more people, one young person and one elderly.

So, there are $7$ good deeds left to be accomplished.
```