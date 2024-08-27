# Tygyn

One of Marcel's ancestors, Manchaary, son of Nyurgun and Sahayaana, was one of the servants of Tygyn Darkhan at the beginning of the 17th century. Tygyn Darkhan, the great leader who unified the Yakutian tribes, seemed to have been very passionate about Number Theory. One day, he assigned a distinct natural number from 2 to $M$ to his $N$ cows. He thought about grouping the cows, based on the numbers assigned to them, into a minimum number of herds. However, he established the following conditions, which must be satisfied for all herds:

Let $x$ be the smallest number assigned to the cows in a herd. Each cow in the same herd must have a number of the form $x * k$, where $k$ is a natural number. All prime divisors of $k$ (apart from 1) must be greater than or equal to any prime divisor of $x$ for all cows in the herd.

However, Tygyn is a bit busy maintaining peace in his territory, so he asked Manchaary to take care of the cows. This task seemed quite difficult for Manchaary, but the reward was wonderful: he could marry the beautiful Sardaana! We know the end of the story: Manchaary solved the task and Sardaana became one of Marcel’s ancestors. However, when Marcel found out about the story, he thought the problem might return to its origins. Therefore, participants from Tuymaada 2019 must solve it!

## Input data

The input file `tygyn.in` contains on the first line the natural numbers $N$ and $M$. The next line contains $N$ numbers with values between 2 and $M$, representing the distinct numbers assigned to Tygyn Darkhan's $N$ cows.

## Output data

The output file `tygyn.out` contains the minimum number of herds in which Manchaary can group the cows.

## Constraints and clarifications

$1 \leq N < M \leq 1\ 000\ 000$

For 10 points, $M \leq 20$

For 40 points, $N \leq 1\ 000$

The evaluation is different from that during the official contest.

## Example

`tygyn.in`

```
5 100
2 3 11 22 12
```

`tygyn.out`
```
3
```

`tygyn.in`

```
10 20
8 12 20 6 3 7 11 13 19 15
```

`tygyn.out`

```
9
```