Certainly! Here is the translated statement with the specified format:

---

You have no idea how difficult it is to be a clerk. Tens of reports to compile, hundreds of requests to draft, thousands of signatures, hundreds of thousands of papers to file. The endless circuit of paperwork is known as bureaucracy. In our institution, there are $N$ clerks, numbered from $1$ to $N$. Each of them has to register a considerable number of documents. This is why every day, from the earliest hour, the clerks line up at the secretariat, in order from $1$ to $N$. The method of document registration is as follows: the clerk stands in line, waits until their turn comes, registers **a single** document, then, if they have more documents, they line up again, and so on. Unfortunately, the secretariat can register at most $M$ documents in one day.

# Task

If it is known, for each of the $N$ clerks, the number of documents they have to register at the secretariat, determine the numbers of the clerks who did not manage to sign all their documents by the end of the workday.

# Input data

The file `birocrat.in` contains in the first line two integers $N$ and $M$ with the meaning from the statement ($N$ – the number of clerks, $M$ – the maximum number of documents registered by the secretariat in one day), and on the second line $N$ natural numbers $a[i]$ $(1 \leq i \leq N)$, separated by a space, representing the number of documents that each clerk needs to register, in order from $1$ to $N$.

# Output data

The file `birocrat.out` contains on a single line the numbers of all clerks who remained unresolved as they are found in line at the end of the workday, from the first unsolved to the last. If at the end of the day all clerks have signed all their documents, the output file will contain the value $0$.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $0 < M < 10^{14}$;
* $1 \leq a[i] \leq {10}^{9}$;
* The total number of documents for all clerks can be represented on `long long` $( < {10}^{18})$

# Example 1

`birocrat.in`
```
5 10
2 4 1 3 2
```

`birocrat.out`
```
4 2
```

## Explanation

Initially, a queue was formed with the following clerks $\\{1,2,3,4,5\\}$. After the first round of all clerks at the secretariat, $5$ documents were registered, and in the queue remained clerks $\\{1,2,4,5\\}$ in that order. After the second round, $4$ more documents were signed, and in the queue were clerks $\\{2,4\\}$ again. Clerk $2$ registers the document and stands back in line, after which the secretariat closes.

# Example 2

`birocrat.in`
```
3 6
1 2 1
```

`birocrat.out`
```
0
```

