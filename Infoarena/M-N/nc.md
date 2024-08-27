## Task

A $text$ consisting of both uppercase and lowercase letters of the English alphabet, as well as punctuation marks: $,$ (comma), $.$ (period), $!$ (exclamation mark), $?$ (question mark), and $\dots$ (ellipsis) is given. The $text$ can span multiple lines. We know that a $sentence$ ends with one of the punctuation marks $.$, $?$ , $!$, or $\dots$. We want to determine how many $sentences$ there are and how many $words$ each $sentence$ contains. Since the $text$ is in an unofficial language, $words$ can start with a lowercase $letter$ and can contain uppercase $letters$ inside or at the end. Note that $words$ can be separated by any number of $spaces$ and there can be $spaces$ at the beginning and end of $sentences$.

## Input data

The $text$ is located in the $input$ $file$ `nc.in`.

## Output data

In the $output$ $file$ `nc.out`, the first line will contain a $number$ $N$ representing the $number$ of $sentences$ in the $text$, and each of the following $N$ $lines$ will contain one $number$, so that at the $(i+1)$ -th $line$, the $number$ of $words$ contained in the $i$ -th $sentence$ will be printed.

## Constraints

The $text$ will contain a maximum of $1000$ $lines$

Each $line$ will have at most $4000$ $characters$

Each $line$ ends with an $end-of-line$ $character$.

## Example

`nc.in`

De sarbatori, codeaza alaturi de cei dragi! La UniBuc FMI, cea mai cool faCOOLtate. Esti  pregatit  ? te asteptam alaturi de noi... FMI RullZ!

`nc.out`

5
7
7
2
5
2