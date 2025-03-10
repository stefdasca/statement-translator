
# Task
The principal wanted to recalculate by herself each average of every student admitted to her high school to ensure there were no calculation errors. Thus, she decided to implement a program to do this for her, but since she forgot her glasses at home, she cannot guarantee the accuracy of the code. However, she assures you that the problem lies in the formula used to calculate the admission average.

The admission average is calculated as follows:  

* The overall average of the middle school years has a weight of $20 \\%$.  
* The grade from the National Evaluation exam in Romanian Language and Literature has a weight of $40 \\%$.  
* The grade from the National Evaluation exam in Mathematics has a weight of $40 \\%$.  

Thus, $\\text{admissionAverage} = (\\text{middleSchoolAverage} \\cdot 0.20) + (\\text{romanianGrade} \\cdot 0.40) + (\\text{mathGrade} \\cdot 0.40)$.

You can find the incorrect program [here](bad_source.cpp) or in the "Attachments" section on the side.

# Input data
The program will read from the keyboard the overall average of the middle school years, the grade from the National Evaluation exam in Romanian Language and Literature, and the grade from the National Evaluation exam in Mathematics.

# Output data
Print the admission average of the student.

# Constraints and clarifications
Each average is between $1.00$ and $10.00$, and the averages will have two decimal places.

# Example 1
`stdin`
```
8.15 6.20 9.20
```
`stdout`
```
7.79
```
## Explanation

$7.79 = (8.15 \\cdot 0.20) + (6.20 \\cdot 0.40) + (9.20 \\cdot 0.40)$

# Example 2
`stdin`
```
5.00 9.90 10.00
```
`stdout`
```
8.96
```
## Explanation
$8.96 = (5.00 \\cdot 0.20) + (9.90 \\cdot 0.40) + (10.00 \\cdot 0.40)$
