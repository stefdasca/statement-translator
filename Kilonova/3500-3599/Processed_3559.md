
# Task

Bogdan has a sequence of non-zero natural numbers written on a sheet of paper, called $A$. He thought about transforming the sequence as follows:

1. First, he divides all elements of the sequence $A$ into $3$ disjoint subsequences that he denotes as $X$, $Y$, $Z$ ($X$ is the subsequence with the elements from the beginning, $Z$ the one with elements from the end, and $Y$ the one with the remaining elements in between; each of the $3$ subsequences must have at least one element). This partition is done such that the length of the subsequence $Y$ is at most equal to half of the length of the given sequence $A$.
2. He removes the subsequence $Y$ from the sequence. Then, in this step, the subsequences $X$ and $Z$ are concatenated, in this order, forming a new sequence.
3. He places the subsequence $Y$ onto the new sequence at a chosen position such that all elements of the subsequence $Y$ can be placed one by one, consecutively, over elements of the remaining sequence, starting from the chosen position.
4. The values of the elements over which elements of the placed subsequence overlap are **added** with the corresponding element from the subsequence. Thus, a new sequence $B$ is obtained.

An example of transformation is:

Bogdan's sequence $A$: $\boxed{1, 2, 3, 4} \boxed{1, 2, 3, 3, 1} \boxed{2, 3, 4, 5}$.

Step $1$: He chooses to form the subsequences as follows: $X$ with the first $4$ elements $(1, 2, 3, 4)$, $Y$ with the elements from positions $5$ to $9 \ (1, 2, 3, 3, 1)$ and $Z$ with the elements from positions $10$ to $13 \ (2, 3, 4, 5)$.

Step $2$: after removing the subsequence $Y$, we obtain: $1, 2, 3, 4, 2, 3, 4, 5$.

Step $3$: He applies the extracted subsequence starting at position $3$ (for example, he could not apply the subsequence on positions greater than or equal to 5 because it could not overlap with all elements over the remaining sequence):
```
    1 2 3 3 1
1 2 3 4 2 3 4 5
```

Step 4: The sequence $B$ becomes: $1, 2, \textbf{4, 6, 5, 6, 5}, 5$.

Bogdan explains his transformation rule to Cosmin and proposes the following game: he shows pairs of sequences $A$ and $B$, and for each pair, he asks: can you decide if the given sequence $B$ can indeed be obtained from the given sequence $A$ by applying the described rule exactly once? If this is possible, the task is to identify the way to obtain it.

# Input data

The file `prieteni.in` contains on the first line a number $t$ representing the number of pairs of sequences that Bogdan gives as a test to Cosmin. Next, the $t$ pairs of sequences are described, each on $4$ lines.
The first line of a group contains the value $n$ representing the number of elements in the sequence $A$. The second line contains the $n$ elements of the sequence $A$, in order of positions from $1$ to $n$. The third line contains a value $m$ representing the number of elements in the sequence $B$. The fourth line contains the elements of the sequence $B$ in order of positions from $1$ to $m$. The elements on the same line are provided separated by a space.

# Output data

The file `prieteni.out` contains $t$ lines, each containing the result of verifying a given pair of sequences $A$ and $B$, in the order they appear in the input. If the sequence $B$ cannot be obtained from the sequence $A$, the line will contain only the value $0$. Otherwise, the line will contain $4$ values, separated by a space, as follows: `1 P L I`. The value $1$ represents the success code ($B$ can be obtained from $A$). $P$ represents the position in $A$ from where the subsequence is extracted. $L$ represents the length of the extracted subsequence. $I$ represents the position where the application of the subsequence starts in $B$. If there are multiple variants, the one with the minimum $I$ is displayed, and if there are still multiple variants, the one with the minimum $P$ is chosen.

# Constraints and clarifications

* $1 \leq t \leq 10$;
* $3 \leq n \leq 2 \ 000$;
* $1 \leq m \leq 2 \ 000$;
* The elements of the given sequences are natural, non-zero, and at most equal to $100$;
* For $17$ points, it is guaranteed that all pairs in the input file for which $B$ can be obtained from $A$ have the property that the extracted subsequence $Y$ is applied at the same position from which it was extracted.
* For $31$ points, it is guaranteed that all pairs in the input file for which $B$ can be obtained from $A$ have the property that the extracted subsequence $Y$ is formed of a single element.

# Example

`prieteni.in`
```
2
13
1 2 3 4 1 2 3 3 1 2 3 4 5
8
1 2 4 6 5 6 5 5
12
1 2 3 4 1 2 3 3 1 2 3 4
7
1 2 4 6 5 6 3
```

`prieteni.out`
```
1 5 5 3
0
```
