Here is the translated and processed text according to the specified instructions:

---

The most known measure of a mountain peak is its altitude. Secondary peaks of a tall mountain can have considerable altitudes, but in general, they are not as relevant. For this reason, geographers have introduced a new measure for a peak: **prominence**. A **profile** is a representation of altitudes in successive points, between which we can move left or right.

~[proeminenta.png]

In the drawing, we have the profile of the Făgăraș mountains, on which we demonstrate the following definitions:
1. A **peak** is a point (or a succession of consecutive points with the same altitude), for which the altitudes of the adjacent points on the left and right are strictly lower than the altitude of the peak. For example, Negoiu is a peak (its altitude is $2535m$, the point on the profile to its left has an altitude of $2306m$, and the point on the profile to its right has an altitude of $2030m$). Another example of a peak is Urlea, being represented on the profile by two consecutive points with an altitude of $2473m$, having on the left a point with an altitude of $2160m$, and on the right a point with an altitude of $1511m$.
2. The **deepest valley** between two peaks is the minimum altitude of a point that is between the two peaks. For example, in the drawing, the deepest valley between Negoiu and Moldoveanu is $2030m$.
3. The **prominence** of a peak is the **minimum** difference between its altitude and the **deepest** valley between it and a strictly higher peak. If there is no strictly higher peak, the prominence is the altitude of the peak. For example, to determine the prominence of the peak Gălășescu Mare, we can consider the strictly higher peaks (in order from left to right: Negoiu, Moldoveanu, and Urlea). If we start from Negoiu, the difference between the deepest valley and Gălășescu Mare is $2470 - 2030 = 440m$. If we start from Moldoveanu, the difference between the deepest valley and Gălășescu Mare is $2470 - 2213 = 257m$. If we start from Urlea, the difference between the deepest valley and Gălășescu Mare is $2470 - 2160 = 310m$. The minimum difference is $257m$, so the prominence of the peak Gălășescu Mare is given by the peak Moldoveanu.

# Task

Write a program that, knowing the configuration of a profile, solves the following two tasks:

1. Determine the number of peaks existing on the profile;
2. Determine the prominence of each peak on the profile.

# Input data

The input file `proeminenta.in` contains the following information:
- The first line contains the natural number $C$, representing the task that needs to be solved: $1$ or $2$.
- The second line contains the natural number $N$, representing the number of points in the profile.
- The third line contains $N$ natural numbers separated by a space $a_1, a_2, \ldots, a_N$, representing the altitudes of the $N$ points on the profile, in order from left to right.

# Output data

The output file `proeminenta.out` will contain a single line with the answer to the task $C$. If $C = 1$ the answer will be the natural number $Nr$, representing the number of peaks. If $C = 2$ the answer will be a sequence of $Nr$ natural values separated by a single space, representing the prominences of the $Nr$ peaks, in the order from the input file.

# Constraints and clarifications

* $3 \leq N \leq 10^6$;
* $0 \leq a_i < 2^{31}$, for $1 \leq i \leq N$;
* $a_1 < a_2$ and $a_{N-1} > a_N$;

| # | Points | Constraints |
| - | ------ | ------------ |
| 1 | 10     | $C = 1$ |
| 2 | 30     | $C = 2$ and $N \leq 1000$ |
| 3 | 20     | $C = 2$ and the altitudes $a_i$ are distinct two by two |
| 4 | 40     | No other constraints |

# Example 1

`proeminenta.in`
```
1
19
1387 1890 2306 2535 2030 2391 2079 2544 2213 2470 2305 2433 2160 2473 2473 1511 1735 1621 1367
```

`proeminenta.out`
```
7
```

# Example 2

`proeminenta.in`
```
2
19
1387 1890 2306 2535 2030 2391 2079 2544 2213 2470 2305 2433 2160 2473 2473 1511 1735 1621 1367
```

`proeminenta.out`
```
505 312 2544 257 128 313 224
```

## Explanation

The profile from the input files is the one represented in the drawing. The 7 peaks are named in the drawing. Although the altitudes appear in the table on multiple lines, they will be written on a single line in the input file.

---

I've preserved the mathematical values, variable names, general syntax, structure, and format as requested. This includes maintaining the custom image format exactly as is and adhering to the specified translations for certain terms and expressions.