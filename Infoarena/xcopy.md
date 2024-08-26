## Task

Today, at the end of the computer science class, the teacher gave a very difficult homework problem, so the students decided to copy from each other. However, they must work smart to avoid being caught. The class consists of $N \times M$ students, seated in desks arranged in $N$ rows and $M$ columns. We say that two students are neighbors if they are in adjacent desks either in rows or columns. Each child's homework consists of finding a natural number. To avoid getting caught, all their homeworks must be distinct. Moreover, the students are very lazy, so they will change their homework very little compared to their neighbors' homework. Specifically, any student's homework differs by exactly one bit in binary representation from their neighbor's homework. For example, $3$ and $2$ differ by exactly one bit, while $2$ and $4$ differ by two bits. To avoid raising too much suspicion, the students want to create their homeworks such that the highest value of any homework is as small as possible. Given the dimensions of the class, $N$ and $M$, construct a configuration of homework values for each student in the class so the teacher won't realize they copied.

## Input data

The input file `xcopy.in` contains on the first and only line 2 numbers separated by a single space, $N$ and $M$ as described above.

## Output data

The output data, to be printed in the output file `xcopy.out`, consists of printing the configuration of homework values for each student. The file will contain $N$ rows, and on each row, there will be $M$ natural numbers separated by a space. These represent the students' answers corresponding to their positions in the class.

## Constraints and clarifications

$1 \leq N, M \leq 2000$

## Constraints

Additionally:
### Points

## Constraints

$1$

$7 \ N=1$

$2$

$9 \ N$ and $M$ are powers of $2$

$3$

$14 \ N$ is a power of $2$

$4$

$70$ No additional constraints

## Scoring

This problem also accepts partial solutions, so partial points are awarded for each test, depending on how close the given solution is to the optimal answer using the following formula:

Where:

$S$ is the test score,

$G$ is the given answer,

$O$ is the optimal answer.

Attention! A solution that does not meet all the requirements of the problem for a specific test (all numbers must be distinct and any two adjacent numbers must differ by exactly one bit) will be scored $0$ for that test.

## Example

`xcopy.in`

`3 3`

`xcopy.out`

`5 4 6`

`1 0 2`

`9 8 10`

## Explanation

In this section, the subscript positioned at the bottom-right of the number represents the base in which it is written. For example, eight can be written as $8_{10} = 1000_2$

One of the optimal answers for the kids is given in the following table:

$0101_2 = 5_{10}$

$0100_2 = 4_{10}$

$0110_2 = 6_{10}$

$0001_2 = 1_{10}$

$0000_2 = 0_{10}$

$0010_2 = 2_{10}$

$1001_2 = 9_{10}$

$1000_2 = 8_{10}$

$1010_2 = 10_{10}$

We can see that between any two adjacent desks, the students' numbers in those desks differ by exactly one bit. The maximum value of the solution is $10$ and is the optimal answer. It is evident that there are other optimal answers - for example, the proposed solution but mirrored vertically or horizontally. One of the possible partial solutions where the maximum is $15$ is:

$0110_2$

$0111_2$

$0101_2$

$1110_2$

$1111_2$

$1101_2$

$1010_2$

$1011_2$

$1001_2$

This solution would be scored, according to the scoring formula, with $59.1\%$ of the test score.