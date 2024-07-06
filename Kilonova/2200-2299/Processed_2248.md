```markdown
# Task

Larry, the lazy lizard, has decided to take some very challenging physics courses at school. In this subject, there are no assignments, only tests! Also, being very lazy, he wants to study as little as possible for his tests.

He needs to take $N$ tests in this subject. For each test, you are given two values: $a_i$ and $b_i$. $a_i$ is the score he would receive if he studied, and $b_i$ is the score he would receive if he chose not to study. Note that he can either study or not, there is no intermediate option.

His teacher also has a condition: only the scores of $N - 1$ tests will be summed to get the final score! The teacher will randomly eliminate one test from the total score but will inform Larry which test will be eliminated before he takes all the tests.

Remember that the total score is calculated by summing the scores obtained from all his tests (unlike traditional schooling, the total score here can become very large, not just up to $100$).

Given these conditions, you need to find out the minimum number of tests Larry needs to study for to ensure he will get a score of at least $Q$, regardless of what happens ($Q$ is the threshold for a grade of $10$ in this subject), or print $-1$ if it is not possible, no matter how much he studies. You need to print the answer for each of the potential tests the teacher might eliminate (i.e., you need to print $n$ integer values, where the $i$-th integer represents the minimum number of tests to study for, given that the teacher eliminates the $i$-th test).

# Input data

The first line contains two natural numbers separated by a space, $N$ and $Q$. The next $N$ lines contain two integers each, with the $i$-th line containing two numbers separated by a space, $a_i$ and $b_i$, representing the scores with and without studying for that test.

# Output data

Print $N$ lines, with the $i$-th line containing the minimum number of tests to study for if the teacher eliminates the $i$-th test, to achieve a score of at least $Q$, or $-1$ if this is impossible.

# Constraints and clarifications

* $1 \leq N \leq 10^5$;
* $1 \leq Q \leq 10^8$;
* $1 \leq b_i \leq a_i \leq 10^4$;

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|40|$N \leq 2 \ 000$|
|2|60|No additional constraints|

# Example

`stdin`
```
3 5
5 0
3 2
2 1
```

`stdout`
```
2
1
1
```
```