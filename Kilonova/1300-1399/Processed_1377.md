```markdown
Bobi is a passionate hiker. The mountainous area he will visit this summer has an attractive feature: there is a cable car transport system. The horizontal projection of Bobi's chosen route is a straight line. Certain points on the mountain, some of which are on the cable car route, are called altitudes. The horizontal projections of the altitudes are $n$ collinear points located one kilometer apart from each other.

~[8ad76cce3bb09b4c1d8c3588a651462f.png|align=left] In the figure, the mountain profile is represented by a solid line, and the cable car route, where it does not coincide with the mountain profile, is represented by a thick dotted line. The cable car follows the segments that connect the altitudes: $[1,2],  [2,3],  [3,6], [6,7], [7,8]$ and $[8,9]$.

Let $h_1, h_2, ..., h_n$ be the heights of the altitudes. The normal speed at which the cable car moves is $v = 1$ Km/hour. The route of the cable car consists of straight segments and generally follows the mountain profile, passing through each altitude. The deviation from the mountain profile occurs when a cable car can be stretched directly between an altitude $i$ and the first altitude $j$, in the direction of travel, which is at a greater height than altitude $i$.

Bobi has $S$ euros. For each segment of the road traveled between two altitudes $i$ and $j$, he must pay $h_j - h_i$ euros if it is an uphill segment and nothing if it is a horizontal segment.

When descending a slope between two altitudes $i$ and $i + 1$, Bobi has two options: the first option is to descend at the normal speed $v = 1$ Km/hour and do not pay anything. The second option, which the boy can choose by pressing a button in the cable car, is to descend the slope, regardless of its length, in one hour, so at a speed different from the normal one, but in this case, Bobi must pay $h_i - h_{i+1}$ euros.

# Task

Knowing the heights of the $n$ altitudes through which the cable car will pass and the amount of money Bobi has, write a program that determines:

1. The total length of the cable car route measured between altitude $1$ and altitude $n$.
2. The minimum time in hours Bobi needs to reach an altitude with an order number **greater than or equal to** $K$, knowing that he starts from altitude $1$ and that there is at least one option that leads to this minimum time and costs a sum less than or equal to $S$.

# Input data

The input file `telecab.in` contains on the first line three natural numbers $n \ K \ S$ separated by a space.

On each of the next $n$ lines contains a natural number. On line $i + 1$ contains the number $h_i$, expressed in kilometers, representing the height of altitude $i \ (i = 1, 2, ..., n)$.

# Output data

The output file `telecab.out` will contain on the first line an integer $L$, representing the total length of the cable car route, between altitudes $1$ and $n$, expressed in kilometers. On the second line will be written the natural number $Tmin$, representing the minimum time Bobi needs to reach an altitude with an order number greater than or equal to $K$.

# Constraints and clarifications

* $3 \leq n \leq 100 \ 000$
* $1 \leq h_1, h_2, ..., h_n \leq 10$
* $1 \leq K, S \leq 1 \ 000$
* The distance between two successive altitudes on the route is calculated as the integer part of the Euclidean distance in the plane between the two altitudes.
* Between two consecutive altitudes, the mountain profile is a straight segment connecting the altitudes.
* For all test cases, it is guaranteed that Bobi has enough money to reach or exceed altitude K.
* For rectilinear movement at constant speed, **distance = speed × time**.
* Solving the first requirement earns $20\\%$ of each test's score.

# Example 1

`telecab.in`
```
9 8 7
4
5
2
2
1
3
5
3
3
```

`telecab.out`
```
12
9
```

## Explanation

The example is the one from the figure. The length of the cable car route is:

$1 + 3 + 3 + 2 + 2 + 1 = 12$

The minimum travel time to altitude $8$ is:

$1 + 1 + 3 + 2 + 2  = 9$

Segment $[1,2]$ is covered in $1$ hour and $1$ euro is spent.

Segment $[2,3]$ is covered in $1$ hour and $3$ euros are spent.

Segment $[3,6]$ is covered in $3$ hours and $1$ euro is spent.

(The distance from altitude $3$ to altitude $6$ is: $\\lfloor \\sqrt{(6 - 3)^2 + (3 - 2)^2} \\rfloor$, and the time is $\\frac{3}{1} = 3$).

Segment $[6,7]$ is covered in $2$ hours and $2$ euros are spent.

Segment $[7,8]$ is covered in $2$ hours and $0$ euros are spent.

# Example 2

`telecab.in`
```
5 3 2
1
2
2
3
1
```

`telecab.out`
```
5
3
```

## Explanation

The length of the cable car route is: $1 + 2 + 2 = 5$

The minimum travel time to altitude $4$ is: $1 + 2 = 3$

Segment $[1,2]$ is covered in $1$ hour and $1$ euro is spent.

Segment $[2,4]$ is covered in $2$ hours and $1$ euro is spent.

It is noted that the cable car _reaches_ altitudes $2$ and $4$, passing _above altitude_ $3$.
```