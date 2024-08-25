## Subarrays

While Antonio is searching for tulips, we present another problem. Marinica has at his disposal two natural numbers with $N$ digits and $M$ digits, respectively. He wants to find out how many distinct subarrays of the first number (which do not start with the digit $0$) have the property that they are less than or equal to the second number. Help Marinica!

## Input data

The input file `subsecvente.in` will contain two lines, the first line contains the first number, and the second line contains the second number.

## Output data

The output file `subsecvente.out` must contain a single number: how many distinct subarrays of the first number (which do not start with the digit $0$) are less than or equal to the second number.

## Constraints and clarifications

$1 \leq N \leq 1\, 000\, 000$  
$1 \leq M \leq N$  

Attention! In a subarray, all digits that appear are in consecutive positions in the initial number. Any subarray can be characterized by 2 indices $i$ and $j$, with $i \leq j$, with the property that both the element at position $i$ and the one at position $j$ exist, and the subarray starts at position $i$ and ends at position $j$. Two subarrays are considered distinct if their index pairs differ: $(i_1, j_1) \neq (i_2, j_2)$

## Example

`subsecvente.in`   
```
2057
21
```

`subsecvente.out`   
```
4
```

## Explanation

The subarrays of the number `2057` are: `2, 0, 5, 7, 20, 05, 57, 205, 057, 2057`, among which only the following are less than or equal to `21` (excluding those that start with the digit $0$): `2, 5, 7, 20`. Obviously, the other subarrays are not valid because `57, 205, 2057` are strictly greater than `21`.