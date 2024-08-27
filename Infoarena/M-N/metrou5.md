# Metrou5

In the kingdom of Smecherie, the metro network is very generous, also having its fair share of hooligans. Being a kingdom like that of Verde-Imparat or at least like that of his less clever brother, Ros-Imparat, hooliganism is a daily occurrence. One day, a hooligan goes to the metro and sees a sequence of natural numbers with values between $1$ and $K$ written on the platform. Evidently, his uncontrollable behavior compels him to tear everything he sees. Later, looking at the remnants of the sequence, he wonders in how many ways he can complete it with numbers between $1$ and $K$ so that the obtained sequence is non-decreasing.

## Task

Given a sequence of $N$ numbers with values between $1$ and $K$ and some missing values (marked with $-1$ in the sequence), you have to say in how many ways modulo $1.000.000.007$ the missing positions can be filled with numbers still between $1$ and $K$ such that the obtained sequence is non-decreasing (note, not strictly increasing).

## Input data

The input file `metrou5.in` will contain on the first line two natural numbers, $N$ and $K$. The second line will contain $N$ values, namely the elements of the initial sequence or $-1$ if they were torn by the hooligan.

## Output data

The output file `metrou5.out` will contain the required number.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq K \leq 100\ 000$

$1 \leq value_i \leq K$ or $value_i$ is $-1$ if the number at position $i$ is hidden

## Example

`metrou5.in`

$6 \ 5$

$-1 \ -1 \ 1 \ -1 \ -1 \ -1$

`metrou5.out`

$35$