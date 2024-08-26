## Task

Stannis Baratheon is trying to conquer King's Landing. He attacks through the city's port and has $N$ boats lined up in an Indian file (the first one is closest to the port, then the second is behind the first, and so on). Each boat has its specific attack power, but this power decreases according to the boat's distance from the port. If the powers of the boats are seen as an array of integers, for example, $V = [3, 4, 2, 1, 5]$, then the first will hit with a power of $\left\lfloor \dfrac{3}{1} \right\rfloor$, the second with a power of $\left\lfloor \dfrac{4}{2} \right\rfloor = 2$, the third with a power of $\left\lfloor \dfrac{2}{3} \right\rfloor = 0$, the fourth with a power of $\left\lfloor \dfrac{1}{4} \right\rfloor = 0$ and the fifth with a power of $\left\lfloor \dfrac{5}{5} \right\rfloor = 1$, where $\left\lfloor x \right\rfloor$ is the floor of the number $x$. Therefore, the sum of all the hits by the boats is $\dots$ Stannis is about to start the battle, but realizes that he can increase the sum of the hits by reorganizing the boats. However, being in a hurry, he can only circularly permute the array of boats, for example $[3, 4, 2, 1, 5]$ circularly permuted to the left 2 times will result in $[2, 1, 5, 3, 4]$. What is the maximum sum of the hits if you can circularly permute to the left as many times as you want (including 0 times)?

## Input data

The input file `blackwater.in` will contain on the first line a natural number $N$. The second line will contain the $n$ integers that form the array $V$.

## Output data

The output file `blackwater.out` will contain on the first line a single natural number, the maximum sum of the powers of the boats after permutations.

## Constraints

$1 \leq n \leq 80\,000$

$0 \leq v[i] \leq 100\,000$

For 11 points it is ensured that $1 \leq n \leq 5000$

For 10 points it is ensured that $1 \leq k \leq 5000$ where $k$ is the number of non-zero elements

For another 16 points it is ensured that the values of the elements will be only $0$ or $100\,000$

## Example

`blackwater.in`

    5
    3 4 2 1 5

`blackwater.out`

    7

`blackwater.in`

    3
    100000 0 100000

`blackwater.out`

    150000

## Explanation

$[3, 4, 2, 1, 5]$ permuted to the left 4 times will result in $[5, 3, 4, 2, 1] \rightarrow \left\lfloor \dfrac{5}{1} \right\rfloor + \left\lfloor \dfrac{3}{2} \right\rfloor + \left\lfloor \dfrac{4}{3} \right\rfloor + \left\lfloor \dfrac{2}{4} \right\rfloor + \left\lfloor \dfrac{1}{5} \right\rfloor = 5 + 1 + 1 + 0 + 0 = 7$

$[100000, 0, 100000]$ permuted to the left 2 times will result in $[100000, 100000, 0] \rightarrow \left\lfloor \dfrac{100000}{1} \right\rfloor + \left\lfloor \dfrac{100000}{2} \right\rfloor + \left\lfloor \dfrac{0}{3} \right\rfloor = 100000 + 50000 + 0 = 150000$