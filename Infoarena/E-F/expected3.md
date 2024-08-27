Expected3

After receiving a box with $N$ green balls, $M$ red balls, and a black ball as a Christmas gift, you thought of the following game: at each step, you draw one of the balls from the box with equal probability.
if the ball is green, you will gain $A$ points
if the ball is red, you will lose $B$ points
if the ball is black, the game ends
After you draw a ball, it will not be put back into the box.
What is the expected value of the number of points you will get?
It can be shown that the answer can be written as an irreducible fraction $P/Q$, where $gcd(Q, 1\ 000\ 000\ 007) = 1$. In this case, you need to print the number $P * Q^{-1}$ modulo $1\ 000\ 000\ 007$.

## Input data

The input file `expected3.in` contains a single line with 4 natural numbers $N$, $M$, $A$, $B$, as described above.

## Output data

The output file `expected3.out` will contain a single number of the form $P * Q^{-1}$ modulo $1\ 000\ 000\ 007$, where $Q^{-1}$ represents the modular inverse of $Q$ with respect to $1\ 000\ 000\ 007$.

## Constraints

$1 \leq N, M \leq 100\ 000$
$1 \leq A, B \leq 1\ 000\ 000\ 000$
For 40 points,
$1 \leq N, M \leq 1000$
For another 20 points,
$1 \leq N, M \leq 3000$

## Example

expected3.in
```
1 1 3 1
```

expected3.out
```
5
```

expected3.in
```
3 3 4 5
```

expected3.out
```
500000005
```

expected3.in
```
10000 10000 90000 70000
```

expected3.out
```
100000000
```

## Explanations

For the first example, the balls can be drawn as follows:
$ \text{N (0 points), with a probability of } 1/3$
$ \text{VN (3 points), with a probability of } 1/6$
$ \text{RN (-1 points), with a probability of } 1/6$
$ \text{VRN (2 points), with a probability of } 1/6$
$ \text{RVN (2 points), with a probability of } 1/6$
The expected value is