# Sequence 6

Nemroc has defined a sequence as being good if:
- its length is greater than or equal to $2$
- the endpoints are strictly greater than the rest of the elements (e.g., $2 \, 2 \, 3$ is not good, $3 \, 2 \, 3$ is good)

Nemroc gives you an array and asks you to tell him how many subarrays of this array are good.

## Input data

The first line of the input file contains a single natural number $N$, representing the length of the array. The next line will contain $M = \min(N,8192)$ numbers representing an array $x$ and the array that needs to be examined is obtained by applying the following formula $a_i = i + (x_i/8192 \, \operatorname{xor} \, x_i\%8192)$. Both arrays have their first element at index 0.

## Output data

The output file will contain the number requested by Nemroc.

## Constraints and clarifications:

$1 < N < 16\ 000\ 001$

$0 < x_i < 2^{30}$

secv6.in secv6.out 3 3 2 3 2

## Explanation

$0 + (3 \, \operatorname{xor} \, 3) = 0$

$1 + (3 \, \operatorname{xor} \, 2) = 2$

$2 + (3 \, \operatorname{xor} \, 3) = 2$

the array to be examined is $0 \, 2 \, 2$, forming $2$ good sequences $0 \, 2$ and $2 \, 2$