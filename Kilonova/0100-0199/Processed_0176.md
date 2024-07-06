In his quest for glory, Lunasorab came across a string of pearls with length `N`, of different types, represented by a lowercase letter of the Latin alphabet. Among these, pearls marked with `*` are considered magical. They can be transformed (and must be transformed) into a non-magical pearl of any type. Now, Lunasorab has received a natural number `L`, and he knows that if he can find a subarray of maximum length in the initial string, formed by the repeated concatenation of a subarray of length `L` of the string with itself, he can sell it on the black market for a considerable sum (Lunasorab does not shy away from using unconventional methods to achieve his goals).

Since Lunasorab is not very good at exact sciences (he has other talents), he is asking for your help.

Also, being naturally more distrustful, Lunasorab requests the answer for multiple strings.

# Task
For each string in the input file, find the longest subarray of the string that can be obtained by concatenating a subarray of length `L`.

# Input data
The input file `sirag.in` will contain on the first line a natural number `T`, representing the number of tests.
The next `2*T` lines will contain the `T` tests, formatted as follows: on the first line corresponding to a test, there will be the natural numbers `N` and `L`, separated by a single space, representing the length of the string, and the length of the subarray used in repetition, respectively. The second line will contain `N` characters, representing the types of the `N` pearls.

# Output data
The output file `sirag.out` will have `T` lines, each line containing a natural number `M`, which represents the length of the longest subarray with the mentioned property for the respective test.

# Constraints and clarifications
* `1 \leq T \leq 10`
* `1 \leq N \leq 100000`
* `1 \leq L \leq N`
* The types of pearls will be represented either by a lowercase letter of the Latin alphabet or by the character `*` for magical pearls
* For `10%` of tests `L = 1`
* For `30%` of tests `N \leq 2000`

# Example

`sirag.in`
```
1
6 3
a*cab*
```

`sirag.out`
```
6
```

Explanation
---

The string can be transformed into `abcabc`, replacing the first magical pearl with `b`, and the second with `c`. Then the sequence `abc` repeats `2` times, and thus a subarray of length `6` (the entire string) can be obtained with the mentioned property.

