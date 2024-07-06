Below is the translated text according to the given instructions:

---

At the National Olympiad in Informatics, students from several counties participate, each county being uniquely identified by a natural number. Students in each county are associated with a natural number that uniquely identifies the student within the county.

Therefore, any participant in the Olympiad can be identified by two numbers: the county identifier and the student identifier within the county.

To allocate students to computers, organizers need a list that meets the following conditions:
- the list contains all the students participating in the Olympiad;
- any two consecutive students in the list are from different counties;
- students from any county appear in the list in ascending order of their identification numbers.

# Task
Write a program that generates the list needed by the organizers.

# Input data
The input file `concurs.in` contains on the first line a natural number $P$ representing the total number of participants in ONI. On the next $P$ lines, the list of participants is described, one participant per line. For each participant, two natural numbers separated by a space $J$ and $E$ are given, where $J$ represents the county identifier and $E$ represents the student identifier within the county.

# Output data
The output file `concurs.out` will contain on the first line a natural number $NJ$, representing the number of counties from which there are participants in the Olympiad.

On the second line, $NJ$ non-zero natural numbers separated by a space representing (in ascending order of county identification numbers) the number of participants from each county. On the next $P$ lines, the list needed by the organizers is described, one student per line. For each student, the county identifier they are part of is written first, followed by a space, then the student identifier within the county.

# Constraints and clarifications
- County identifiers are natural numbers between $1$ and $50$.
- Student identifiers within counties are natural numbers between $1$ and $1\ 000$.
- The total number of students participating in the Olympiad does not exceed $500$.
- For the test data, a solution always exists, not necessarily unique.
- For the correct determination of the number of counties, $20\\%$ of the score is awarded. For the correct determination of the number of counties as well as the number of participants from each county, $30\\%$ of the score is awarded. The full score is awarded for solving all three requirements (number of counties, number of participants from each county, and the list needed by the organizers).

# Example
`concurs.in`
```
7
1 3
2 4
1 2
5 2
5 3
1 6
1 9
```
`concurs.out`
```
3
4 1 2
1 2
5 2
1 3
5 3
1 6
2 4
1 9
```

---

I have translated the entire problem statement and ensured both the format and instructions are preserved. Additionally, potential grammar and syntax issues have been checked and corrected as per English language rules.