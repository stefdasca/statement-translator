```markdown
After failing at the Olympics, Chuck Nirros found solace in the wonderful sandwiches from OverWay. Aware that he is gaining weight, he decided to enroll in sports classes with a qualified coach. The training takes place over the course of $T$ days, with a different number of students $N_i$ present each day. The coach has a unique way of choosing the order in which the students will use the equipment: at the beginning of each day, he will choose a secret non-zero natural number $K_i$, then the students line up in a row and are numbered from left to right starting with $1$, representing the leftmost student, and ending with $N_i$, representing the rightmost student. He then starts counting from left to right, and when he reaches one of the ends, he continues counting starting from that end and going towards the opposite end.

For example, for $N_i=3$, he will count as follows: $1 \ 2 \ 3 \ 3 \ 2 \ 1 \ 1 \ 2 \ 3 \ 3 \ 2 \ 1 \dots$ . At each $K_i$, the student he stops at is completely removed from the row and is allowed to use the training equipment. Unfortunately, Chuck Nirros does not know the secret numbers, but he knows the order in which the students were removed from the row.

# Task

Given the order of the students removed on each of the $T$ days, find the *smallest* possible value that each of the secret numbers $K_i$ can take.

# Input data

The `sport.in` file contains on the first line the number of days $T$. The next $2 \cdot T$ lines contain the order in which the students were eliminated on each of the $T$ days and will have the following configuration:

* line $2 \cdot i$ contains the number of students present at the training in day $i$, denoted by $N_i$.
* line $2 \cdot i+1$ contains $N_i$ natural numbers separated by a space, representing the order in which the students were eliminated on day $i$. Obviously, the numbers on this line are distinct from each other.

# Output data

The `sport.out` file contains $T$ non-zero natural numbers representing the minimum values that each of the secret numbers $K_i$ can take, one per line.

# Constraints and clarifications

* $1 \leq T \leq 1 \ 002$
* $1 \leq N_i \leq 42$
* Attention! The secret numbers are non-zero natural numbers.

# Example

`sport.in`
```
2
2
2 1
6
2 4 6 3 1 5
```

`sport.out`
```
2
2
```

## Explanation

For the first day, another possible answer is $3$, but it is not minimal.

For the second day, the sequence of students will look as follows:

* $1 \ 2 \ 3 \ 4 \ 5 \ 6$ – initially
* $1 \ 3 \ 4 \ 5 \ 6$ – after counting $1 \ 2$
* $1 \ 3 \ 5 \ 6$ – after counting $3 \ 4$
* $1 \ 3 \ 5$ – after counting $5 \ 6$
* $1 \ 5$ – after counting $5 \ 3$
* $5$ – after counting $1 \ 1$
```