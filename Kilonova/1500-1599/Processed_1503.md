Vlad has invented a new game. The game involves $N$ stands arranged in a straight line. Each stand has a label featuring a natural number. The label is considered correct if the number meets the following two conditions:

1. It contains as many even digits as odd digits;
2. It starts with odd digits in ascending order, followed by even digits in descending order.

For example, the label $137860$ is correct, but the labels $23541$, $135$, $64$, and $3146$ are not correct.
For his game, Vlad built a repair robot that can verify numbers and repair them if necessary. The repair robot moves in a straight line and stops at each of the $N$ stands in sequence. At each stand, the robot checks the label and, if it is not correct, it "repairs" it. To repair a label, the robot arranges the odd digits in ascending order, then the even digits in descending order; if the label contains no odd digits, the largest even digit is replaced with $9$; if the label contains no even digits, the smallest odd digit is replaced with $0$. Moving from one stand to another takes $t$ seconds, verifying the label of a stand takes $v$ seconds, and repairing it takes $r$ seconds. The robot's journey ends after it has checked all $N$ stands and repaired the incorrect labels.

# Task

Write a program that reads the number $N$ of stands, the time (hour $h$, minute $m$, second $s$) when the robot reaches the first stand, times $t$, $v$, and $r$ with the meanings from the statement, and the labels of the stands, and that solves the following tasks:
1. Calculate and print the time (hour, minute, and second) when the robot finishes verifying all $N$ stands and repairing the incorrect labels;
2. Repair (where necessary) the labels of the stands and print the labels of the $N$ stands at the end.

# Input data

The input file `robot.in` contains on the first line a natural number $C$, representing the task to be solved ($1$ or $2$). On the second line, there are natural numbers $N$, $h$, $m$, $s$, and on the third line, natural numbers $t$, $v$, $r$, with the meanings from the statement. The numbers on the same line are separated by a space. On the following $N$ lines are the labels of the stands, in the order they are arranged, one label per line.

# Output data

If $C = 1$, the output file `robot.out` will contain a single line with $3$ natural numbers separated by a space $hf \ mf \ sf$, representing the hour, minute, and second when the robot finishes repairing.

If $C = 2$, the output file `robot.out` will contain $N$ lines with the labels of the stands, in the order they are arranged, after the robot has completed verification and repair, one label per line.

# Constraints and clarifications

* $2 \leq N \leq 500$
* Labels of the stands have at least two and at most nine digits.
* The robot starts and completes the repair on the same day.
* $0 \leq h, hf < 24$
* $0 \leq m, mf, s, sf < 60$
* Correct resolution of task $1$ is worth $40$ points.
* Correct resolution of task $2$ is worth $60$ points.

# Example 1

`robot.in`
```
1
3 11 20 50
7 5 15
376572
3564
123
```

`robot.out`
```
11 21 49 
```

## Explanation

The task is $1$. There are $3$ stands. For simplicity, we note the time as $h:m:s$ hour $h$, $m$ minutes, and $s$ seconds. The robot reaches the first stand at $11:20:50$. The first stand has the label $376572$, which is incorrect, so the robot repairs it. Here, it spends $5$ seconds for checking and $15$ seconds for repairing, so it leaves at $11:21:10$. The robot reaches the second stand at $11:21:17$; its label $3564$ is correct, so the robot does not modify it; it spends $5$ seconds checking and leaves at $11:21:22$. The robot reaches the third stand at $11:21:29$. The third stand has the incorrect label $123$, the robot repairs it, so it spends $5 + 15 = 20$ seconds, and the time it ends its journey is $11:21:49$.

# Example 2

`robot.in`
```
2
3 11 20 50
7 5 15
376572
3564
113
```

`robot.out`
```
357762
3564
130
```

## Explanation

The task is $2$. There are $3$ stands.
The first stand has the incorrect label $376572$, the robot repairs it, and it becomes $357762$.
The second stand's label $3564$ is correct, so the robot does not modify it.
The third stand has the incorrect label $113$, the robot repairs it and it becomes $130$.