Certainly! Here is the translated problem statement:

---

This weekend, tickets for the concert of the most popular artist have just gone on sale. Since this artist is extremely popular, a number of $n$ persons have lined up at the ticket booth. For simplicity, the first person in line will have index $1$, the second will have index $2$, and so on.

Because standing in line is extremely boring, each person started counting how many people shorter than them are in front of them. It is known that the heights of people are represented by positive natural numbers.

Lack of imagination prevented the people in line from finishing the game, so we will do it. Knowing how many people shorter than themselves each person in line has in front of them, we need to determine the height of each person in the sequence.

If there are multiple valid solutions, the minimum lexicographical solution is required. If there are two valid sequences of heights for the $n$ people, $A_1, A_2, ..., A_n$ and $B_1, B_2, ..., B_n$, we say that sequence $A$ is lexicographically smaller than $B$ if there is a natural number $i$ less than or equal to $n$ such that $A_i < B_i$ and $A_j = B_j$ for any $j \in \{1,2,..., i-1\}$.

# Task

Given the initial sequence of observations of the people in line, reconstruct the minimum lexicographical sequence that can represent their heights.

# Input data

In the file `weekend.in`, the first line contains the number $n$. The second line contains a sequence of $n$ natural numbers separated by a space, where the value at position $i$ signifies the number of people strictly shorter than person $i$ and with an index less than $i$.

# Output data

In the file `weekend.out`, the sequence of heights will be printed. On line `i` of the output file, the height of the person with index `i` will be contained.

# Constraints and clarifications

* It is guaranteed that the data set is correct and there will always be at least one solution;
* **Two or more people CANNOT have the same height**;
* $1 \leq N \leq 200\ 000$;
* For 40% of the tests: $N \leq 5\ 000$.

# Example

`weekend.in`
```
4
0 1 1 0
```

`weekend.out`
```
2
4
3
1
```

## Explanation

We can observe that this is the smallest lexicographical sequence that satisfies the observations in the input.

Another solution could have been the sequence `2 5 3 1`, but this is lexicographically larger.