## Task

You have a very simple problem to solve. You are given an array (initially empty) and many operations on it. The operations are of 5 types: Type 1, add the value $v$ at position $1$, shifting all other elements $1$ position to the right. Type $2$, add the value $v$ to the end. Type $3$, remove the first element, shifting the rest $1$ position to the left, the inverse operation of type $1$. Type $4$, remove the last element, the inverse operation of type $2$. Type $5$, you are given $x$, $y$, and $k$. You need to determine the $k$-th element in sorted order among the elements positioned at $x$, $x + 1$, $x + 2$, $\dots$, $y$ in the array.

## Input data

The input file `kthvalue.in` will contain on the first line a natural number $M$, representing the number of operations you need to handle. The next $M$ lines will describe each operation in detail. Thus the first number on each line will represent the type of the operation ($1$ $2$ $3$ $4$ or $5$). For operations of type $1$ on the same line there will be an additional number $v$ representing the value to be added. For operations of type $5$ on the same line there will be an additional $3$ numbers $x$, $y$, and $k$ with the descriptions given above. To parse the file you can use the following C++ code:
```
#include <fstream>
#include <memory>
using namespace std;

class Reader {
public:
    Reader(const string& filename): m_stream(filename), m_pos(kBufferSize - 1), m_buffer(new char[kBufferSize]) { next(); }

    Reader& operator>>(int& value) {
        value = 0;
        while (current() < '0' || current() > '9') next();
        while (current() >= '0' && current() <= '9') {
            value = value * 10 + current() - '0';
            next();
        }
        return *this;
    }

private:
    const int kBufferSize = 32768;

    char current() { return m_buffer[m_pos]; }

    void next() {
        if (!(++m_pos != kBufferSize)) {
            m_stream.read(m_buffer.get(), kBufferSize);
            m_pos = 0;
        }
    }

    ifstream m_stream;
    int m_pos;
    unique_ptr<char[]> m_buffer;
};

Reader fin("kthvalue.in");
int x;
fin >> x;
```

## Output data

The output file `kthvalue.out` must contain as many lines as there are operations of type $5$. For each such line, you need to print the corresponding number.

## Constraints and clarifications

$1 \leq M \leq 1\ 000\ 000$  
$1 \leq x \leq y \leq \text{number of elements in the array at that moment}$  
$1 \leq v \leq M$  
There won't be operations of type $3$ or $4$ when the array is empty  
You are recommended to parse the input file efficiently.

## Example

`kthvalue.in`
```
7
1 1
1 7
2 7
5 1 3 1
3
2 6
5 2 3 2
1 7
```

`kthvalue.out`
```
7
1
```

## Explanation

The array will transform as follows [] $\rightarrow$ [1] $\rightarrow$ [7 1] $\rightarrow$ [7 1 7] $\rightarrow$ [1 7] $\rightarrow$ [1 7 6].