The DFG terrorist group is threatening the peace in Iași. The Secret Services of Iași (SSI) have found out that the group consists of `N` terrorists, numbered from `1` to `N`.

The fighter V Power wants to neutralize each terrorist to restore the safety of the city. V Power knows that there are `K` constraints given as pairs in the form `(x, y)`, meaning that the terrorist `y` can only be eliminated after the terrorist `x` has been eliminated (otherwise, they cannot be located even by SSI).

Before setting off, V Power wants to know in how many ways she can neutralize all the terrorists using advanced taekwondo techniques. In other words, you are asked to determine the number of ways modulo `R` to eliminate all the terrorists, according to the `K` constraints. A way to eliminate all the terrorists means choosing the order in which they are eliminated.

# Input data
The first line of the file `teroristi.in` contains three natural numbers: `N, K, R` separated by a space, having the significance described above.
Each of the next `K` lines contains two natural numbers `x y`, separated by a space, having the meanings described above.

# Output data
The first line of the file `teroristi.out` will contain a natural number `Z` representing the number of ways modulo `R` in which the group can be neutralized.

# Constraints and clarifications
* `N \leq 100`
* `K \leq 100`
* `1 \leq x, y \leq N`
* In the `K` constraints, at most `20` terrorists will be mentioned.
* `R` is prime, $R < 10^9$
* It is guaranteed that there is at least one way to eliminate the terrorists.

# Example:
`teroristi.in`
```
4 3 666013
1 2
4 3
1 3
```
`teroristi.out`
```
5
```
Explanations
---
The `5` ways are:
```
1 4 2 3
4 1 2 3
1 4 3 2
4 1 3 2
1 2 4 3
```