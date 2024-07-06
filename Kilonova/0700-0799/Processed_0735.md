Mircea is passionate about programming. He has started solving increasingly difficult problems. Thus, he encountered a problem that provides a square array with $n$ rows and $n$ columns, the components of the array being all distinct natural numbers from $1$ to $n^2$. To verify the program he wrote, he needs a file containing that array. After he created this file, his brother, who likes to play tricks, tampered with the file and replaced some consecutive numbers with the number $0$. When Mircea returns from playing, he is astonished to find that his program doesn't work for that specific test. After debugging for a few hours, he realizes that his program is correct and that the input file has issues.

# Task
Write a program to help Mircea by finding the smallest and the largest of the consecutive numbers that his brother changed.

# Input data
The file `numere.in` will contain on the first line $n$, and on the next $n$ lines, the elements of the array, with $n$ elements per line separated by a space, after the modifications made by Mircea's brother.

# Output data
The file `numere.out` will contain on a single line, with a single space between them, the required numbers (the first one being the smallest).

# Constraints and clarifications
- $0 < n \leq 500$
- Mircea's brother changes at least one number in the file.
- The numbers changed by Mircea's brother are smaller than or equal to $60\ 000$.

# Example
`numere.in`
```
3
5 0 7
0 0 1
6 9 8
```
`numere.out`
```
2 4
```
## Explanation
In the input file, the numbers $2$, $3$, and $4$ were replaced by $0$.