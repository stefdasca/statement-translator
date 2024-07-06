Popel, a high school student qualified for the National Informatics Team, has just learned the Sieve of Eratosthenes algorithm to find prime numbers, which is described as follows:

```
prim[i]=1, for any i from 2 to N
for i from 2 to N:
    if prim[i] is 1:
        for j from 2*i to N by i:
            prim[j] = 0
```

Due to fatigue and stress, Popel incorrectly initialized the `prim` array, placing `0` instead of `1` at some positions. After running the algorithm on the incorrectly initialized `prim` array, he obtained a new array, which he wrote down on a piece of paper.

Later, he could no longer remember the initial `prim` array, but he still had the final array he obtained. Moreover, he was not sure if he correctly wrote some values in the final array, so he marked them with the character `?`. Popel asks you to find an initial array with the property that if he runs the above algorithm on it, he would obtain an array that matches the final array noted on the paper. Additionally, he wants the initial array to have as many `1`s as possible.

# Input Data
The file `ciurulet.in` contains:
- The first line contains the number `N` representing the value up to which the algorithm will run.
- The next line contains `N-1` characters from the set `{0, 1, ?}`, without spaces between them, representing the array noted on the paper. The character `?` indicates a character that Popel no longer remembers (i.e., Popel does not know whether it was `0` or `1`). The `i`-th character among these represents the value of `prim[i+1]`. If it is different from `?`, then Popel remembers it exactly. Otherwise, it could be anything (`0` or `1`).

# Output Data
The file `ciurulet.out` contains:
- The first line contains the maximum number of `1`s that can appear in an initial array that results in a final array matching the one noted on the paper.
- The second line contains `N-1` characters from the set `{0, 1}`, without spaces between them, representing the initial array used.

# Constraints and clarifications
- `2 \leq N \leq 1\ 000\ 000`
- For `30%` of the tests, the array in the input file does not contain the character `?`.
- For two arrays `A` and `B` to match, `A[i]` and `B[i]` must be equal for any `i` from `2` to `N` with `B[i]` different from `?`. In other words, `0` matches with `0`, `1` matches with `1`, and both `0` and `1` match with `?`.
- It is guaranteed that the final array noted on the paper is a valid one.
- Any array from which the noted array on the paper is obtained after applying the above algorithm and which contains a maximum number of `1`s will be considered correct.
- **The two arrays are indexed starting from position 2**.

# Examples
`ciurulet.in`
```
6
10??0
```

`ciurulet.out`
```
4
10111
```

**Explanation**
---
The transformations through which the array `1011` will go are: `10111 -> 10011 -> 10010`
The array `10010` matches what Popel noted on the paper.

`ciurulet.in`
```
9
??10?00?
```

`ciurulet.out`
```
5
01101011
```

**Explanation**
---
Applying the above algorithm on the array `01101011` finally results in the array `01100000`, which matches what Popel noted on the paper.