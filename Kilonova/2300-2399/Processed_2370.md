
# Problem Statement

Let's consider a binary matrix with $n$ rows (numbered from $1$ to $n$) and $m$ columns (numbered from $1$ to $m$). Inside this matrix, we can distinguish one or more objects of type `I`.

An object is considered to be of type `I` if:
* it is formed from three subarrays (rectangular zones of the matrix) adjacent vertically (let's call them the top subarray, the middle subarray, and the bottom subarray);
* the $3$ subarrays contain only the value $0$;
* the subarrays can be identified by the indices of the elements that represent the top-left corner and bottom-right corner (for the top subarray $(l_1, c_1) \\ (l_2, c_2)$, for the middle subarray $(l_3, c_3) \\ (l_4, c_4)$, and for the bottom subarray $(l_5, c_5) \\ (l_6, c_6)$). For the object to respect the graphical form of the letter `I`, the following relationships must also be respected:
* $1 \\leq l_1 \\leq l_2 < l_3 \\leq l_4 < l_5 \\leq l_6 \\leq n;$
* $l_3 = l_2 + 1;$
* $l_5 = l_4 + 1;$
* $1 \\leq c_1 < c_3 \\leq c_4 < c_2 \\leq m;$
* $1 \\leq c_5 < c_3 \\leq c_4 < c_6 \\leq m;$

~[imag.png]

# Task

Determine the maximum area of an object of type `I`. The area of an object is equal to the number of elements existing in the 3 subarrays that constitute the object.

# Input data

The first line of the file `imax.in` contains two natural numbers separated by a space $n$ and $m$, with the significance given in the statement. The next $n$ lines contain $m$ values from the set $\{0, 1\}$, separated by a space, representing the elements of the matrix.

# Output data

The output file `imax.out` will contain a single line which will print the maximum area of an `I` object.

# Constraints and clarifications

* $1 \\leq N \\leq 150$;
* $1 \\leq M \\leq 150$;

# Example

`imax.in`
```
4 4
0 0 0 0
1 0 0 1
0 0 0 1
0 1 1 0
```

`imax.out`
```
8
```

~[explicatie.png|align=left]
