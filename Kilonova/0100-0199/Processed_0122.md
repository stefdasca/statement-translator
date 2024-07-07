
An application that must be executed on a multi-processor computer consists of `N` independent code fragments, which can be run in parallel. Each fragment must be executed entirely on a single processor. To parallelize the application as much as possible, the code fragments are small and thus have small execution times. More precisely, each fragment's execution takes **ONE** or **TWO** clock cycles on a **Pentium IV** processor.

The system on which the application is to be executed consists of `P` processors. Unlike most such systems, however, the `P` processors have different execution speeds. The first processor is a **Pentium IV** and is the fastest. The second processor is twice as slow as the first, the third is three times slower … the `i-th` processor is `i` times slower than the first. Under these conditions, the execution time of each code fragment differs depending on the processor on which it will be executed. Let's assume a code segment has an execution time of `T` (where `T` is `1` or `2`) on the first processor. Then on a processor `i`, its execution time will be `i*T`.

# Task
Knowing that the code fragments can be executed in any order and on any processor, and that any processor can execute at a given moment only one fragment of code, determine the minimum time after which the application (i.e., all code fragments) will finish executing. The time after which the application finishes is equal to the maximum of the times after which each processor becomes available again. The time after which a processor becomes available is equal to the sum of the execution times of the code fragments run on that processor.

# Input data
The first (and only) line of the input file `proc.in` contains three integers separated by spaces: `N` – the number of code fragments, `K` – the number of code fragments that have an execution time on a Pentium IV equal to `1` (implicitly, `N-K` have an execution time equal to `2`), and `P` – the number of processors in the system.

# Output data
The output file `proc.out` will contain a single line containing the minimum time after which the application finishes executing.

# Constraints and clarifications
* `0 \leq K \leq N \leq 1\ 000\ 000\ 000`
* `1 \leq P \leq 65\ 535`
* At least `40%` of the tests will have `N \leq 2\ 000` and `P \leq 2\ 000`.
* At least `70%` of the tests will have `N \leq 65\ 535` and `P \leq 16\ 383`.

# Example

`proc.in`:
```
4 3 2
```

`proc.out`:
```
4
```

Explanation
---

On the first processor, a code fragment with an execution time (calculated on a Pentium IV) equal to `1` and a code fragment with an execution time equal to `2` are executed => the time after which this processor becomes available is `1*1 + 1*2 = 3`. On the second processor, two code fragments with an execution time (calculated on a Pentium IV) equal to `1` are executed => the time after which this processor becomes available is `2` [number of fragments] `* (2*1)` [execution time of each fragment on processor `2`] `= 4`.
```

