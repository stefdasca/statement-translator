Gigel is passionate about order. When he visits his grandmother, he always tidies up the kitchen cabinet, where the plates are in 3 vertical stacks. These plates are sometimes not arranged by their size. Yesterday, when he visited his grandmother, he decided to arrange all the plates into a single stack, ordered in descending order from the base to the top by diameter. To add a gameplay element to this activity, he decided that in each move he would take only one plate from the top of a stack and place it on top of another stack, and he would never place a larger plate over a smaller one.

To be able to code the moves, the three stacks of plates will be called columns and will be numbered 1, 2, and 3. At any moment, any of the columns may or may not contain plates. If a column does not contain any plates, we will say that it is empty. On an empty column, you can place any plate that can be accessed. If a column contains at least one plate, then a new plate can be placed on top of this column only if the diameter of the new plate is less than or equal to the diameter of the plate on the top of the column.

The solution to the problem will consist of a succession of operations. An operation consists of extracting a plate from a column \( C_1 \) and placing it on another column \( C_2 \), respecting the above constraints. Given a column \( C \), we say that the sequence of operations is correct if, after executing all operations, all the plates are on column \( C \), in descending order of diameters from the base to the top.

# Task

Knowing the configuration of the initial three stacks of plates, as well as the number \( C \) of the column where the plates should be at the end, write a program that determines a correct sequence of operations.

# Input data

The input file `farfurii.in` contains 4 lines. The line \( i \ (1 \leq i \leq 3) \) contains the natural number \( N_i \), which represents the number of plates in column \( i \), followed by \( N_i \) natural numbers separated by a space, representing the sizes of the plate diameters from the base to the top of column \( i \) (if \( N_i = 0 \), then there are no plates on column \( i \)). The last line contains the number \( C \ (1, 2 \text{ or } 3) \), representing the column where all the plates will be finally placed.

# Output data

The output file `farfurii.out` will contain the operations, in the order of their execution, one operation per line. An operation will be described by two numbers separated by a space \( C_1 \space C_2 \) with the meaning: "the plate from the top of column \( C_1 \) is moved to the top of column \( C_2 \)". On the last line, the numbers \( 0 \space 0 \) will be printed.

# Constraints and clarifications

- \( 1 \leq C_1, C_2, C \leq 3 \)
- \( 1 \leq \) sizes of the plate diameters \( \leq 100 \)
- \( 2 \leq N_1 + N_2 + N_3 \leq 18 \)
- The solution is not unique. Any correct solution is accepted. It is not required to optimize the number of operations, but the problem-solving must fit within the specified execution time.

|#|Points|Constraints|
|-|-|-|
|1|4|All the plates are of the same size.|
|2|11|There are only two different plate sizes.|
|3|12|There are only three different plate sizes.|
|4|22|All the plates are arranged on a single column.|
|5|14|All the plates form two increasing columns from base to top.|
|6|18|All the plates have different sizes.|
|7|19|Without additional constraints|

# Example

`farfurii.in`
```
2 1 7
3 5 1 9
0
3
```

`farfurii.out`
```
2 3
1 3
2 1
2 3
1 2
1 3
2 3
0 0
```

## Explanation

The plates need to be placed on column \( C = 3 \). Initial configuration:

~[img1.jpg|align=center]