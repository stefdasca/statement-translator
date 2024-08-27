Mugur

We say that an array \(P\) of round brackets constitutes a correct parenthesization if \(P = Ø\) or \(P = M_1 M_2 \dots M_K\), meaning it is formed by concatenating the subarrays \(M_1, M_2, \dots, M_K\) \((K \geq 1)\). We say that an array \(M\) of round brackets is a bud if \(M = (P)\), meaning it is formed by enclosing a correct parenthesization \(P\) between characters \((\) and \()\). Thus, given a correct parenthesization, one can say how many buds it is composed of. For example, the parenthesization \(S_1 = (())()\) has two buds: \(M_1 = (())\) and \(M_2 = ()\). The array \(S_2 = (()()(()))\) has only one bud: \(M_1 = (()()(()))\).

## Task

Being curious by nature, Amadaeus wonders how many correct parenthesizations with \(K\) buds he can form with \(N\) pairs of parentheses. Since the result can be very large, Amadaeus is satisfied (this time) with the remainder of this number when divided by 123457.

## Input data

The input file `mugur.in` contains a single line with the numbers \(N\) and \(K\).

## Output data

The output file `mugur.out` will contain the required number.

## Constraints

1 \(\leq\) \(K\) \(\leq\) \(N\) \(\leq\) 500

## Example

`mugur.in`
```
4 2
```

`mugur.out`
```
5
```

## Explanation

We have the arrays: \(()(()())\) \(()((()))\) \((())(())\) \(((()))()\) \(()())()\)