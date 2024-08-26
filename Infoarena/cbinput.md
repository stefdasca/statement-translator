## Task

Georgel has the following problem to solve: Given a sequence of $N$ numbers in ascending order with values between $1$ and $K$, where each value from $1$ to $K$ appears at least once in the sequence, find the last occurrence of each value from $1$ to $K$ in the sequence. Georgel, a novice in computer science, solved it as follows (C++ code):

```cpp
int binarySearch(int val) {
    int left = 1;
    int right = N;
    while(left <= right) {
        int mid = (left + right) / 2;
        if(v[mid] == val) {
            while(mid <= N && v[mid] == val) {
                mid++; // <==
            }
            return mid - 1;
        } else if(v[mid] < val) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

for (int i = 1; i <= K; i++) {
    cout << binarySearch(i) << endl;
}
```

We want to teach him a lesson he will never forget! Given $N$ and $K$, find a valid input sequence such that line 9 (mid++) is executed the maximum number of times.

## Input data

The input file `cbinput.in` will contain on the first line an integer $T$ representing the number of tests. Each test will appear on a single line that will contain two integers $N$ and $K$.

## Output data

The output file `cbinput.out` will contain the answers for the $T$ tests. The answer for each test will be on a single line that will contain $N$ numbers representing the desired sequence.

## Constraints

$1 \leq T \leq 100$

$1 \leq K \leq N \leq 1000$

## Example

`cbinput.in`
```
2
6 4
1 1
```

`cbinput.out`
```
1 1 1 1 2 2
3 4 1
```

## Explanation

In the first test, we can construct a sequence such that line $9$ is executed $6$ times.