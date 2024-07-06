Below is the translation of the given competitive programming problem statement from Romanian to English, following the specified instructions:

---

Before the Easter holiday, gifts were received at school for the fifth-grade students. There are $N$ boxes of candies, and the number of candies in each box is known. **The number of boxes of candies received by each child must be the same and this number must be greater than or equal to $2$**. The boxes of candies will be given in the order they were received: the first boxes to the first child, the next boxes to the second child, the next boxes to the third child, and so on. 

The goal is to distribute the boxes of candies to as many children as possible. Additionally, there is one more condition: to distribute all the boxes to the children, or at most one box may remain undistributed. If the decision is made that one box is not to be given to the children, it is kept by the headteacher to serve them upon returning to school, and the remaining boxes of candies are placed on the teacher's desk in the order they were received, without the students knowing about the held-back box.

This box selection should be made so that **the total number of candies distributed is as large as possible**.

# Task

1. What is the maximum number of children who will receive gifts?
2. What is the maximum possible number of candies that can be received by a child under the described conditions?

# Input data

The input file `cadouri.in` contains on the first line a number $C$, indicating the task. The second line contains a number $N$ representing the number of boxes of candies received at school. The third line contains $N$ numbers, separated by a space, representing the number of candies in each box, in the order they were received.

# Output data

The output file `cadouri.out` contains two natural numbers, separated by a single space, with the following meaning: for $C = 1$ the first value is the maximum number of children who receive gifts and the second is the number of candies in the held-back box; for $C = 2$ the first value is the maximum number of candies received by a child and the second represents the number of candies in the held-back box. If no box is held back, the second value in the output file will be $0$ (both for task $1$ and for task $2$).

# Constraints and clarifications

* $2 \leq N \leq 100 \ 000$;
* The numbers on the third line are natural, non-zero, and consist of at most $9$ digits.
* For $23$ points, $C = 1$;
* For $77$ points, $C = 2$.

# Example 1

`cadouri.in`
```
1
5
2 7 4 1 2
```

`cadouri.out`
```
2 1
```

## Explanation

Task $1$ is solved. Two children receive gifts. The box with one candy is not given to any child.

# Example 2

`cadouri.in`
```
2
5
2 7 4 1 2
```

`cadouri.out`
```
9 1
```

## Explanation

Task $2$ is solved. Two children receive gifts; the first child receives the boxes with $2$ and $7$ candies, and the second child receives the boxes with $4$ and $2$ candies. Thus, the first child receives the maximum number of candies, $9$. The box with one candy is not given to any child.

---

Please review and verify that the translation maintains all specified formatting and preserves the problem's integrity.