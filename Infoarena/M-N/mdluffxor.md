## Task

MDL uffXor is a free spirit and wants to become the king of the space pirates. Unfortunately, first, he has to do some administrative work. MDL uffXor has to deal with various sequences of treasure chests, which are found in a certain order. Each sequence contains one or more chests, and each chest contains a treasure with a value that is a natural number not exceeding $10^9$. These are built by his enemy, the evil Xoro, to confuse him – however, Xoro never knows the values of the treasures in the chests at any moment. Each sequence of chests is either:
- A single chest, whose value is unknown to Xoro. This value is generated randomly.
- A sequence created by Xoro, whose values are equal to a concatenation of two previous sequences of chests.
- A sequence created by Xoro, whose values are equal to the prefix of a previous sequence of chests.
- A sequence created by Xoro, whose values are equal to the suffix of a previous sequence of chests.

However, it is guaranteed that any sequence will have at most $10^{18}$ chests. At any moment, the evil Xoro can ask MDL uffXor what the value of the $K$-th most valuable treasure (from the most valuable to the least valuable) in a particular sequence is. Xoro does not use this information when constructing subsequent queries.

Given the sequences of chests, find the answers to Xoro's queries.

## Input data

The input file `mdluffxor.in` will contain on the first line a natural number $Q$. The input will be encoded in an unusual way. To decode it, first initialize an integer variable `last` with the value $0$. On the next $Q$ lines, you will find one of the following:
- $1 \ x$, meaning that a sequence containing a single chest, with a value equal to $x$, appears.
- $2 \ x \ y$, meaning that a new sequence, equal to the concatenation of the $(X \ XOR \ last)$-th and $(Y \ XOR \ last)$-th sequences, appears.
- $3 \ x \ l$, meaning that a new sequence, equal to the prefix of length $(l \ XOR \ last)$ of the $(X \ XOR \ last)$-th sequence, appears.
- $4 \ x \ l$, meaning that a new sequence, equal to the suffix of length $(l \ XOR \ last)$ of the $(X \ XOR \ last)$-th sequence, appears.
- $5 \ x \ K$, representing a query by Xoro: "What is the $K$-th (not $K \ XOR \ last$) most valuable treasure in the $(x \ XOR \ last)$-th sequence?” After such a query, if the answer was `ans`, last is updated with the value $(17 * last + ans) \mod 666.013$

The sequences are indexed starting from $1$, in the order in which they appear. It is guaranteed that the input will only refer to sequences that already exist.

## Output data

In the output file `mdluffxor.out`, Xoro's query answers will be printed, in order, on separate lines.

## Constraints

$K \leq 400$

$Q \leq 200,000$

## Example

`mdluffxor.in`
```
8
1 5
1 6
2 1 2
2 3 3
4 3 4
4 5 6
2 5 4
1 5
```

`mdluffxor.out`
```
5
```