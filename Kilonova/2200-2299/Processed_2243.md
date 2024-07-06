```markdown
Marius promised his parents that if they buy him an AcadStation 6 console, he will finish the school year with an average grade of 10. However, since Marius was busy playing games, he couldn't keep his promise and realizes that his only solution is to break the school's grading program.

# Task

Help Ms. Acadania solve the problem! You can find the program [here](medii.cpp) or in the "Attachments" section on the side.

# Input data

The program reads from the keyboard the numbers $n$ and $m$, representing the number of students in Marius's class and the number of grades for each student, respectively. Then, $n$ lines are read with $m$ natural numbers each, representing the grades of each student.

# Output data

The screen will display the averages in descending order with a precision of up to $2$ decimal places.

# Constraints and clarifications

- **Do not modify the line `cout << setprecision(3);`!**
- $0 \le n \le 27$
- $0 \le m \le 15$
- The $n \cdot m$ numbers read will be natural numbers between $1$ and $10$.

# Example

`stdin`
```
3 5
1 2 3 4 6
3 2 6 10 2
4 2 1 5 9
```

`stdout`
```
4.6 4.2 3.2
```

## Explanation

The average for each student is calculated, then ordered in descending order.

For the first student, the average is $ \frac{1 + 2 + 3 + 4 + 6}{5} = 3.2 $.

For the second student, the average is $ \frac{3 + 2 + 6 + 10 + 2}{5} = 4.6 $.

For the third student, the average is $ \frac{4 + 2 + 1 + 5 + 9}{5} = 4.2 $.
```
