# Task
The name of this problem is Calafat because it was composed during tomorrow's trip to Calafat.

# Task
Given an array of `N` natural numbers. For each distinct value in a subarray defined by `2` indices `st` and `dr`, consider the distance between the indices of its first and last appearance within the subarray. Given `M` subarrays of the form `[st, dr]`, the task is to calculate the sum of the distances corresponding to all distinct values in the subarray.

# Input data
The first line of the input file `calafat.in` will contain two natural numbers `N` and `M`. The second line will contain the `N` numbers of the given array. The next `M` lines will contain two numbers `st` and `dr`, indicating that we want to calculate the sum mentioned above for the subarray `[st, dr]`.

# Output data
The output file `calafat.out` will contain `M` natural numbers, one on each line, representing the `M` required sums.

# Constraints and clarifications
* `1 \leq N, M \leq 200\ 000`
* `1 \leq st \leq dr \leq N`
* The values in the array will be within the range `[1, N]`
* For `20%` of the tests, it is guaranteed that `N, M \leq 1000`
* For another `25%` of the tests, it is guaranteed that `N, M \leq 35\ 000` and the number of distinct elements in the array is at most `100`
* For another `25%` of the tests, it is guaranteed that `N, M \leq 70\ 000`

# Example

`calafat.in` 
```
7 3 
1 3 1 2 2 1 3 
2 4 
2 7 
3 6
```

`calafat.out`
``` 
0 
9 
4
```

# Explanations

In the first subarray, each value appears only once, so the sum of the differences is `0`.

In the second subarray:
- The value `3` appears at indices `2` and `7`, resulting in the difference `7-2=5`
- The value `1` appears at indices `3` and `6` -> difference `6-3=3`
- The value `2` appears at indices `4` and `5` -> difference `5-4=1`

The sum of the differences is 9.

In the third subarray:
- The value `1` appears at indices `3` and `6` -> difference `6-3=3`
- The value `2` appears at indices `4` and `5` -> difference `5-4=1`

The sum of the differences is `4`.