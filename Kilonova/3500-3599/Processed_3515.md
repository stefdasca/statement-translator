
# Task

Ioana the Ant is on the OX axis. She wants to collect as much cheese as possible, so she will be moving for $N$ seconds. At second $i$, she will choose $a_i \neq 0$, an integer, and will move by a distance of $a_i$ meters to the right if $a_i > 0$ and by $-a_i$ meters to the left if $a_i < 0$. She always starts from the origin, and after the $N$ moves, she arrives back at the origin. 

Teodor the Bug, jealous because Ioana has more cheese than him, wonders how Ioana moved. Ioana tells Teodor only $N$, the number of seconds, and $K$, the total distance she traveled, but she does not tell him the numbers $a_i$. Now Teodor wants to find out in how many ways he can choose the sequence $a_i$. He is not good at counting, but he will ask you to help him. In return, he will reward you with 100g of cheese. 

Attention! Ioana can be cunning and might tell Teodor two numbers $N$ and $K$ for which the sequence $a_i$ does not exist. If you do not know how to answer Teodor's question, but you know how to tell him if Ioana is lying, he will reward you with 50g of cheese.

# Input data

The first line of the input will contain two integers $N$ and $K$.

# Output data

The first line of the output will contain the answer to Teodor's question, modulo $10^9+7$.

To only answer the second question: print 0 if Ioana is lying or a number different from 0 if Ioana is telling the truth.

# Constraints and clarifications

* $ 1 \leq N, K \leq 10^6$;
* If you do not know how to answer Teodor's main question, but you know how to tell if Ioana is lying, you will receive 50% of the score for the group.

|#| Score |        Constraints                                    | 
|-|---------|------------------------------------------------------|
|0|   0     | Examples                                              |
|1|   10    | $N, K \le 10$                                        |
|2|   12    | $N, K \le 100$                                       |
|3|   36    | $N, K \le 1000$                                      |
|4|   42    | no additional constraints                             |

# Example 1

`stdin`
```
2 4
```

`stdout`
```
2
```

## Explanation

Ioana can choose the sequence $a_i$ in two ways: $\{ -2, 2 \}$, $\{ 2, -2 \}$.

# Example 2

`stdin`
```
3 4
```

`stdout`
```
6
```

## Explanation

Ioana can choose the sequence $a_i$ in 6 ways: 
- $\{ -1, -1, +2 \}$;
- $\{ -1, +2, -1 \}$;
- $\{ +2, -1, -1 \}$;
- $\{ +1, +1, -2 \}$;
- $\{ +1, -2, +1 \}$;
- $\{ -2, +1, +1 \}$.

# Example 3

`stdin`
```
2 3
```

`stdout`
```
0
```

## Explanation

Teodor realizes that Ioana has lied to him.
