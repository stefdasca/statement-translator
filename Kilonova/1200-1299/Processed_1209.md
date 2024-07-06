The National Anonymous High School (LNA) is invited to participate in the Romanian-mathematics Olympiad with a team of $m$ students. In this Olympiad, students work as a team and need to solve two subjects: one in Romanian and one in mathematics. $n$ students, numbered from $1$ to $n$, have been tested and scored in both subjects. As expected, generally, students good at mathematics proved to be somewhat weak in Romanian and vice versa. To maximize the chances of winning for the LNA team, the director decided to send $m$ students out of the $n$ tested students, such that the absolute difference between the sum of the Romanian language scores of the students in the team and the sum of the mathematics scores of the students in the team is minimized. If there are multiple teams of students that meet the previous condition, a team for which the sum of all the scores is maximum will be selected among them.

# Task

Write a program that, in accordance with the director's decision, determines the **absolute difference** between the sum of the Romanian language scores of the students in the LNA team and the sum of the mathematics scores of the students in the team, as well as the **sum** of all the scores of the students in the LNA team.

# Input data

In the input file `materom.in`, the first line contains the natural numbers $n$ and $m$ separated by a space, with the significance from the statement.  
Each of the following $n$ lines contains two natural numbers separated by a space. More precisely, line $i + 1$ in the file contains $m_i$, $r_i$, where $m_i$ is the score obtained in mathematics, and $r_i$ is the score obtained in Romanian by student $i$.

# Output data

The output file `materom.out` contains two lines. The first line contains the absolute difference between the sum of the Romanian language scores of the students in the team and the sum of the mathematics scores of the students in the team. The second line contains the sum of the scores of the students selected in the LNA team.

# Constraints and clarifications

* $1 \leq m < 20$
* $1 \leq n \leq 500$
* $m \leq n$
* $0 \leq m_i, r_i \leq 20$

# Example

`materom.in`
```
4 2
2 3
1 2
6 2
4 1
```

`materom.out`
```
2
10
```

## Explanation

Out of the $4$ students, we need to select $2$. We have $6$ possibilities, of which $3$ have the absolute difference between the sum of the mathematics scores and the sum of the Romanian scores as $2$.  
These are:
- $(1, 2)$ for which the sum of scores is $8$;
- $(1, 4)$ for which the sum of scores is $10$;
- $(2, 4)$ for which the sum of scores is $8$.

We choose the combination $(1, 4)$ because it has the maximum sum.