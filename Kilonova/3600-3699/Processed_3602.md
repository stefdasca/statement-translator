The director of our school has a big problem: How many times must an URGENT!!! message be sent? Regardless of the communication channel used (e-mail, WhatsApp, the school website, etc.), there will always be students to whom the message either does not reach or does not arrive in a timely manner. After many attempts, the director has decided to number the $n$ students in the school with distinct numbers from $1$ to $n$ and to study the communication relationships between the students. Then, based on these communication relationships, to choose a minimum number of spreading students to which he can directly send the message, which will then be transmitted to all students through the communication relationships among them.

# Task

Write a program that, knowing the communication relationships between students, determines the minimum number of spreading students required for the director’s message to reach all the students in school in a timely manner.

# Input data

The input file `raspandaci.in` contains on the first line the natural number $n$, representing the number of students in school. The following lines contain pairs of natural numbers $x \\ y$ ($1 \\leq x, y \\leq n$) meaning that student $x$ immediately transmits any message received to student $y$.

# Output data

The output file `raspandaci.out` will contain a single line on which the minimum number of spreading students necessary for the director’s message to reach all the students in the school in a timely manner will be written.

# Constraints and clarifications

* $2 \\leq n \\leq 10^5$;
* The number of communication relationships between students in the input file is $\\leq 400 \\ 000$;
* A student can also communicate the message to themselves.

|#|Points|Constraints|
|-|-------|-----------|
|0|  10   |Mandatory|
|1|  30   |$2 \\leq n \\leq 100$|
|2|  11   |$100 \\lt n \\leq 1 \\ 000$|
|3|  49   |No additional constraints|

# Example

`raspandaci.in`
```
6 
2 1 
1 6 
3 4 
4 1 
3 5 
4 3 
5 1 
6 5
```

`raspandaci.out`
```
2
```

## Explanation

The two spreading students could be students $2$ and $3$. If the director sends the message to student $2$, it will also reach students $1$, $5$, and $6$. 
Additionally, if the message is also sent to student $3$, it will also reach student $4$.

Another possible solution would be for the director to send the message to students $2$ and $4$.