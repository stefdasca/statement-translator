Ali Lalap is playing Xmoto on his mobile phone. The goal of the game is to ride a motorcycle through the Gheorgheni circuit. The track consists of `N` segments. The fuel consumption for segment `i (1 \leq i \leq N)` is defined as follows:
$a_i \cdot v + k_i$ liters, if $v \leq v_i$
$b_i \cdot v + q_i$ liters, if $v > v_i$,
where $a_i, b_i, k_i, q_i, v_i$ are constant values, and `v` is the speed at which Ali Lalap travels on that segment.

To avoid overstraining the motorcycle, Ali Lalap prefers to ride at a **constant speed** and wants to know how many possible speed choices exist such that the total fuel consumption is `L` liters.

# Task
Calculate for how many distinct speed values the total consumption will be `L` liters.

# Input data
The input file `xmoto.in` contains the natural numbers `N` and `L` on the first line. The following `N` lines each contain four **real** numbers $a_i, b_i, k_i, q_i$ followed by one **integer** number $v_i$ with the meanings from the statement.

# Output data
The output file `xmoto.out` will contain on the first line a single number `M`, representing the maximum number of speed values for which traveling the entire track results in a total consumption of `L` liters. On the following `M` lines, `M` distinct real numbers will be printed, each with at least `6` **decimal places and sorted in ascending order** $w_1, w_2, ... w_M$, such that if the track is traveled at speed $w_i$ `(1\leqi\leqM)` the total consumption is `L` liters.

# Constraints and clarifications
* `N \leq 50000`
* The real numbers $a_i, b_i$ belong to the interval `[-100, 100]`
* $-1 \ ; 000 \ ; 000 \leq k_i, q_i \leq 1 \ ; 000 \ ; 000$
* `L \leq 100 000 000`
* On each segment, the consumption will be strictly positive for any speed in the interval `(0, 10\ 000]`
* The maximum speed of the motorcycle is `10\ 000` km/h
* The motorcycle runs from start to finish at the same speed (no time is wasted starting from a standstill, there are no accelerations/braking)
* All speeds (maximum speed, speeds $v_i$, the speed that needs to be determined) are expressed in the same unit of measure
* Any solution in which the speeds differ by at most $10^{-6}$ from the correct result is considered correct.
* Verification of total consumption will be done with a precision of $10^{-6}$ relative to `L`.
* It is guaranteed that `M` is finite.
* Determining `M` correctly without accurately calculating the `M` speeds will score `50%` of the points on the test.
* For `10%` of tests `N=1`
* For `25%` of tests $a_i, b_i > 0$
* For `50%` of tests `N \leq 1\ 000`

# Example

`xmoto.in`
```
2 150
3.0 -2.0 2.0 22000.0 60
2.0 4.0 4.0 2.0 50
```
`xmoto.out`
```
1
28.800000
```

# Explanation

`28.8 \leq 60` so the consumption on the first segment is `x = 3*28.8 + 2 = 88.4`
`28.8 \leq 50` so the consumption on the second segment is `y = 2*28.8 + 4 = 61.6`
Total consumption: `x + y = 88.4 + 61.6 = 150