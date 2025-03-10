# Task

Consider the following implementation of the quicksort algorithm:

``` cpp
int cnt = 0, v[MAX_N + 1], mai_mici[MAX_N], mai_mari[MAX_N]; // global variables

int pivot(int st, int dr) {
    int nr_mai_mici = 0, nr_mai_mari = 0;
    for (int i = st + 1; i \leq dr; i++) {
        if (v[i] < v[st])
            mai_mici[++nr_mai_mici] = v[i];
        else
            mai_mari[++nr_mai_mari] = v[i];
        cnt++;
    }

    v[st + nr_mai_mici] = v[st];
    for (int i = 1; i \leq nr_mai_mici; i++)
        v[st + i - 1] = mai_mici[i];
    for (int i = 1; i \leq nr_mai_mari; i++)
        v[st + nr_mai_mici + i] = mai_mari[i];

    return st + nr_mai_mici;
}

void sorteaza(int st, int dr) {
    if (st < dr) {
        int p = pivot(st, dr);
        sorteaza(st, p-1);
        sorteaza(p+1, dr);
    }
}
```

For an array $v$ with $n$ elements stored at positions from $1$ to $n$, we call `sorteaza(1,n);`, after which the array $v$ becomes sorted in ascending order.

A permutation of $n$ elements is an array of $n$ natural values between $1$ and $n$, distinct two by two.

Given a specified $n$, determine a permutation of $n$ elements, such that applying the above algorithm results in the variable `cnt` having a minimal final value. If there are multiple permutations that satisfy the task, determine the lexicographically smallest permutation among them.

# Input data

The file `quick.in` contains on the first line two natural numbers separated by space, $p$ and $n$.

# Output data

For $p=1$, the file `quick.out` contains on the first line the minimum value obtained in the variable `cnt` after applying the algorithm for a permutation of length $n$.
For $p=2$, the file `quick.out` contains on the first line $n$ distinct natural numbers, between $1$ and $n$, separated by spaces, representing the lexicographically smallest permutation of length $n$, corresponding to the minimum calculated value in the variable `cnt`, after the sorting algorithm is complete.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$
* An array $a_1, a_2, \ldots, a_n$ is lexicographically smaller than another array $b_1, b_2, \ldots, b_n$ if there exists an integer $i$ ($1 \leq i \leq n$) such that: $a_1 = b_1$, $a_2 = b_2$, $ \ldots $, $a_{i−1} = b_{i−1}$, and $a_i < b_i$.
* For tests worth $6$ points $p = 1$ and $n \leq 10$;
* For other tests worth $9$ points $p = 2$ and $n \leq 10$;
* For other tests worth $20$ points $p = 1$ and $n \leq 5 \ 000$;
* For other tests worth $30$ points $p = 2$ and $n \leq 5 \ 000$;
* For other tests worth $14$ points $p = 1$.

# Example 1

`quick.in`
```
1 4
```

`quick.out`
```
4
```

# Example 2

`quick.in`
```
2 4
```

`quick.out`
```
2 1 3 4
```

## Explanation

Starting from the sequence `2 1 3 4`, during the call `sorteaza(1, 4)` there are three increments to `cnt`. Afterwards, the sequence becomes `1 2 3 4`. Then there are two more recursive calls, `sorteaza(1, 1)` and `sorteaza(3, 4)`. The first recursive call performs no more increments, while the second performs one increment, then calls `sorteaza(3, 2)` and `sorteaza(4, 4)`, which perform no further increments. In total, there are $4$ increments.

Similarly, for the sequence `3 2 1 4`, $4$ increments are also made: during the call `sorteaza(1, 4)` three increments are performed, turning the sequence into `2 1 3 4`, then two more recursive calls are made, `sorteaza(1, 2)` and `sorteaza(4, 4)`, the latter performing no more increments, while the first performs one, turning the sequence into `1 2 3 4`, calling further `sorteaza(1, 1)` and `sorteaza(3, 2)`, which perform no additional increments. This sequence `(3 2 1 4)` is not an acceptable solution as it is not lexicographically smaller than `2 1 3 4`.

Note that we are not interested in the moment when the sequence gets sorted but in the number of increments the given algorithm makes on the detected permutation. For example, if the obtained permutation was `1 2 3 4`, a call to `sorteaza(1,4)` would have made three increments, and then the permutation would have remained the same, followed by a recursive call to `sorteaza(2,4)`, which performs two more increments, followed by the recursion `sorteaza(3, 4)` which makes one increment, and then `sorteaza(4, 4)` which performs no more increments. Therefore, the number of increments would have been $6$, even if the given sequence was already in ascending order.