The NASA researchers installed a seismograph on Mars, which recorded the movements at the planet's surface. The seismograph sent a signal to Earth each second out of the $N$ seconds that define the analyzed time period. The signal was coded by researchers as $1$ if the seismograph detected movement and $0$ if no movement was recorded at the planet's surface. Therefore, a quake on Mars was defined by researchers as a continuous period during which the seismograph sent, second by second, a coded signal of $1$, starting after at least two signals coded with $0$, and ending when at least two signals coded with $0$ were recorded.

# Task

Knowing the sequence of the $N$ values sent in order by the seismograph, write a program that determines:

1. The maximum duration, in seconds, of a quake;
2. The number of quakes that occurred during the analyzed time period;
3. Due to a technical error, the seismograph transmitted incorrectly for a continuous period of time. Therefore, in the initial sequence consisting of the $N$ signals, we need to replace the value $0$ with the value $1$ in a single non-empty subarray of adjacent zero elements. Analyzing all possibilities of making this modification, determine the maximum duration of a quake that results after modifying the initial sequence of signals.

# Input data

The input file `seism.in` contains on the first line a natural number $C$ which can have the values $1, 2$ or $3$ and represents the number of the task.

The second line contains a natural number $N$ having the meaning described in the statement.

The next line contains $N$ natural numbers separated by a space, representing the coding of the signal sent by the seismograph, from second to second, starting with second $1$ and until second $N$.

# Output data

The output file `seism.out` will contain on the first line a single natural number representing the result determined according to the task.

# Constraints and clarifications

* $5 \leq N \leq 100\ 000$;
* A quake lasts between $1$ and $N - 4$ seconds;
* For tasks $1$ and $2$, it is guaranteed that the seismograph detected at least one quake.
* For task $3$, it is guaranteed that there is at least one non-empty subarray of elements equal to $0$ that can be changed to $1$ to have at least one quake in the entire sequence.
* Correctly solving the first task earns $40$ points, correctly solving the second task earns $40$ points, and correctly solving the third task earns $20$ points.

# Example 1

`seism.in`
```
1
21
0 0 1 1 1 1 0 0 0 0 0 1 0 1 0 0 1 1 0 0 1
```

`seism.out`
```
4
```

## Explanation

The maximum duration of a quake is $4$ seconds.

# Example 2

`seism.in`
```
2
21
0 0 1 1 1 1 0 0 1 0 0 1 0 1 0 0 1 1 0 0 1
```

`seism.out`
```
3
```

## Explanation

The seismograph recorded $3$ quakes. The first quake lasts for $4$ seconds, the second lasts for $1$ second, and the last one lasts for $2$ seconds.

# Example 3

`seism.in`
```
3
8
0 0 1 1 0 1 0 0
```

`seism.out`
```
4
```

## Explanation

The element at position $5$ in the sequence is changed to $1$, and a quake lasting $4$ seconds is obtained.

# Example 4

`seism.in`
```
3
14
0 1 1 0 0 0 0 0 0 0 0 0 1 0
```

`seism.out`
```
5
```

## Explanation

Change to $1$ the signals associated with seconds $6, 7, 8, 9$, and $10$ and a quake lasting $5$ seconds is obtained.