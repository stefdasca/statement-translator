Given a list with $n$ words and $q$ operations on this list. The same words can exist multiple times in the list.

The operations are as follows:
* `1 s` - Add the word $s$ to the list.
* `2 s` - Remove an occurrence of the word $s$ from the list. If that word is not in the list, nothing happens.
* `3 s` - Find the number of distinct triplets formed from words in the list that have the word $s$ as a suffix.

# Task
Perform all the operations one by one. Display the answers to the operations of type 3.

# Input data
The first line contains the natural number $n$, and the second line contains the elements of the list described in the problem statement, separated by exactly one space.
The next line contains the natural number $q$, and the following lines contain the operations described in the problem statement.

# Output data
Each line contains the answers to the operations of type 3.

# Constraints and clarifications
- For 20 points, $0 \leq n, q \leq 1\ 000$.
- For another 25 points, $0 \leq n, q \leq 100\ 000$.
- For another 55 points, $0 \leq n, q \leq 1\ 000\ 000$. **For submissions in C++, it is recommended to include this line of code at the beginning of the `main()` function: `cin.tie(0);ios::sync_with_stdio(0);`**.
- **The distinction between triplets is made by the positions of the words in the list, not by the content of the words.**
- Each word in the input data will have at least one character and at most 20 characters. The allowed characters are only the 26 lowercase letters from `a` to `z`.

# Example
`stdin`
```
5
acasa sa sa sa casa
3
2 sa
3 a
3 casa
```
`stdout`
```
4
0
```

# Explanation
- After the operation `2 sa`, one occurrence of the word `sa` was removed from the list. Now, the list consists of the words `acasa`, `sa`, `sa`, `casa`.
- The operation `3 a` will display the number `4`, because the triplets formed from words that have the word `a` as a suffix are `(acasa,sa,sa)`, `(acasa,sa,casa)`, `(acasa,sa,casa)` and `(sa,sa,casa)`. The reason why `(acasa,sa,casa)` was counted twice is because in the first triplet we considered the word `sa` at position `2` in the list, and in the second triplet we considered the word `sa` at position `3` in the list.
- The operation `3 casa` will display the number `0`, because the only words that have the word `casa` as a suffix are the words `acasa` and `casa`, which cannot form a triplet.