Let's imagine that at a certain high school there are only two classes per year: one for Science and one for Humanities. Currently, registrations for the ninth grade are taking place. Each of the two classes has $M$ available spots, both in Science and Humanities. If the list of students registered for a certain class contains more than $M$ students, the top $M$ students with the highest grades will be admitted. Both classes already have $M$ registered students, and for each of them, the registration grades are known.

There are still $N$ remaining students who have not yet registered and are privileged in this process (since they have graduated middle school at this high school). Their privilege is that they can now register after the public registrations have ended, and the registration grades for both classes are known. Each of the $N$ students has two grades: the grade for Science and the grade for Humanities (these may differ since the admission exams for the two classes are different). Each of the $N$ students will choose to register in at most one class. They will coordinate their choices to **maximize** the number of admitted students. Because the calculations become quite complex, they may use your help.

# Task
The $N$ students want answers to the following two questions:
1) What is the maximum number of **privileged** students who can be admitted if there is an additional restriction that all the admitted privileged students must be admitted to the same class?
2) What is the maximum number of **privileged** students who can be admitted if they can register in different classes?

# Input data
The input file `admitere.in` contains on the first line a value equal to $1$ or $2$, representing the task to be solved. The next line contains the two numbers $N$ and $M$. The third line contains $M$ numbers, separated by spaces, representing the grades of the students currently forming the Science class. The fourth line contains $M$ numbers, separated by spaces, representing the grades of the students currently forming the Humanities class. The following $N$ lines will contain a pair of numbers $R_i$ and $U_i$, separated by a space, representing the grade with which the $i$-th privileged student would register for the Science class and the Humanities class, respectively.

# Output data
The output file `admitere.out` will contain on the first line the value $MAX$: the maximum number of admitted privileged students. The second line will contain a string of $N$ characters from the set $\\{$`R`$, `U`$, `X`\\}$, which will describe the optimal scenario. If the $i$-th student registers for Science, the $i$-th character will be `R`. If the $i$-th student registers for Humanities, the $i$-th character will be `U`. If they do not register anywhere, the $i$-th character will be `X`.

Since students do not want to make unnecessary efforts, any privileged student who will not be admitted in the optimal scenario will register in no class. In other words, for the described scenario to be considered correct, it is necessary that **exactly $MAX$** characters in the string are different from `X`.

# Constraints and clarifications
- $1 \\leq N, M \\leq 2\ 000$
- Tests worth a total of 25 points will request solving task 1, while the remaining 65 points will request solving task 2. A default of 10 points is granted.
- For task 2, tests worth a total of 45 points will have $1 \\leq N, M \\leq 150$.
- All $N + M$ grades for the Science class are distinct in pairs. The same applies to the grades for the Humanities class.
- All grades are natural numbers in the range $[1, 4\ 000]$.
- The grades of the students already registered for the Science and Humanities classes will be given in ascending order.
- If there are multiple correct solutions, any of them is accepted.

# Example 1
`admitere.in`
```
1
2 3
2 4 6
6 7 8
3 5
12 14
```
`admitere.out`
```
1
XR
```
## Explanation
It is not possible for both students to be admitted to the same class. There are several solutions where only one student is admitted: `XR`, `XU`, `RX`. Any of these is correct.

# Example 2
`admitere.in`
```
2
2 3
2 4 6
6 7 8
3 5
12 14
```
`admitere.out`
```
2
RU
```
## Explanation
Since we are solving task 2, it is allowed to register students in different classes. There is a solution where both students are admitted, and it is unique: the one where the first student is registered for Science (they could not be admitted to Humanities regardless of the decision of the second student), and the second student is registered for Humanities.