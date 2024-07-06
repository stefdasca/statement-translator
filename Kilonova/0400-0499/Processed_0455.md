# Semarun

Because he is a good athlete and can run consistently at $x$ meters per second, Gigel has set out to win the semarun competition. This competition starts at moment $0$ and consists of completing a route of $n$ meters, which includes $k$ traffic lights.
For each traffic light, the following are known:

- The distance at which it is positioned from the starting point, expressed in meters - $d$;
- The number of seconds it shows the red light - $r$;
- The number of seconds it shows the green light - $v$.

At the beginning of the competition, all traffic lights show red, then alternate between red and green.
Upon encountering a traffic light, participants must wait if it is red or if it changes from green to red, and may pass if it is green or if it changes from red to green. The winner is the one who covers the distance from the starting line to the finish in the shortest time without exceeding $s$ seconds from the start of the competition.

It is important to know that before the start of the competition, each participant must choose the moment (expressed in seconds from the start of the competition) when they will start the route so that they reach the finish in the shortest possible time.

# Task
Because Gigel knows that it is not important to arrive first at the finish but to complete the route in the shortest possible time, he asks for your help with the following task: determine the moments of time that Gigel could choose to start the route so that he does not stop at any traffic light and when he reaches the finish, not more than $s$ seconds have passed since the beginning of the competition (moment $0$).

# Input data
The first line of the input file `semarun.in` contains the natural numbers $n$, $x$, and $s$. The second line contains the natural number $k$, and the next $k$ lines specify for each traffic light the natural numbers $d$, $r$, and $v$.

# Output data
The first line of the output file `semarun.out` will contain the number of solutions for Gigel's task, and the second line will contain the solutions separated by a space, in ascending order.

# Constraints and clarifications
* $1 \leq d \leq n \leq 100 \ 000$;
* $1 \leq x \leq 12$;
* $1 \leq s \leq 864 \ 000$;
* $1 \leq k \leq 70 \ 000$;
* $1 \leq r, v \leq 5$;
* It is guaranteed that the input data provides at least one solution;
* All solutions in the output file must be positive natural numbers.

# Example

`semarun.in`
```
400 10 60
3
30 2 2
60 3 3
90 4 4
```

`semarun.out`
```
3
3 4 11
```

## Explanation

The moments of time that Gigel can choose to meet the task requirements are $3$, $4$, or $11$ seconds from the start of the competition.

If Gigel starts the route after $3$ seconds from the start, he will reach the three traffic lights at seconds $6$, $9$, and $12$, just when they change from red to green. He will finish at second $43$, fitting within the limit of $60$ seconds.

For any other choice apart from the $3$ mentioned above, Gigel would encounter at least one traffic light that would indicate red or change from green to red upon encountering it, or he would not meet the time limit.