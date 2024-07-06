# Task

Gheorghe has started piano lessons and learned that he can create a scale by choosing $7$ notes from the set of $12$ notes available on the piano. He received a homework task from his teacher Tiberiu, to compose a progression. For the melody to sound harmonious, teacher Tiberiu taught him to use only notes from a single scale. Moreover, he asked the melody to be **as long as possible**.

The notes are numbered from $1$ to $12$, and to simplify the task, Tiberiu told him to put the notes from the chosen scale into a melody such that the first note is smaller than the second and no two adjacent notes are equal. For example, if the scale $1, 2, 3, 4, 7, 9, 10$ is chosen, the notes from that scale must be used to create that sequence. (A correct melody example would be: $1, 2, 3, 4, 3, 2, 7, 9, 10$, and incorrect ones would be: $2, 1, 3, 4, 3, 2, 7, 9, 10$ or $1, 2, 2, 4, 3, 2, 7, 9, 10$). **The main goal of Gheorghe is to select the set of $7$ notes such that he can create the longest possible melody respecting these conditions and present this melody.**

Gheorghe was deeply thinking about a shawarma during the lesson and did not understand much. He tried to do his homework, but the melody sounded mediocre. Help Gheorghe to fix the melody by selecting only one scale from it and rearranging the notes of the scale so that Tiberiu will still keep him in the lessons. He must form the longest melody that respects Tiberiu's conditions.

# Input data

The input file `tralala.in` contains on the first line the natural number $N$, the number of notes Gheorghe initially used.  
The second line of the input file `tralala.in` contains a sequence of $N$ natural numbers from $1$ to $12$ representing the sequence of notes of the initial melody.

# Output data

The output file `tralala.out` will contain on the first line a natural number $L$ representing the number of notes used after the melody has been fixed.  
The second line of the output file `tralala.out` will contain a sequence of natural numbers separated by spaces, from $1$ to $12$, representing the melody Gheorghe presents to Tiberiu in the next class. (He trusts you)

# Constraints and clarifications

* $1 \\leq N \\leq 1\ 000\ 000$;
* All notes in the initial and final sequence will be from $1$ to $12$
* It is guaranteed that in the initial melody there will be at least $7$ different notes
* The score for each of the $50$ tests will be calculated according to the following formula: **Let $L$ be the length obtained by your solution and $L_o$ be the length obtained by the committee's solution**. If the solution is correct and respects the above rules, the score obtained for each test is: $2 \cdot min(1, \frac{L}{L_o}^2)$

# Example 1

`tralala.in`
```
20
1 5 12 3 10 5 2 6 11 2 2 3 1 6 12 3 9 5 8 8
```

`tralala.out`
```
17
1 2 3 5 6 8 12 8 6 5 3 2 1 2 3 5 12 
```

## Explanation

This melody consists of $17$ notes, obtaining the maximum score.

# Example 2

`tralala.in`
```
10
1 1 1 2 2 3 4 5 6 7
```

`tralala.out`
```
9
1 7 3 5 4 2 7 2 1
```

## Explanation

This solution consists of $9$ notes, and the optimal melody consists of $10$, so the score obtained on this test would be $2 \cdot \frac{9}{10}^ 2 = 1.62$