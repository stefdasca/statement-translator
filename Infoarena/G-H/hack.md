Hack

At the last contest on Codeforces, you had to solve the following problem: Given a matrix of dimensions $N \times M$ with cells of value $0$ or $1$ and a start cell, determine the minimum cost to reach all other cells from the start cell. A movement consists of changing the current cell with an adjacent one in the $4$ cardinal directions without ever leaving the matrix. The cost of movement is $0$ if and only if the two cells between which travel occurs have the same value. Otherwise, the cost is $1$. Of course, you solved this problem correctly because you are omniscient. Now you wish to examine the code of other participants and eventually find tests on which their solution does not work or works too slowly. In the source of a certain competitor, you found the following function that calculates distances using a BFS-like algorithm with a queue. You are sure that this code is still inefficient. You need to find a test of dimensions $N \times M$, with $N$ and $M$ of maximum value $50$, such that the value of the COUNTER variable is as high as possible after the function's execution.

```cpp
#define PII pair<int, int> 
#define VI vector<int>  
const int INFINITY = 1000000; 
const int dx[5] = {0, 0, 1, -1}; 
const int dy[5] = {1, -1, 0, 0};  

int getDistance(vector<string> &A, PII start) {
    int n = A.size(), m = A[0].size(); 
    int COUNTER = 0;  
    start.first--, start.second--; // reindexing from 0.  
    queue<PII> Q; 
    vector<VI> d(n, vector<int> (m, INFINITY)); 
    d[start.first][start.second] = 0; 
    Q.push(start);  
    while(!Q.empty()) { 
        PII node = Q.front(); 
        Q.pop();  
        COUNTER++;  
        for(int dir = 0; dir < 4; ++dir) { 
            int newX = node.first + dx[dir]; 
            int newY = node.second + dy[dir]; 
            if(newX < 0 || newX >= n || newY < 0 || newY >= m) continue;
            int cost = 0; 
            if(A[node.first][node.second] != A[newX][newY]) cost = 1;  
            if(d[node.first][node.second] + cost < d[newX][newY]) { 
                d[newX][newY] = d[node.first][node.second] + cost; 
                Q.push({newX, newY}); 
            } 
        } 
    }  
    return COUNTER; 
} 
```

Your score will be calculated as follows, with the formula being valid only if COUNTER is at least $2500$. Otherwise, the score is $0$.
```cpp
int POINTS = floor((min(COUNTER, 18000) - 2500.0) / (18000 - 2500) * 100); 
```
In short, for $100$ points the COUNTER variable must be greater than or equal to $18,000$. 

## Input data

The input file `hack.in` will contain nothing.

## Output data

The output file `hack.out` will contain $4$ numbers on the first line: $N$, $M$, $startX$, $startY$, representing the dimensions of the matrix and the coordinates of the start cell. $startX$ and $startY$ will be indexed from $1$.

## Constraints

$1 \leq N, M \leq 50$ 

The statement is fictitious, do not look for the last contest on Codeforces.

## Example

`hack.in`

`hack.out`
```
5 5 3 3
00000
01110
01010
01110
00000
```

## Explanation