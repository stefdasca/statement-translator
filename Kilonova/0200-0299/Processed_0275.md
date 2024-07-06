You have just received a (very large) rectangular sheet of dimensions `N \times M`, divided into `1 \times 1` squares. Each square is colored on both sides with one of the 26 existing colors in the universe, identified for simplicity by a lowercase English letter.

Having nothing better to do during the competition, you decided to learn *origami*. However, since not everyone is a master of origami and this craft requires experience and artistic vision (things which, of course, you will acquire over time), you have decided that, for a start, it is more interesting to fold the sheet in a clearly established way.

More specifically, at each step, you will choose a line (horizontal or vertical) **located between two consecutive lines (or columns)** and you will "fold" the smaller half over the larger one *only if the colors match perfectly*. An example of such a valid fold is shown below:

\\
~[origami.png]

After any fold, you will obtain a new pattern (obviously, of smaller dimensions). **If both halves are equal, both folding options are valid.**

A master in algorithms and efficient data structures, you immediately notice that after any fold, the resulting pattern will constitute a **submatrix** of the initial pattern. Naturally, the next question comes to your mind:

*"How many distinct submatrices can I obtain by folding the sheet any number of times (or not at all), without rotating the sheet or flipping it to the other side?"*

Formally, two submatrices are considered distinct if at least one of the four corners differs in indices from one submatrix to the other.

# Input data
The file `origami.in` contains on the first line the natural numbers `N` and `M` separated by a space, and on the following `N` lines, there is one string of characters of length `M`, representing the initial configuration of the sheet colors.

# Output data
The file `origami.out` will contain a single positive natural number `X`, representing the number of *distinct submatrices* that can be obtained by applying the operations described in the statement.

# Constraints and clarifications
* For all tests: `1 \leq N \leq M, N * M \leq 1 000 000`
* For `10` points: `M \leq 10`
* For `30` points: `M \leq 40`
* For `50` points: `M \leq 600, X \leq 100 000`
* For `70` points: `M \leq 1 000`
* **For performance reasons, it is recommended to read entire lines, not character by character.**

# Examples
`origami.in`
```
5 7
baabbaa
cbbccbb
ababbab
cabccba
bccaacc
```
`origami.out`
```
2
```

Explanation
---

It is the example from the drawing above. The only possible answers are the initial matrix and the submatrix after applying the operation highlighted in the figure.

`origami.in`
```
3 3
zzz
zzz
zzz
```
`origami.out`
```
36 
```
For this example, any submatrix is valid.