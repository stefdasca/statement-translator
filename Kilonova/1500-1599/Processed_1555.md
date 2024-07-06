# The $N$ students participating in the olympiad were invited to admire the city panorama from the Ferris wheel with $N$ seats installed in the Children's Town. Each student is wearing a T-shirt with a natural number, the numbers on the T-shirts being different two by two and having values between $1$ and $N$. Initially, they occupy all the $N$ seats of the wheel, starting with the lowest seat and continuing with the next seats, in a clockwise direction.

The wheel moves circularly, in a clockwise direction, with a number of positions, stops and the student sitting on the lowest seat disembarks. Next, it rotates in the same direction, a **bigger** number of positions, then stops, and the student sitting on the lowest seat disembarks, and so on until all students have disembarked.

# Task

Given the number $N$ of students, as well as the numbers on the T-shirts, in the order in which the students are initially on the wheel, determine $N$ numbers representing the positions by which the wheel moves circularly for each student to disembark, so that the students disembark from the wheel in increasing order of the numbers on their T-shirts.

The $N$ position numbers must be in strictly increasing order, and the total number of positions must be minimal.

# Input data

From the file `roata.in`, the first line contains $N$, representing the number of students, and the second line contains $N$ distinct natural numbers, separated by a space, representing the numbers on the T-shirts.

# Output data

In the file `roata.out`, $N$ strictly increasing numbers will be written, representing the required position numbers.

# Constraints and clarifications

* $2 \leq N \leq 50\ 000$;
* For $50\%$ of the score, $2 \leq N \leq 1\ 000$;
* If initially, the student with the T-shirt number $1$ is on the lowest seat of the wheel, he will disembark after the wheel moves $N$ positions and reaches the lowest seat again.

# Example

`roata.in`
```
6
6 1 3 4 5 2
```

`roata.out`
```
5 8 9 11 17 22
```

## Explanation

~[roata_0.png]

Initially, the students are seated in a clockwise direction, starting with the student with T-shirt $6$, who occupies the lowest seat.

~[roata_1.png]

1) By rotating $5$ positions clockwise, the student with T-shirt $1$ reaches the lowest seat and disembarks.

~[roata_2.png]

2) By rotating $8$ positions clockwise, the student with T-shirt $2$ reaches the lowest seat and disembarks.

~[roata_3.png]

3) By rotating $9$ positions clockwise, the student with T-shirt $3$ reaches the lowest seat and disembarks.

~[roata_4.png]

4) By rotating $11$ positions clockwise, the student with T-shirt $4$ reaches the lowest seat and disembarks.

~[roata_5.png]

5) By rotating $17$ positions clockwise, the student with T-shirt $5$ reaches the lowest seat and disembarks.

~[roata_6.png]

6) By rotating $22$ positions clockwise, the last student, with T-shirt $6$, reaches the lowest seat and disembarks.