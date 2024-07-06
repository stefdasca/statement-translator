A bijective function $p: \\{1, 2, ..., N\\} \\rarr \\{1, 2, ..., N\\}$ is called a *permutation of length $N$*. On the set of permutations of length $N$ (denoted by $S_N$), we define the **composition** operation $\circ$ as follows: $p \\circ q: \\{1, 2, ..., N\\} \\rarr \\{1, 2, ..., N\\} $, $(p \\circ q)(i) = p(q(i))$. We can define inductively $p_1 \\circ p_2 \\circ ... \\circ p_k = (((p_1 \\circ p_2) \\circ p_3) \\circ ... \\circ p_k)$. We call a *generating subgroup* of the set $S_N$ any subset $\\{p_1, p_2, ..., p_k\\} \subseteq S_N$ which satisfies the property that any permutation $X$ from $S_N$ can be written as $p_{i_1} \\circ p_{i_2} \\circ ... \\circ p_{i_L}$ with $i_1, i_2, ..., i_L$ chosen conveniently, not necessarily distinct or increasing. It is considered that the result of composing zero permutations is the *identity permutation* ($p(i)=i$ for any $1 \\leq i \\leq N$).

# Task
A nonzero natural number $N$ is given. You are asked to construct a generating subgroup of the set $S_N$.

# Interaction
This problem is in interactive format. You will have to implement two functions:
```cpp
void selectpermgroup (int N);
```
This function needs to choose the permutations contained in the generating subgroup. Within this function, you can call the function
```cpp
void addperm(int* permutation)
```
implemented by the committee, to which you give as a parameter a pointer to the first position of a permutation of length $N$ to signal the addition of each of the permutations to the subgroup. The `selectpermgroup` function will be called only once per test. In this function, the `addperm` function can be called as many times as needed.

If you use `std::vector` from C++ STL, call `addperm(v.data())`.

It is guaranteed that in the committee's implementation, the `addperm` function will make a copy of the given permutation parameter, so there will be no issues if you reuse the pointer to the same memory area later to add another permutation.
```cpp
void solve(int N, int* permutation);
```
This function receives as parameter **the same $N$** as the previous function, and a pointer to the first element of a permutation of length $N$. You need to construct a sequence of permutations from those chosen in the previous function which, composed in the given order, give the permutation `permutation`.

Use the function provided by the committee
```cpp
void compose(int id)
```
to choose the next permutation from the composition sequence, where the parameter `id` represents the index of the permutation (starting from $0$) in the chosen subgroup. The order is consistent with that in which you called the `addperm` function within `selectpermgroup`. At the end of the `solve` function, the permutation obtained by the successive composition of all the given permutations through `compose` should be equal to the requested permutation.

**Attention!** This function will be **called multiple times** within the same test. With each call to the `solve` function, the calls to the `compose` function from the previous `solve` calls will be ignored (it starts again with $0$ permutations chosen to obtain the desired permutation).

# Scoring
For any test, if any call to the `solve` function does not correctly obtain the requested permutation or if any invalid call is made (e.g., `addperm` within `solve` or `compose` within `selectpermgroup` or invalid permutations/ids in calls to committee functions), the score for that particular test will be $0$. Otherwise, we will define the **cost** for an entire test as $|SG| \times max(C)$, where $|SG|$ is the size of the chosen subgroup and $max(C)$ is the maximum number of calls to the `compose` function within one call to the `solve` function. The next table defines the scoring structure for tests:

| Value N | Maximum Cost | Score |
| - | - | ------------|
|$N \leq 50$|$125\ 000$|$5$|
|$N \leq 100$|$40\ 000$|$5$|
|$N \leq 100$|$20\ 000$|$5$|
|$N \leq 200$|$39\ 999$|$10$|
|$N \leq 300$|$130\ 000$|$13$|
|$N \leq 600$|$140\ 000$|$15$|
|$N \leq 600$|$130\ 000$|$17$|
|$N \leq 1\ 000$|$205\ 000$|$30$|

# Example
Interactor:
`selectpermgroup(3);`
Contestant:
`addperm([2,1,3]);`
`addperm([2,3,1]);`
`addperm([3,2,1]);`
Interactor:
`solve([3, 1, 2]);`
Contestant:
`compose(1);` $[2,3,1]$
`compose(2);` $[2,3,1] \circ [3,2,1]=[1,3,2]$
`compose(0);` $[1,3,2] \circ [2,1,3]=[3,1,2]$
Interactor:
`solve([1, 3, 2]);`
Contestant:
`compose(0);` $[2,1,3]$
`compose(1);` $[2,1,3] \circ [2,3,1]=[1,3,2]$
Interactor:
`OK!` $ Cost=3 \times max(2,3)=9$