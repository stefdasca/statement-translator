# Twoton

Few of the problems at ACM-ICPC have the solution given right in the statement. However, for this problem, a possible solution is as follows:
```c
#include <stdio.h>  
int n;
int a[1000024];
int count = 0;

int wtf(int i) {
  count++;
  if (count >= 19997) {
    count -= 19997;
  }
  if (i == n - 1) {
    return a[i];
  }
  if (a[i] < wtf(i + 1)) {
    return a[i];
  } else {
    return wtf(i + 1);
  }
}

int main() {
  FILE *fin = fopen("twoton.in", "r");
  FILE *fout = fopen("twoton.out", "w");
  fscanf(fin, "%d", &n);
  for (int i = 0; i < n; ++i) {
    fscanf(fin, "%d", &a[i]);
  }
  wtf(0);
  fprintf(fout, "%d\n", count);
  fclose(fin);
  fclose(fout);
}
```

Write a program that calculates the number computed by the above program.

## Task

## Input data

The input data is read from the file `twoton.in`. The first line contains a natural number $n$ and the next line contains $n$ natural numbers, separated by spaces.

## Output data

In the output file `twoton.out`, print the number calculated by the above program.

## Constraints and clarifications

All numbers in the input file are natural numbers between $1$ and $100000$.

## Example

`twoton.in`
```
4
4 2 3 1
```

`twoton.out`
```
15
```