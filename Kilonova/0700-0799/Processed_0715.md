Sinbad the Sailor dreams that he is in a cave filled with treasures. Everywhere, there are chests full of jewels and gold coins, and the cave is illuminated by their shine. As Sinbad marvels at all the splendors around him, a mysterious voice says:

> There is a way to reach here, and if you succeed, all these treasures will be yours. This cave is at the top of Mount Ararat, but on the way, evil spirits will try to stop you. You must fight and defeat them in fair combat. To open the cave, you must remember how many spirits you have defeated and loudly recite the magic formula.
> The magic formula is the smallest number that has both the first digit and the number of digits equal to the number of evil spirits you have defeated. But beware! This number must also have the property that any sequence of two consecutive digits must be different prime numbers.

At this moment, Sinbad wakes up and wants to go in search of the treasure. He is not afraid of the evil spirits, but he knows how many calculations the search for the magic formula requires (and he knows he is not very good at math). Therefore, he asks you to help him.

# Task

Sinbad will tell you the number $n$ (representing the number of evil spirits he has defeated), and you need to tell him the magic formula. If there is no such number, tell Sinbad that it was just a dream and that it's time to get ready for school.

# Input data

The input file `visul.in` will contain $n$.

# Output data

The output file `visul.out` will contain a single natural number, namely the one requested by the problem. If there is no solution, the message `Nu exista` will be printed.

# Constraints and clarifications

* $1 \\leq n \\leq 10$;

# Example 1

`visul.in`
```
3
```

`visul.out`
```
311
```

## Explanation

In the example, $311$ is displayed because: $31$ is a prime number, and $11$ is a prime number.

# Example 2

`visul.in`
```
1
```

`visul.out`
```
Nu exista
```