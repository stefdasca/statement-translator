```markdown
# Task

Upset due to the economic crisis, Don Stefano has decided to take up gambling, specifically roulette. His plan is as follows: enter the casino with $X$ lei, place bets, and if he reaches $0$ lei or at least $Y$ lei (where $Y$ is a number determined by Don Stefano), he stops betting and goes home. Don Stefano has decided to play at $2$ roulette tables simultaneously, betting $2$ lei each minute, one at each roulette table. The two roulette tables are identical, half of the slots on one roulette being red, and half blue.

Wanting to have as many options as possible, Don Stefano will ask $T$ questions in the form: "If I enter the casino with $X$ lei and stop either at $0$ lei or at least $Y$ lei, what is the probability of going home with at least $Y$ lei?"

# Input data

The first line of the file `cazino.in` contains $T$, the number of questions. The following $T$ lines each contain two numbers, $X_i$ and $Y_i$, with the significance given in the statement.

# Output data

The file `cazino.out` will contain $T$ lines, with the $i$-th line containing the answer to question $i$.

# Constraints and clarifications

* $1 \leq T \leq 100 \ 000$
* $1 \leq X \leq Y \leq 1 \ 000 \ 000$
* The answer must be displayed to $5$ decimal places.

# Example

`cazino.in`
```
3
5 10
1 5
123 4412
```

`cazino.out`
```
0.40000
0.00000
0.02765
```
```