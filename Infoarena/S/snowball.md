## Task

Brace yourselves, pizza is coming. It is winter and it has just snowed in the Imaginary City. Thus, a layer of snowflakes has formed. Each has its spectacular shape, but although we know very well that "no two snowflakes are alike", we will consider in this problem that there are at most $10\ 000$ types of snowflakes, encoded by natural numbers (from $1$ to $10\ 000$). Otis and Tiţa, the two dogs, have gone outside and are enjoying the snow. Tiţa dug with her nose in a straight line and managed to form a snowball $B$ consisting of a string of snowflakes $b_0, b_1, \dots, b_{M-1}$. Jealous, Otis wants to make a prettier snowball than Tiţa's. Thus, he is in front of a strip of snow $A$, $a_0, a_1, \dots, a_{N-1}$. He can start from any index $i$, with $0 \leq i \leq N-1$, and can form a snowball from the snowflakes in consecutive positions. For unknown reasons, Otis considers his snowball to be prettier than Tiţa's only if it cannot be formed from her snowball. In other words, the snowball $B, b_0, b_1, \dots, b_{M-1}$ must not be found as a subsequence in the sequence chosen by Otis. Otis is curious about how many ways he can build his snowball, but of course, in the end, he will choose the one with the maximum length. Since his only skill is eating, he asks you to give him some of your pizza and also to help him make a snowball prettier than Tiţa's.

## Input data

The input file `snowball.in` contains on the first line two natural numbers $M$ and $N$, meaning the length of Tiţa's snowball and the length of the strip in front of Otis, respectively. On the next line is the string $B$ of $M$ natural numbers, representing Tiţa's snowball, and on the third line, the string $A$ of $N$ natural numbers, representing the strip in front of Otis.

## Output data

The output file `snowball.out` will contain two natural numbers, meaning the maximum length of Otis's snowball and the number of ways to choose to form it, respecting the conditions from the statement. It is guaranteed that there is at least one solution.

## Constraints and clarifications

$1 \leq N \leq 500\ 000$

$1 \leq M \leq 10\ 000$

The strings $A$ and $B$ will contain only natural numbers less than or equal to $10\ 000$.

The string $B$ will not contain two identical elements.

## Example

`snowball.in`

```
3 7 
1 3 2 
1 3 1 2 89 100 55 
```

`snowball.out`

```
6 24
```