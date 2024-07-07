# Task

Gigel is a very greedy boy. He has $N$ stacks at home, each containing $M$ boxes of candies. At the beginning of each day, Gigel takes a single box from the top of one of the stacks and instantly eats all the candies in it, after which he throws it away (since a candy box without candies in it depresses him). He performs this activity (eating all the candies in the box from the top of a stack) every day until all the stacks are empty. Gigel would be very happy if the number of candies in each box would remain constant until he reaches that box to eat the candies. However, reality does not match Gigel's desires. Each candy box is characterized by two parameters: $Z$ and $B$. Initially (at the beginning of the first day), the box contains $Z \cdot B$ candies. At the end of each day, the number of candies in the box decreases by $B$. After $Z$ days, the number of candies in the box becomes $0$. When the number of candies in a box becomes $0$, something spectacular happens: the box disappears, and all the candy boxes above it, if it is not at that moment, the box at the top of the stack it is in, move down by one position in the stack; if it is at the top of the stack but is also the last box in the stack, then the stack is emptied; if it is at the top of the stack and the stack contains other candy boxes, then the box below it becomes the new top box of the stack (if this box also disappears on the same day, the box below this one is considered, and so on).

# Task

Given the number of stacks, the number of candy boxes in each stack, and the parameters $Z$ and $B$ for each candy box, determine the maximum total number of candies that Gigel can eat.

# Input data

The first line of the input file `bombo.in` contains the integers $N$ and $M$. The following $N$ lines contain $M$ pairs of numbers, describing the candy boxes in each stack, from the base to the top of the stack. Such a pair contains the numbers $Z$ and $B$, having the meaning specified above. Any two numbers on the same line in the input file are separated by a single space.

# Output data

In the file `bombo.out`, print a single number, representing the maximum number of candies that Gigel can eat.

# Constraints and clarifications

* $1 \leq a, b \leq 1\ 000 \ 000$;
* $1 \leq N \leq 4$;
* $1 \leq M \leq 10$;
* For each candy box:
  * $1 \leq Z \leq 50$;
  * $1 \leq B \leq 1000000$;
* At least 30% of the test files will have $N \leq 2$
* At least 65% of the test files will have $M \leq 6$
* At least 55% of the test files will have for each candy box $Z > N \cdot M$ 

# Example 1

`bombo.in`
```
2 3
50 1000 1 3 1 100
2 3000 1 10 1 20
```

`bombo.out`
```
51100
```

# Example 2

`bombo.in`
```
4 6
3 1 2 2 3 3 2 4 2 5 2 6
2 1 3 2 2 3 3 4 1 5 3 6
1 1 2 2 2 3 2 4 3 5 1 6
2 1 2 2 3 3 2 4 2 5 2 6
```

`bombo.out`
```
32
