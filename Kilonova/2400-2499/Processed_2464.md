> "Only in Ohio could something like this happen..." - Baby Gronk 

# Task 
In Ohio, there exists a keyboard with \( N \) buttons connected to a computer, and each button is assigned a value \( a_i \). However, since it's Ohio, the keyboard is broken. When a combination of \( K \) buttons is pressed, the computer will display the maximum value among the values of the buttons that were pressed. Since Baby Gronk is from Ohio, he will press all possible combinations of \( K \) distinct buttons. What is the sum, modulo \( 1\ 000\ 000\ 007 \), of the values that appear on the computer screen?

# Input data 
The first line of the input file `ohio.in` contains \( N \) and \( K \). The next line contains \( N \) values \( a_i \).

# Output data
The first line of the output file `ohio.out` will contain the answer to the problem, as described in the statement. 

# Constraints and clarifications 
* \( N \le 100\ 000 \), \( K \le 50 \)
* \( a_i \le 10^9 \)
* For 40 points, \( N \le 1000 \)

# Example 1
`ohio.in`
``` 
5
3 2 4 2 3 4 
``` 
`ohio.out`
``` 
39 
```
## Explanation 
All subsets of values corresponding to all possible combinations are: [2, 4, 2], [2, 4, 3], [2, 4, 4], [2, 2, 3], [2, 2, 4], [2, 3, 4], [4, 2, 3], [4, 2, 4], [4, 3, 4], [2, 3, 4].

# Example 2 
`ohio.in`
```
5 
1 1 0 1 1 1 
```
`ohio.out`
```
4 
```

# Example 3
`ohio.in` 
```
5 
2 3 3 4 0 0
```
`ohio.out` 
```
31
```