```markdown
A vector is read from the keyboard until the element $0$. A second vector is also read, again until the element $0$.

# Task
How many elements from the second vector are present in the first? The code for this problem is almost ready, but it contains some bugs. You can find the code [here](intersectie.cpp) or in the "Attachments" section on the side.

# Input data

The first line of the console contains multiple non-zero numbers representing the elements of the first array, followed by the number $0$.

The second line of the console contains multiple non-zero numbers representing the elements of the second array, followed by the number $0$.

# Output data

The console will contain a number representing the answer to the task.

# Constraints and clarifications
- All input values can be stored in the `int` data type.
- The first array contains at most $10\ 000$ values.
- The second array contains at most $1\ 000$ values.

# Example

`stdin`
```
1 2 3 4 0
4 4 1 -1 0
```

`stdout`
```
3
```
```