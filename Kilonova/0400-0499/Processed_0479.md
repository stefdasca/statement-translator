At a dance party, there are `N` boys and girls, each having a unique number on their chest between `1` and `N`. They line up in the order of their designated numbers, at a distance of `1` meter from each other. The evening proceeds in rounds of tango. For each round, the organizers choose a continuous subarray (given by the left and right ends) of the `N` dancers to participate in the round and:

* If the number of boys (in the sequence) differs from the number of girls (in the sequence), the round will not be danced;
* If their numbers are identical, then each boy will go to invite a distinct girl to dance. The girls will accept only if the sum of the distances traveled by the boys to the chosen girls is minimal. The tango can begin.

At the end of each round, the dancers resume their places.

The boys, hoping this evening to be special for each (or at least for as many as possible) of them, ask you to determine for each round if it can be danced, and, if affirmative, what the sum of the distances traveled by them (expressed in meters) that will please the girls.

Fortunately, for some tests, the boys managed to come to an agreement with the jury and can tell you in advance which subarrays will be for a few rounds.

# Implementation Details
You will implement two functions with the following headers:
```cpp
void init(std::string s)
std::vector<long long> dance(std::vector<int> l, std::vector<int> r)
```

The string `s` in the `init` procedure is made up of `N` characters from the set `{B, F}`. If $s_k = B$, it is considered that the dancer with number `k + 1` is a boy, and if $s_k = F$, the dancer with number `k + 1` is a girl `(0 \leq k < N)`. The vectors `l` and `r` in the `dance` function have the same size (we will denote it `Q`) and represent the ends of the subarray for each dance round given by the jury in advance at that moment. More precisely, round `i + 1 (0 \leq i < Q)` will be composed of the competitors $[l_i, l_{i + 1}, ..., r_i]$.

**Attention!** For each test, the `init` function will be called only once, at the beginning of the program, then the `dance` function will be called at least once. For each call of the function, it is guaranteed that the lengths of the `l` and `r` vectors are positive and equal $(|l| = |r| = Q)$ and that $1 \leq l_i \leq r_i \leq N$ for any `0 \leq i < Q`.

The `dance` function must return an array of length `Q` of natural numbers between $0$ and $10^{18}$, representing the answers for each of the rounds. In the vector, the answer (expressed in meters) for the dance round characterized by $l_i$ and $r_i$ (`0 \leq i < Q`) will be found on position `i`. If the number of boys in the subarray is different from the number of girls, it is considered that the answer is `0` (since the boys quickly realize this and do not move at all).

# Scoring
`T` represents the total number of rounds within a test (formally, we note $T = \sum Q$, where it will sum up across all calls of the `dance` function).

## Subtask 1 (5 points)
* `1 \leq N \leq 250`
* `1 \leq T \leq 100 000`
* The `dance` function will be called exactly once.
## Subtask 2 (13 points)
* `1 \leq N \leq 2 000`
* `1 \leq T \leq 100 000`
* The `dance` function will be called exactly once.
## Subtask 3 (5 points)
* `1 \leq N \leq 100 000`
* `1 \leq T \leq 20`
* The `dance` function will be called exactly once.
## Subtask 4 (46 points)
* `1 \leq N \leq 100 000`
* `1 \leq T \leq 100 000`
* The `dance` function will be called exactly once.
## Subtask 5 (7 points)
* `1 \leq N \leq 100 000`
* `1 \leq T \leq 100 000`
* The `dance` function will be called at most `T` times.
## Subtask 6 (19 points)
* `1 \leq N \leq 1 000 000`
* `1 \leq T \leq 1 000 000`
* The `dance` function will be called exactly once.
## Subtask 7 (5 points)
* `1 \leq N \leq 1 000 000`
* `1 \leq T \leq 1 000 000`
* The `dance` function will be called at most `T` times.

# Model Grader
Note: The model grader will call the `dance` function only once.
The grader will read from the console the input data in the following format:
* line `1`: `s` (`|s| = N`), representing the initial configuration of the dancers
* line `2`: `Q`, representing the number of dance rounds
* line `3 + i` (`0 \leq i < Q`): $l_i \ r_i$ (separated by space), representing round `i + 1`
The grader will display on the console your response in the following format:
* line `1 + i`: `(0 \leq i < Q)`: answer for round `i + 1`

# Example
`stdin`	
```
BFBFBBFFFBFBBFBF
6
1 2
5 10
6 15
8 12
8 13
1 16
```
`stdout`
```
1
5
9
0
7
10
```
	
Explanation
---
This is a possible way to achieve the third dance round:

~[enunt_Tango.jpg|align=center|width=50%]