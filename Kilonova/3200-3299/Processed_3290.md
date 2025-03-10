> _The Carpathian protozoic laser of the Getodacians would surely defeat the positronic gamma particle field of the samurais._  
> -- OTV

After you repaired your time machine, you decided that the first stop should be Dacia, the famous and sacred land of your Dacian ancestors. Once you step out of the machine after entering the coordinates, you realize you have arrived in the Great Square of the former capital, Sarmizegetusa, on the day of all Dacian saints. According to your knowledge, on this holiday, the famous Dacian Dance is always performed. Being present at such a performance, you deduced that it operates in the following manner:

$N$ heroes gather in a circle, each with a number from 1 to $N$ inscribed on their forehead. Initially, these numbers are in order (see Constraints and clarifications). Then, a series of dance steps are performed according to the sacred sequence $a_0, a_1, \dots, a_{K-1}$, with the hero numbered 1 holding a baton.

At step $x$, the following things happen in order:
* Let $i = (x \textrm{ mod } K)$, which is the remainder of dividing $x$ by $K$.
* This happens $a_i$ times: the hero holding the baton will pass it to the person on their right and will exit the circle to be sacrificed to Zalmoxis. If there is only one hero left at this step, they will symbolically pass the baton to themselves and then also exit the circle. If this process cannot be repeated $a_i$ times because all heroes have left, the dance will end here.
* After removing a sacrificed hero, the circle rearranges so that all remaining heroes form a new compact circle. The remaining heroes maintain their initial relative order among themselves.
* Then, the baton is passed to the right $a_i$ times **without the heroes leaving the circle**.
* The baton passing continues in the next step.

It is well known that the Dacians were the founders of modern programming, so they always began this dance from step $0$.

After witnessing this incredible performance, you decided to ask a villager next to you a few questions about the dance, which come in two varieties:

1. In what position is the person with ID $P$ eliminated?
2. What is the ID of the $P$-th person eliminated?

# Task

After you asked the questions to the villager, they responded to you with a single word in old Dacian, which you predict could answer all your questions. However, your ear is not trained to understand this language of the gods, so you are left wondering what the answers to these questions could be.

# Input data

The first line contains the natural numbers $N$ and $K$, representing the number of heroes in the initial circle and the length of the sacred sequence.

The second line contains $K$ natural numbers $a_0, a_1, a_2, \dots, a_{K-1}$, the elements of the sacred sequence.

The third line contains the natural number $Q$, the number of questions you ask.

The next $Q$ lines contain the components of the questions. Thus, each line will contain two natural numbers $T$ and $P$, representing the type of the question and its parameter.

# Output data

The $Q$ lines will contain the answers to the questions in order.

# Constraints and clarifications

* **Note:** A [video clip](HeroDance.mp4) that illustrates what happens in the example below is attached to this problem.
* $1 \le N \le 10^9$;
* $1 \le K \le 10^5$;
* $1 \le Q \le 10^5$;
* $1 \le a_i, P \le N$, for $0 \le i < K$;
* $1 \le T \le 2$;
* The initial order is defined as follows:
  * The left neighbor of the person with number $i$ inscribed is the one with number $i - 1$, and the right neighbor is the one with number $i + 1$ for $2 \le i \le N - 1$.
  * The left neighbor of the person with number $1$ inscribed is the one with number $N$, and the right neighbor is the one with number $2$.
  * The left neighbor of the person with number $N$ inscribed is the one with number $N - 1$, and the right neighbor is the one with number $1$.

|#| Score | Constraints | 
|-|---------|------------|
|1|    2    | $N \le 20$ |
|2|    3    | $N \le 10^3$ |
|3|   10    | $N \le 10^6$ |
|4|   14    | $K = 1$, $a_0 = 1$ and $T = 1$ for any question  |
|5|   16    | $K = 1$, $a_0 = 1$ and $T = 2$ for any question |
|6|   18    | $T = 1$ for any question |
|7|   20    | $T = 2$ for any question |
|8|   17    | Without additional constraints |

# Example

`stdin`
```
12 2  
2 1  
12  
1 1  
1 2  
1 3  
1 4  
1 5  
1 6  
1 7  
1 8  
1 9  
1 10  
1 11  
1 12
```

`stdout`
```
1  
2  
7  
8  
3  
10  
4  
5  
11  
9  
6  
12
```

## Explanation

The first hero is eliminated first, the second hero is eliminated second, the third hero is eliminated seventh, the fourth hero is eliminated eighth, the fifth hero is eliminated tenth, the sixth hero is eliminated fourth, the seventh hero is eliminated fifth, the eighth hero is eliminated eleventh, and the ninth hero is eliminated ninth. And so on.