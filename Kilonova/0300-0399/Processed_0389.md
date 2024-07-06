*"Yellow sun, its evil twin,
In the black, the winds deliver him"*

Humanity is on the brink of nuclear collapse. Dr. Merkwürdigliebe is designing an operating system for guiding rockets. The survival of humanity depends on the memory allocation algorithm implemented by the **kmalloc** function.

This function receives a single parameter `size`, a natural number, identifies a continuous free memory area of size $2^{size}$ and returns the starting address of this area. After this moment, the respective memory area becomes occupied.

The operating system has at its disposal $N$ bytes numbered from `0` to `N - 1`. `P` continuous memory intervals are given, which are already reserved and cannot be used for allocation.

The program you will write to save humanity will provide an implementation of the `kmalloc` function and will not read from or write to any file. Instead, your program will implement the following functions:

```cpp
void init(long long N, int P, std::vector<std::pair<long long, long long>> intervals);
long long kmalloc(int size);
```

The `init` function will be called only once at the beginning of each test and will provide `N` - the number of available bytes, `P` - the already reserved intervals and an array containing two integers between `0` and `N - 1`, representing the starting and ending addresses of the reserved intervals. These intervals will not overlap and will be given in the ascending order of the occupied addresses.
The `kmalloc` function will be called multiple times during a test and will need to return the starting memory address of the allocated area of size $2^{size}$.

You don't need to implement the `main` function, but you can declare additional variables/functions.

# Constraints and clarifications
* $1 \leq N \leq 2^{62}$
* The `kmalloc` function will be called at most `500 000` times per test
* `0 \leq P \leq 100 000`
* The commission's program will adapt to the strategy chosen by the competitor.
* It is guaranteed that all memory allocation requests can be met by a suitable algorithm.

# Example
The function `init(13, 2, {{5,5},{6,6}})` is called by the commission.
There are `13` available bytes numbered from `0` to `12` and `2` reserved intervals. Byte `5` is reserved, byte `6` is reserved.
The function `kmalloc(2)` is called, returning `0`.
A request to allocate a `4`-byte area is made, allocating bytes `0, 1, 2, 3`.
The function `kmalloc(0)` is called, returning `4`.
A request to allocate a `1`-byte area is made, allocating byte `4`.
The function `kmalloc(1)` is called, returning `7`.
A request to allocate a `2`-byte area is made, allocating bytes `7, 8`.
The function `kmalloc(2)` is called, returning `9`.
A request to allocate a `4`-byte area is made, allocating bytes `9, 10, 11, 12`.