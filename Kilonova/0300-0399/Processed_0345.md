
Pepi is an outstanding student studying Computer Science in Bucharest. In his year the total number of students is $2^N$ . Because Pepi cares a lot about his fellow students he doesn't bother remembering their names but he has assigned everyone, including himself, an ID from $0$ to $2^N - 1$.

The students in Pepi's year have organized a charitable event for the Ukrainian people where every student came dressed in $1$ of $2$ colors, either yellow or blue (it is possible that everyone wore only one of the $2$ colors). Unfortunately, Pepi forgot how everyone was dressed but he desperately wants to remember.

Because Pepi is a good judge of the human mind he remembers that any student $S1$ talked to one of his classmates $S2$ if and only if their ID differ by $1$ bit (in their binary representation). Also, Pepi is sure that any student $S1$ did not talk to more than $\lceil \sqrt{N} \rceil$ classmates that wore the same color as $S1$. Pepi remembers clearly the fact that the number of students that wore yellow was not equal to the number of students that wore blue.

Because this problem is a trivial one for Pepi he requests that you find any possible way that he and his friends were dressed at the event.

# Task

On the first line, there is one number $N$ ($1 \leq N \leq 22$) that has the meaning from the problem statement.

# Output

On a single line, there have to be printed $2^N$ values. These represent the colors Pepi and his classmates wore during the event, taking into account all the conditions Pepi remembers.

To simplify this problem the colors will be encoded: $0$ meaning yellow and $1$ meaning blue. A value found at the position $i$ in the output string represents the color that the student with the ID $i-1$ wore during the event (the first value from the output string is the color that the student with ID $0$ wore).

If there is more than one solution print any of them.

# Example

`stdin`
```
1
```

`stdout`
```
11
```

Explanation
---

There are $2$ students with IDs ranging from $0$ to $1$. The student with the ID $0$ talks only with the student with ID $1$ and he doesn't talk to more than $\lceil \sqrt{1} \rceil = 1$ students dressed with the same color as him.

The number of students dressed in yellow is not equal to the number of students dressed in blue. So, a possible way that the students were dressed would be blue and blue ($11$). Of course, yellow, yellow ($00$) is another great solution.
