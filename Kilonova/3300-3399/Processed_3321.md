
# Task

Alex and Bogdan were bored during their computer science class, so they started to play a numbers game. In this game, Bogdan wrote on a sheet a sequence of $N$ numbers, with values ranging between $0$ and $K - 1$, and asked Alex to choose a property that the sequence should satisfy. If the sequence satisfies the chosen property, then Alex wins the game; otherwise, Bogdan is declared the winner.

After some thinking, Alex chooses the following property: "The sum of any subarray of Bogdan's written sequence whose length is a prime number must be divisible by 3." Alex is unsure about how good his choice was, so he asks you to determine the number of sequences Bogdan could have written that satisfy the property he chose.

# Input data

The first line contains the two values, $N$ and $K$, with the meaning given in the statement.

# Output data

The first line should contain the answer to the task, namely the number of different sequences Bogdan could have written. Since this number can be very large, it should be printed modulo $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000 \ 000$;
* $1 \leq K \leq 1 \ 000 \ 000 \ 000$;

# Example

`stdin`
```
2 4
```

`stdout`
```
6
```

## Explanation

The sequences that Bogdan could have chosen are as follows:
- $0 \ 0$;
- $0 \ 3$;
- $1 \ 2$;
- $2 \ 1$;
- $3 \ 0$;
- $3 \ 3$.

```
