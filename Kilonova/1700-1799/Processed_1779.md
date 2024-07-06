Thermopanes likes to play with very large natural numbers. Sometimes his sister gives him a new number, and in this case, he adds it to his collection of numbers. Other times his sister asks him: **"If you were to arrange the numbers in your collection in ascending order, what would be the number at position $k$?"**

# Task

Given a sequence of operations where Thermopanes' sister either gives him a number or asks him a question, respond in order to all the questions asked.

# Input data

The input file `nums.in` will contain on the first line the natural number $n$ representing the number of operations. The next $n$ lines will contain $2$ numbers $t$ and $x$ separated by a space. If $t$ is $1$, then the element $x$ is added to Thermopanes' collection, and if $t$ is $0$, then Thermopanes is asked a question.

# Output data

The output file `nums.out` will contain $L$ lines (one line for each operation of type $0$). Each line $i$ will contain the answer to the $i$-th question.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$
* $1 \leq k \leq$ number of elements in the collection at the time of the question
* The number of digits of any number added to the collection will not exceed $100 \ 000$
* The size of the input file will not exceed $6$ MB
* If Thermopanes receives a number already existing in his collection, he will not add it again.
* No number starts with $0$

# Example 1

`nums.in`
```
7
1 1232
1 1002
1 212
0 2
1 213
1 123
0 3
```

`nums.out`
```
1002
213
```

## Explanation

At the moment the first question is asked, the numbers in the collection are: $212 \ 1002 \ 1232$, with the $2$-nd being $1002$. When the second question is asked, the numbers are: $123 \ 212 \ 213 \ 1002 \ 1232$, with the $3$-rd being $213$.