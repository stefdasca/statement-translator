
# Task
To ensure that all information sent by Digit Chief is valid, he decided to add a control digit in addition to the data. This control digit is obtained by summing the digits of a number, then summing the digits of the result again, and so on until the result becomes a single digit. For example, for the number $1234$, we first obtain $1+2+3+4=10$, and then for $10$, we obtain $1+0=1$, which is the control digit. He decides to implement this in a program, but Zoly the meerkat, who is a very good programmer, decided to make a joke and break his program. Help Digit Chief fix his program and obtain the correct control digit. You can find the program [here](bad_source.cpp) or in the "Attachments" section on the side.

# Input data
The number $n$ is read from the keyboard, for which the control digit needs to be calculated.

# Output data
The control digit of the number $n$ is displayed on the screen.

# Constraints and clarifications

* $0 \leq n \leq 1 \ 000 \ 000 \ 000$

# Example
`stdin`
```
123456789
```
`stdout`
```
9
```
## Explanation
$123 \ 456 \ 789 \rightarrow 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45$;

$45 \rightarrow 4 + 5 = 9$
