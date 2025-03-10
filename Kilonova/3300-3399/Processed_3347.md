
# Task

We have an array with $n$ natural numbers. We will repeatedly apply a `folding` operation until we reach an array consisting of a single element (with each application of the operation, the array changes, and subsequent applications are made on the modified array).

During a folding operation, the last element is folded over the first one, the second last over the second, the third last over the third, and so on. If $n$ is odd, the last element cannot be folded, so it is extracted and noted separately. The new array will have $[\\frac{n}{2}]$ elements, and each is equal to the sum of the two elements that overlap after folding.

A new folding operation is applied to the newly obtained array, and so on, until we reach an array consisting of a single element, which can no longer be folded but is noted separately.

Determine the numbers noted separately.

# Input data

The file `pliere.in` contains on the first line the number $n$ and on the second line, separated by spaces, the $n$ elements of the initial array.

# Output data

The file `pliere.out` contains on the first line the numbers noted separately, in the order of their appearance, separated by a space.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* The elements of the initial array are natural numbers with at most 2 digits.

# Example

`pliere.in`
```
11
2 3 4 7 5 6 2 1 9 4 6
```

`pliere.out`
```
6 13 30
```

## Explanation

The initial array has an odd number of elements, so the middle one, $6$, will be noted separately. After folding, the new array is: `8 7 13 8 7`

This array also has an odd number of elements, so $13$ is noted separately. After folding, we reach the array `15 15`.

This one has an even number of elements, so nothing is noted separately, and after folding, we obtain the array: $30$. This number is noted separately, and we stop.
