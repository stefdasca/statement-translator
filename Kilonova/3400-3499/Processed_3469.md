Gigel wants to buy subscriptions from $N$ companies. Each company offers three types of subscriptions (Gigel cannot buy more than one subscription from a single company). Gigel assigns each subscription a score based on how useful it is in his daily life.

The starter subscription of company $i$ costs $0$ coins and has a score of $a_i$, the standard subscription costs $1$ coin and has a score of $b_i$, while the premium subscription costs $2$ coins and has a score of $c_i$.

## Task

Since Gigel is going to the casino tonight, he doesn’t know how many coins he will have left to purchase subscriptions. Therefore, he asks $Q$ questions, each specifying the number of coins he might have left after his night at the casino. Help Gigel determine the maximum sum of subscription scores he can achieve from the $N$ companies for each scenario.

## Input data

The first line contains two integers, $N$ and $Q$.  
The second line contains $N$ integers representing the array $a$.  
The third line contains $N$ integers representing the array $b$.  
The fourth line contains $N$ integers representing the array $c$.  
The next line contains $Q$ integers $K_i$, each representing the number of coins Gigel wants to spend on subscriptions.

## Output data

The output consists of $Q$ integers on a single line, where the $i$-th number represents the answer to the $i$-th question.

## Constraints and clarifications

$\textcolor{red}{Attention!}$ Due to the large amount of input and output data, we recommend adding the following lines of code at the beginning of the `main` function:
```cpp
ios_base::sync_with_stdio(false);
cin.tie(0);
cout.tie(0);
```

- $1 \leq N \leq 300 \ 000$
- $1 \leq Q \leq 2 \cdot N$
- $1 \leq K \leq 2 \cdot N$
- $0 \leq a_i \leq b_i \leq c_i \leq 10^9$
- Gigel buys exactly one subscription from each company.

### Scoring

| Subtask | Points | Constraints                     |
|---------|--------|---------------------------------|
| 1       | 21     | $N \leq 3 \ 000$               |
| 2       | 16     | $b_i = c_i$ for each $i$       |
| 3       | 23     | $K \leq 10 \ 000$              |
| 4       | 18     | $Q = 1$                        |
| 5       | 22     | No additional constraints      |

## Example

**Input**
```plaintext
4 3
2 2 1 0
8 3 2 1
9 7 3 12
1 3 6
```

**Output**
```plaintext
11 
23 
29
```

## Explanation

We will explain the answer for the second question $(K = 3)$:

| #  | Company 1     | Company 2     | Company 3     | Company 4     |
|----|---------------|---------------|---------------|---------------|
| Starter | 2         | $\textcolor{red}{2}$  | $\textcolor{red}{1}$  | 0             |
| Standard | $\textcolor{red}{8}$  | 3             | 2             | 1             |
| Premium  | 9         | 7             | 3             | $\textcolor{red}{12}$ |

Gigel will buy the standard subscription from the first company, the starter subscription from the 2nd and 3rd companies, and the premium subscription from the 4th company. The sum of the scores of these subscriptions is $8 + 2 + 1 + 12 = 23$.