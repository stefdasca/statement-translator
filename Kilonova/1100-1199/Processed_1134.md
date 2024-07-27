The manager of a music band needs to receive offers for concerts and possible cancellations of concerts from different cities. The cities are coded with the numbers $1, 2, \dots, n$ and each city can host at most one concert. The manager keeps in touch with the concert organizers in these cities and constantly updates the obtained data. Via fax, he receives $m$ messages, which can be of one of the two types: $D \\ nr$ or $N \\ nr$.

With the following meanings: for the first message, the organization of a concert in city $nr$ is desired, while for the second message, the cancellation of the concert in city $nr$ is desired. A message is made up of exactly two lines.

Task:
1. Display the cities where the music band will perform (on the same line with a space between them).
2. Display the city (or cities if there are several, on the same line with a space between them) where the organizers are the most undecided (i.e., they have canceled and proposed organizing a concert in their city the most times).
3. Display the number of cities that did not send any message to the manager.

# Input data

The first line of the input file `turneu.in` contains two integers, $n$ and $m$, representing the number of cities and the number of messages.

On the next $m$ lines are pairs of the form $D \\ nr$ or $N \\ nr$ with the meaning from the statement.

# Output data

The first line of the output file `turneu.out` will contain the cities where the music band will perform (on the same line with a space between them), in ascending order.
The second line will contain the cities with the maximum number of changes, in ascending order of the city number.
The third line will contain the number of cities that did not send any message to the manager.

# Constraints and clarifications

* $1 \leq n, m \leq 100\ 000$;
* The tests and constraints have been redone.
* It is guaranteed that no concert which was not organized will be canceled, and that a concert that has already been announced will not be announced again.

# Example 1

`turneu.in`
```
5 6
D 2
D 3
N 3
D 3
D 5
N 2
```

`turneu.out`
```
3 5 
3 
2
```