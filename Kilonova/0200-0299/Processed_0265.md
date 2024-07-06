Here is the translated text with the specified instructions applied:

---

Consider an array of `N` integers, indexed from `1`. We define the second maximum of the array as the largest number in the array, excluding the maximum. To find the maximum and second maximum, you will perform comparisons between the elements of the array.

Given that you only have $N+\lceil \log_2 N \rceil-2$ comparisons, find the positions of the maximum and second maximum. Here, $\lceil \log_2 N \rceil$ denotes the ceiling of the logarithm base `2` of `N`.

# Task

Find the two numbers, performing at most $N+\lceil \log_2 N \rceil-2$ comparisons. To make the comparisons, the following function is provided to you:

```cpp
int compare(int i, int j)
```

which compares the number at position `i` with the one at position `j` and returns `1` if the element at position `i` is greater than or equal to the one at position `j`, or `-1` otherwise. If `i` or `j` is an invalid index, the function will return `0`.

The program must implement the function
```cpp
std::pair<int, int> solve(int N)
```
\
where `N` has the meaning described above. The function will return the two required values.

# Constraints and clarifications
* `2 \leq N \leq 100 000`
* The file `compare.h` must be included
* The problem has been modified
* For `20` points, you can use a maximum number of $2 \cdot N-3$ comparisons
* For another `80` points, you can use a maximum number of $N+\lceil \log_2 N \rceil-2$ comparisons

# Example 1

If the considered array is `(5, 3, 4)`, then a correct execution of the program is as follows:

`compare(1, 2)` which returns `1`;

`compare(1, 3)` which returns `1`;

`compare(2, 3)` which returns `-1`;

At this point, you have exhausted the allowed number of comparisons (`3+2-2=3` comparisons) and the function will return the numbers `1` and `3`, representing the positions that hold the maximum of the array (`5`), and the second maximum (`4`), respectively.

# Example 2

If the considered array is `(5, 7, 7)`, a correct execution of the program is as follows:

`compare(1, 2)` which returns `-1`;

`compare(2, 3)` which returns `1`;

`compare(1, 3)` which returns `-1`;

At this point, you have exhausted the allowed number of comparisons (`3+2-2=3` comparisons) and the function will return the numbers `2` and `3`, representing the positions that hold the maximum of the array (`7`), and the second maximum (`7`), respectively.

Note:
For this example, there is another correct solution, where you consider the maximum (`7`) at position `3` and the second maximum (`7`) at position `2`.

---