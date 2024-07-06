> Very long, Florinel Coman... Go, Florineeeeeel!

# Task

Paul is a unique boy whose main activities are watching anime and football. Recently, he realized that he has come to know the intricacies of Japanese animated cartoons so well that he can finally use them productively; specifically, he wants to direct his own anime.

Paul's anime focuses on Romania's qualification for the 2024 European Football Championship. Thus, the main characters are $2n + 1$ football teams numbered from $1$ to $2n + 1$. Since he is at the beginning of the scenario design and still does not know how Romania will rank in the European Championship, Paul starts by writing about the group stage. All these $2n + 1$ football teams belong to the same group — the one that includes Romania, of course.

Paul forgot that any football match in the qualifying stages also has a return match; thus, he will write only one episode for each pair of two teams. Since Paul forgot that there could be draws, every match in the anime will end with the victory of one of the teams, with no option for a draw. In total, Paul will write $N \cdot (2 \cdot N + 1)$ episodes.

An anime is not complete without a rating, and Paul wants his anime to have as low a rating as possible and an inconsistent story, because, as we all know, the best animes are always at the bottom of the rankings. Thus, the inconsistency of the story is defined as the number of distinct team triplets $(i, j, k)$ for which, in Paul's scenario, team $i$ will win against team $j$, team $j$ will win against team $k$, and team $k$ will win against team $i$.

Help Paul write the worst possible anime by telling him how each episode should end!

Formally, let $n$ be a natural number. Display a binary matrix (a matrix containing values of $0$ or $1$) with $2n + 1$ rows and $2n + 1$ columns, which respects the following properties:

* $A[i][j] \neq A[j][i]$ for any $i \neq j$;
* the number of triplets $(i, j, k)$ with $i \neq j \neq k$, for which $A[i][j] = A[j][k] = A[k][i] = 1$, is maximized.

# Input data

The first line contains a single integer $n$.

# Output data

Print $2n + 1$ rows. On the $i$-th row, you will find a string of length $2n + 1$, representing the concatenation of the values on the $i$-th row of matrix $A$.

# Constraints and clarifications

For all tests, $1 \leq n \leq 1\ 000$. Furthermore, for $42$ points, it is guaranteed that $n \leq 100$.

For each test, your solution will be scored based on the optimal solution. Let $S_{o}$ be the maximum number of triplets and $S_{c}$ the number of triplets in the given solution for a certain test. We denote by $x = S_{c}/S_{o}$. The score obtained on that test is:

$ \displaystyle \text{score}_{test} \cdot \min\left(\frac{2e^{2x}}{e^2 + e^{x + 1}} \times (0.8 x^{400} + 0.2 x), 1\right)$

# Example

`stdin`
```
1
```

`stdout`
```
001
100
010
```

