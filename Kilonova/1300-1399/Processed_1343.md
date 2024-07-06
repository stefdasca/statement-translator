~[marathon.png|align=right]
For organizing the mail carriers' marathon event, the organizers have placed $n + 2$ traffic lights along the route, at equal distances from one another. The first traffic light is placed at the starting line, and the last one is placed at the finish line, both of which will have a green light on from the start to the end of the race. For each traffic light encountered along the route, its three colors - red, yellow, and green - light up successively as follows: **always after red comes yellow, after yellow comes green, and after green comes red**, and so on. The red light of each traffic light changes to yellow after $5$ seconds, yellow changes to green after $3$ seconds, and green changes to red after $2$ seconds.
At the moment of the start and when the timer begins, all $n$ traffic lights along the route turn on. Some will have the red color, others yellow, and others green; they are not synchronized at this moment.
Each mail carrier enlisted in the marathon must cover the route from the starting line to the finish line and pass through each of the $n$ traffic lights, but only when each one is green. If a competitor arrives at a traffic light and it is green, they must proceed further. If they reach a traffic light exactly **at the second it changes color**, the competitor **can proceed further only if this change is from yellow to green**, not from green to red or from red to yellow.

# Task

Knowing that the mail carrier Andrei takes $k$ seconds to cover the distance between two successive traffic lights, write a program to determine the minimum number of seconds required for him to cross the finish line.

# Input data

From the input file `marathon.in`:
* The first line contains two natural numbers $n$ and $k$ separated by a space. The value $n$ represents the number of traffic lights placed between the start and finish lines, and the number $k$ represents the time required, expressed in seconds, to cover the distance between any two successive traffic lights on the route.
* The next line contains $n$ integer values separated by spaces, representing the color each traffic light has at the start moment. **We will encode the red color with** $-2$, **yellow with** $-1$, **and green with** $0$.

# Output data

The output file `marathon.out` will contain a single line that will print the natural number $s$, which represents the minimum number of seconds required for Andrei to cross the finish line.

# Constraints and clarifications

* $1 \leq n \leq 5 \ 000$
* $1 \leq k \leq 600$
* The finish line is placed immediately after the last traffic light.

# Example

`marathon.in`
```
3 2
0 0 -1
```

`marathon.out`
```
25
```

## Explanation

The start is given and after $2$ seconds, the mail carrier reaches the first traffic light. At this moment, it changes from green to red, so the mail carrier cannot pass. He waits $8$ seconds, it turns green, and after another $2$ seconds, he reaches the second traffic light (a total of $12$ seconds from the start). Here he waits another $8$ seconds, it turns green, and he can proceed. He covers the distance to the third traffic light in $2$ seconds. When he reaches this traffic light (after $22$ seconds from the start), he waits for $1$ second, it turns green, and after $2$ seconds, he crosses the finish line ($22 + 1 + 2 = 25$ seconds).