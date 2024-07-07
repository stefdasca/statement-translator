Certainly! Here is the translated document:

---

In a distant land, the economy is in crisis. The biggest problem is the lack of capital which creates financial blockages. For example, a company $X$ may owe debts to a company $Y$ which it cannot pay because another company $Z$ owes debts to company $X$ which remain unpaid, and so on.

There is a list of all company debts in the following form: $X > Y \\ S$, meaning â€œcompany $X$ owes company $Y$ an amount $S$â€. It is possible that $X$ has multiple debts to company $Y$ (depending on the contracts concluded together) or even that $X$ owes debts to $Y$ and $Y$ has debts to $X$.

# Task

Given the list of company debts, write a program that solves the following tasks:

1. Determine the number of distinct companies that appear in this list;
2. Create a financial situation of the distinct companies in this list, written in lexicographical order; for each company, two values $SD \\ SP$ will be determined, where $SD$ represents the total amount of debts the company owes to other companies, and $SP$ is the total amount the company has to collect from other companies.

# Input data

The input file `datorii.in` contains on the first line a natural number $C$ representing the task to be solved ($1$ or $2$). The second line contains a natural number $D$ which represents the number of existing records in the list of company debts. On the next $D$ lines, the debts of the companies are described, in the specified format in the statement, one debt per line.

# Output data

The output file `datorii.out` will contain the answer to the task $C$ specified in the input file. If $C = 1$, the file will contain a natural number, representing the number of distinct companies that appear in the mentioned list. If $C = 2$, the file will contain for each of the distinct companies in the mentioned list a single triplet of the form $X \\ SD \\ SP$, where $X$ is the name of the company, and $SD$ and $SP$ have the significance from the statement for the company $X$; the triplets will be written so that the names of the companies appear in lexicographical order, each triplet on a separate line of the file, and $X$, $SD$ and $SP$ will be separated by a single space.

# Constraints and clarifications

* There are at most $6 \\ 000$ distinct companies in the mentioned list of debts.
* The name of a company is made up of a maximum of $20$ characters (uppercase and lowercase letters of the English alphabet, digits, spaces); a distinction is made between uppercase and lowercase letters in the names of companies; there are no other restrictions regarding the names of the companies.
* Two distinct companies have distinct names. A company cannot owe debts to itself.
* In the description of a debt ($X > Y \\ S$) there is a single space between $X$ and >, a single space between > and $Y$, and a single space between $Y$ and $S$.
* $1 \\leq D \\leq 80 \\ 000$;
* The amounts owed by companies are non-zero natural numbers $\leq 10^6$;
* If $X$ and $Y$ are the names of two distinct companies, and $k$ ($k \\geq 0$) is the maximum value with the property that the sequence formed by the first $k$ characters of $X$ is identical to the sequence formed by the first characters of $Y$, we say that $X$ lexicographically precedes $Y$ if $X$ has only $k$ characters or if the ($k + 1$)-th character of $X$ is smaller than the ($k + 1$)-th character of $Y$.
* For tests worth $30$ points, the task is $1$.
* For tests worth $60$ points, the task is $2$.
* For tests worth $40$ points, $D \\leq 1 \\ 000$.
* For tests worth $45$ points, the names of the companies do not contain spaces.

# Example 1

`datorii.in`
```
1
4
Vasile Inc > Anatolia 100
ana > Anatolia 10
ana > Vasilescu Inc 5
Popa25 PF > Anatolia 30
```

`datorii.out`
```
5
```

# Example 2

`datorii.in`
```
2
5
Vasile Inc > Anatolia 100
ana > Anatolia 10
ana > Vasilescu Inc 5
Popa25 PF > Anatolia 30
Popa25 PF > ana 50
```

`datorii.out`
```
Anatolia 0 140
Popa25 PF 80 0
Vasile Inc 100 0
Vasilescu Inc 0 5
ana 15 50
```

---

I have double-checked and fixed any grammatical or syntactical errors according to the rules of the English language.