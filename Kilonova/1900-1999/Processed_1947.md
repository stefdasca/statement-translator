*"In the spring, thawing snow gives rise to rivers and lakes called **Wadi**, lakes that dry up in the summer."* (Wikipedia). This happens in the Atlas Mountains in North Africa. We need to simulate this in the following way:

We have a sequence of numbers, which represent the heights of each place where the water can reach. Each element in the sequence represents the height in meters of a zone with a width of one meter. The zones are contiguous. Water falls from position $0$, from a sufficiently high height, and flows to the right. We call a "unit of water" the amount of water that occupies an area of a $1 \times 1$ square. For example, if a quantity of $4$ units of water melts, it will fall from zone $0$ to the right and will end up occupying the shaded areas. It is observed that if it reaches a certain zone, the water will flow to the right until it hits a vertical wall. We work with the projection in a plane of the imaginary area, so we will consider all elements to have negligible thickness.
~[img1.JPG|align=center|width=auto]

# Task

The configuration of the area is given, and it is required, for several possible amounts of melted water (expressed in "units of water"), to determine the rightmost position that the water reaches and the height it reaches at that position.

# Input data

In the input file `atlas.in` there are multiple tests. The first line of the file contains $T$, the number of tests. Next, there are $4 \times T$ lines. Each test is described by $4$ lines as follows: The first line of the test contains $n$, the number of zones that the water can cross after falling (these are numbered from $1$ to $n$). It is known that the water falls from zone $0$ with infinite height, and to the right is the zone $n+1$, also with infinite height. The second line of the test contains $n$ natural numbers, separated by a space, representing, in order from $1$ to $n$, the heights of the $n$ zones. The third line of the test contains $q$, the number of queries. The fourth line of the test contains $q$ numbers, separated by a space, representing the number of units of melted water.

# Output data

The file `atlas.out` contains one line for each question of each test, in the order of the appearance of the tests and then in the order of the appearance of the queries in each test. Each of these contains two numbers separated by a space representing, in order, the answer to each question. The first number is an integer and represents the rightmost position that the water reaches. The second is a rational number and represents the height at which the water reaches the position given by the first number. This will be displayed in the form of an irreducible fraction `numerator/denominator`.

# Constraints and clarifications

* $ 1 \leq n, q \leq 100 \ 000$;
* $ 0 \leq$ Heights of the pillars $ \leq 100 \ 000$;
* $ 1 \leq$ Values in queries $ \leq 100 \ 000 \times 100 \ 000$;
* $ 1 \leq T \leq 3$;
* In writing the rational number, no space is written before or after the character `/`

# Example

`atlas.in`
```
2
5
0 3 1 4 5
3
4 9 6
3
2 3 1
2
1 2
```

`atlas.out`
```
3 2/1
4 17/4
3 10/3
1 3/1
3 2/1
```
