# Statement

RAU-Gigel's friends want to surprise him on his birthday! To do this, they need to meet at a single place to organize more efficiently. RAU-Gigel has $N$ friends, labeled with numbers from $1$ to $N$, whose positions can be represented as points on a plane with **positive natural coordinate numbers**, which, for simplicity, are also from $1$ to $N$. They want to meet at a single point with **positive natural coordinate numbers**. For this purpose, each friend can take a step of unit length (relative to a Cartesian frame of reference in which the points could be represented) in any of the $4$ cardinal directions (**North, East, South** or **West**) as many times as they wish. It is considered that the distance traveled by a friend to the meeting place is equal to the number of steps taken to reach the respective destination. After a heated discussion, it was agreed upon a compromise to satisfy everyone: RAU-Gigel's friends will meet at one of the points (not necessarily among the given $N$) that minimizes the sum of the minimum distances from each friend to that chosen point (RAU-Gigel's friends do not like to exercise, so they will always travel the shortest path to the decided meeting point). Since RAU-Gigel's friends have a busier period (with exams, admissions, etc.), they cannot perfectly align their schedules to always meet together, so they organize multiple meetings in which friends from a continuous interval of indices based on the initial numbering will participate. For each such meeting, it is desired to find out (for purely statistical reasons) what the minimum sum of all distances traveled by the friends to the meeting point is, if this point is optimally chosen.

# Task

This challenging computer science problem was too difficult for RAU-Gigel's friends, and since they cannot ask him to solve it (to avoid spoiling the surprise), they ask you, knowing that you are a skilled programmer, to help them as quickly as possible (since the birthday is approaching), rewarding you with as many points as possible in your favorite programming contest if you succeed!

# Input data

The input file `meeting.in` contains:

* The first line contains the number $N$, and the next $N$ lines contain $2$ positive natural numbers $x_i$, $y_i$, representing the coordinates of the point for friend number $i$.
* The next line contains a number $Q$, and the next $Q$ lines contain $2$ positive natural numbers $l_i$, $r_i$, representing an interval of friends who will participate in the meeting number $i$.

# Output data

The output file `meeting.out` will contain:

* On the first $Q$ lines, a number which represents the minimum sum of all distances traveled by the friends from the given interval to the meeting point, if this point is optimally chosen.

# Constraints and clarifications

* **Attention!** The point where the friends meet does not necessarily have to be one of the $N$ points where they are initially located, but it could be! Also, its coordinates must be **positive natural numbers** (obviously, RAU-Gigel's friends cannot reach points that do not have integer coordinates, starting from points with **positive natural coordinates** and taking only steps of length $1$).
* **Attention!** If two or more friends at some point travel through a common path segment (make the same steps from the same points), this contributes individually to each friend's route, thus being added multiple times to the required sum, as it appears in multiple routes.
* For tests worth $5$ points, $1 \leq N, Q < 2^7$
* For other tests worth $10$ points, $1 \leq N, Q < 2^9$
* For other tests worth $10$ points, $1 \leq N, Q < 2^{11}$
* For other tests worth $15$ points, $1 \leq N < 2^{17}$ and $1 \leq Q < 2^8$
* For other tests worth $15$ points, $1 \leq N < 2^{11}$ and $1 \leq Q < 2^{17}$
* For other tests worth $15$ points, $1 \leq N, Q < 2^{15}$
* For other tests worth $15$ points, $1 \leq N, Q < 2^{16}$
* For the remaining tests, there are no additional constraints, meaning only the condition $1 \leq N, Q < 2^{17}$ holds.

# Example

`meeting.in`
```
7
2 3
1 4
5 5
4 3
3 6
1 2
7 4
5
1 7
3 5
4 7
2 6
2 5
```

`meeting.out`
```
19
5
12
13
9
```

# Explanation

For the first query in the example, it can be demonstrated that point $A(3, 4)$ is optimal, minimizing the sum of the minimum distances from the other points to it. If we denote by $D(X, Y)$ the minimum distance between points $X$ and $Y$, then $D(P1, A) = 2, D(P2, A) = 2, D(P3, A) = 3, D(P4, A) = 2, D(P5, A) = 2, D(P6, A) = 4, D(P7, A) = 4$, resulting in a sum of $2 + 2 + 3 + 2 + 2 + 4 + 4 = 19$. For the remaining queries in the example, proceed similarly.

~[meeting.png]