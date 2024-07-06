Miruna recently learned the bubble sort algorithm during her computer science class. Below you can see the algorithm's code in C++:

```cpp
int steps = 0;
while (true) {
    ++steps;
    bool isSorted = true;
    for (int i = 1; i < n; ++i)
        if (v[i] > v[i + 1]) {
            swap(v[i], v[i + 1]);
            isSorted = false;
        }
    if (isSorted) 
        break;
}
```

Miruna defines the order of a permutation as the number of steps needed by the algorithm to sort the permutation (i.e., the value of the variable *steps* in the above code at the end of execution).

# Task

Given three natural numbers $N$, $M$, and $K$, find the $K$-th permutation in lexicographic order of length $N$ with order $M$.

# Input data

The first line of the input file `bubblesort.in` will contain three natural numbers $N$, $M$, and $K$, with the above significance.

# Output data

The first line of the output file `bubblesort.out` will contain $N$ natural numbers separated by space, representing the required permutation.

# Constraints and clarifications

* $1 \leq N \leq 300$
* $1 \leq M \leq N$
* The existence of the solution on the test data is guaranteed.

# Example 1

`bubblesort.in`
```
7 4 123
```

`bubblesort.out`
```
1 5 3 6 2 4 7
```

# Example 2

`bubblesort.in`
```
20 5 1097525229548
```

`bubblesort.out`
```
2 7 1 3 4 6 5 10 13 11 9 8 15 12 19 17 16 14 20 18
```

