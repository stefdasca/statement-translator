Disappointed by the Siragul business, Lunasorab decided to go on vacation to Paris. He decided to try new things, such as visiting an art gallery. The gallery has several types of paintings, but the ones that interest Lunasorab the most are the oil paintings (since he was a child, he liked to change the oil in the car). The gallery is formed by $N$ rooms that communicate with each other through $M$ corridors, and the oil paintings are found only on corridors, one on each corridor. Each painting is done with a specific type of oil. Since he doesn’t do things by half, Lunasorab would like to see all the oil paintings. Since this is his first visit to the museum, he wants to see each painting exactly once (when he passes through a corridor, Lunasorab sees the painting located there). Also, to avoid boredom, he does not want to see two consecutive paintings that use the same type of oil and doesn’t want to end the visit with a painting done with the same type of oil as the first painting he saw. He cannot pass from one room to another except through the corridor that connects them and will pass through each corridor exactly once. Also, the sequence of corridors covered does not contain $2$ consecutive paintings done with the same type of oil. Moreover, the type of the first painting seen must be different from the type of the last painting visited. The visit starts and ends in the same room.

Therefore, he asks for your help, promising you a part of the profit from his next business. To make sure you don’t trick him, he will provide you with several gallery plans, ultimately choosing the one he likes the most.

# Task

Given the gallery plan, find a sequence of corridors through which Lunasorab can pass. 

# Input data

The input file `ulei.in` will contain on the first line the natural number $T$, representing the number of tests. The next lines will contain $T$ tests, described as follows. Each test consists of $M + 1$ lines. The first line will contain $N$ and $M$, representing the number of rooms and the number of corridors. On the next $M$ lines, the corridors will be found, one per line, given as $i \\ j \\ t$, meaning there is a corridor from room $i$ to room $j$, containing a painting that uses type $t$ of oil. Corridors are bidirectional, and there can be at most one corridor between the same pair of rooms.

# Output data

The output file `ulei.out` will contain $T$ lines. On each line, there is a sequence of $M + 1$ natural numbers separated by a space, representing the room numbers in the order of the visit.

# Constraints and clarifications

* $1 \\leq T \\leq 5$
* $1 \\leq N \\leq 15 \\ 000$
* $1 \\leq M \\leq 100 \\ 000$
* There will be no corridor from a room to itself
* There will always be a solution in the test cases used for evaluation
* The oil types will be between $1$ and $15 \\ 000$
* For $20\\%$ of the tests, there will be only $2$ types of oil

# Example 1

`ulei.in`
```
1
3 3
1 2 1
2 3 2
3 1 3
```

`ulei.out`
```
1 2 3 1
```

## Explanation

Lunasorab starts the visit in room $1$, continues with rooms $2$ and $3$, finally returning to room $1$. Thus, he visited all the paintings and didn’t get bored.

