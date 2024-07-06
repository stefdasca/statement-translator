Given altitudes of `N` points, situated in a straight line along the `Ox` axis, such that they correspond to consecutive natural abscissas. The first point has abscissa `1`. From this point, a laser beam must be sent to the last point (with abscissa `N`). The beam propagates only in a straight line and cannot pass below the given points (but it can pass through them). To "bypass" the points with altitudes that block the beam, relays are mounted at certain points to change the angle at which the beam propagates, so that it can pass over the peaks in its path. Relays will be mounted at any of the given points, except the first point, from where the beam can start at any angle, and the last point where the beam can be received at any angle.

It has been observed that if the relay is mounted on a pillar at certain points, the number of necessary relays can be reduced. All the pillars to be mounted have the same given height `H`.

# Task

Determine the minimum total number of relays (mounted on pillars or not) for the beam to reach from the initial point to the final point, as well as the points where they will be mounted. If there are multiple solutions with the same minimum number of relays, choose the one with the minimum number of pillars.

# Input data

The file `relee.in` contains on the first line the natural numbers `N` - the number of points and `H` - the height of the pillars. The second line will contain, separated by a space, the altitudes $A_i$ of the `N` points.

# Output data

The file `relee.out` will contain the following information on the first line, separated by a space, the number of relays not mounted on pillars, respectively the number of relays mounted on pillars. On the second line, print the abscissas of the points where the relays will be mounted without being placed on pillars. On the third line, print the abscissas of the points where the relays will be mounted on pillars.

# Constraints and clarifications

* For `50` points: `1 \\leq N \\leq 200`, `1 \\leq H \\leq 500`, $1 \\leq A_i \\leq 2 500$, `i = 1, 2, ..., N`
* For other `50` points: `1 \\leq N \\leq 5 000`, `1 \\leq H \\leq 1 000 000 000`, $1 \\leq A_i \\leq 1 000 000 000$, `i = 1, 2, ..., N`
* `50%` of the score will be awarded for printing the number of relays and `50%` for printing a relay placement solution.
* If three peaks are collinear, then a relay **must not** be placed on the middle peak.

# Example

`relee.in`

```
9 2
3 2 6 6 4 3 5 3 2
```

`relee.out`

```
1 1
7
4
```

Two relays are mounted: `1` on a pillar and `1` without a pillar. A relay without a pillar will be mounted at point `7`, and on a pillar at point `4`. Another variant is to put the relay with a pillar at point `3`. If we placed relays at points `3`, `4`, `7`, we could avoid using any pillars but would use `3` relays instead of `2`.

The example corresponds to the following figure:

~[relee.png]