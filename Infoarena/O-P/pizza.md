# Pizza

Alice and Bob met again after a long time at a pizzeria in eastern Taiwan. Since neither of them wanted to eat an entire pizza, they decided to order a special pizza. This pizza has the property that it is divided into $N$ triangular slices of different sizes. To avoid specifying that a certain slice represents $x\%$ of the entire pizza, the chef wrote with sauce on each slice a natural number greater than $0$, thus approximating this percentage. More precisely, in this case, a slice marked with the value $10$ will be twice as large as a slice marked with the value $5$.

## Task

Since Alice and Bob are big fans of pizza, they want to individually eat as much pizza as possible. Because this type of pizza is special, they created certain rules to make the game fair. They each eat one slice of pizza alternately. Alice is the one who chooses where to take the first slice from. After Alice extracts the first slice, each of them is only allowed to choose a slice adjacent to the previously extracted portion of the pizza. Each of the two children will want to eat as much pizza as possible, so each will have an optimal strategy for extracting slices to eat the maximum possible amount of pizza. By the amount of pizza eaten by one of the children, it is understood as the sum of the values on the extracted pizza slices. The chef is very interested in this game and asks you to calculate the maximum value that both Alice and Bob can extract if both play optimally and to tell them the difference between the value obtained by Alice and the value obtained by Bob.

## Input data

The input file `pizza.in` contains on the first line the value $N$ representing the total number of slices. The next line will describe the configuration of the pizza slices. Specifically, $N$ natural numbers greater than $0$ will be read, representing the values written on $N$ consecutive pieces of pizza (the first slice is chosen at random). It should be noted that on the pizza crust, the $N$-th slice read is before the first slice read.

## Output data

The output file `pizza.out` will contain a single integer representing the difference between the value obtained by Alice and the value obtained by Bob.

## Constraints

$2 \leq N \leq 5000$

$1 \leq X_i \leq 10000$, where $X_i$ represents the value written on the $i$-th slice of pizza

Remember that Antonio and Antonia love pizza!

## Example

`pizza.in`
```
7
7 8 3 10 2 5 7
```

`pizza.out`
```
8
```

## Explanation

Each child will play optimally so that the following pizza slices are extracted in turn:

Alice: Slice with the value $10$

Bob: Slice with the value $2$

Alice: Slice with the value $5$

Bob: Slice with the value $7$

Alice: Slice with the value $7$

Bob: Slice with the value $8$

Alice: Slice with the value $3$

Alice extracts slices with a total value of $25$, and Bob extracts slices with a total value of $17$. The difference between the sum obtained by Alice and Bob is $25 - 17 = 8$.