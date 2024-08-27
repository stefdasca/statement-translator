## Task

G. Tamplaru' I wants to build a new desk. He knows the final dimensions of all the planks he needs to construct the desk and has bought a plank of length $L$ equal to the sum of the lengths of all the necessary planks. He has a special machine in which he can insert a plank of any length, and it will cut it into a maximum of $M$ pieces. The effort exerted by G. Tamplaru' I to cut a plank of length $X$ is equal to $X$. He does not want to work too hard and asks you to determine the minimum effort needed to cut the large plank into the desired lengths.

## Input data

The input file `scandura.in` will contain on the first line two natural numbers $N$ and $M$. The second line will contain, separated by spaces, $N$ natural numbers in ascending order.

## Output data

The output file `scandura.out` will contain on the first line the minimum effort required.

## Constraints

$1 \leq N \leq 10^6$

$2 \leq M \leq N$

$1 \leq$ lengths of the planks $\leq 2 * 10^9$

The result will always fit within 64-bit signed integer types.

## Example

`scandura.in`

`4 2`

`1 2 3 4`

`scandura.out`

`19`

## Explanation

The initial plank has a length of $10$. G. Tamplaru' I performs a cut with a cost of $10$ and obtains 2 planks with lengths $4$ and $6$. He then cuts the plank of length $6$ into 2 planks of lengths $3$. Finally, one of the 2 planks of length $3$ is cut into a plank of length $1$ and one of length $2$. The total effort is equal to $10 + 6 + 3 = 19$.