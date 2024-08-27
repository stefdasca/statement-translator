# Chocolate 2

Taking a break from cleaning, Henry and Hetty are playing with a grid of dimensions $N * M$ and many pieces of chocolate of dimensions $2 * 1$. Each piece of chocolate can be placed anywhere on the grid as long as it covers exactly two cells. The pieces of chocolate can be placed either vertically or horizontally, and must not overlap with other pieces. A cell is considered covered if there is a piece of chocolate placed over it. Henry and Hetty will perform a total of $K+1$ steps. At step $0$, Henry asks Hetty to place a set $A_0$ of chocolate pieces on the grid such that all cells are covered. Then, steps $1$ to $K$ consist of the following stages: Henry chooses a set $C_i$ of unmarked cells and marks them. Once a cell is marked, it remains marked for all following steps. Hetty now has to ensure that all marked cells are uncovered, and all unmarked cells are covered. To do this, she will choose a set $E_i$ of already placed chocolate pieces on the grid and remove them; then, she will place another set $A_i$ of chocolate pieces (possibly empty) on the grid. Help Hetty perform the necessary steps: if she manages to execute them correctly, she can eat all the chocolate used for the game!

## Input data

The first line of the input file `ciocolata2.in` contains three natural numbers $N$, $M$, and $K$, according to the task description. The following lines describe steps $1$ to $K$: the first line describing step $i$ will contain a natural number $B_i$ - the number of cells marked by Henry at step $i$. The next $B_i$ lines contain pairs of natural numbers $X$ and $Y$, representing the coordinates of the cells marked by Henry at the current step.

## Output data

A set of chocolate pieces is displayed as follows: on the first line, display a natural number $P$, representing the size of the set. Then, on the following $P$ lines, display four natural numbers $X_1$, $Y_1$, $X_2$, $Y_2$ representing the coordinates of the cells $(X_1, Y_1)$ and $(X_2, Y_2)$ covered by the current piece. Note: these cells must be adjacent. In the output file `ciocolata2.out`, you must first display the set $A_0$ of chocolate pieces added by Hetty at step $0$. Then, for each step $i$ from the remaining $K$, first display the set $E_i$ of pieces removed by Hetty, and then the set $A_i` of pieces added by Hetty, in this order. If it is not possible for Hetty to execute step $i$, display "-1" and terminate the program, ignoring the remaining steps.

## Constraints

$1 \leq N, M \leq 70$  
$1 \leq K \leq 1700$

For 10% of the tests, $1 \leq N, M \leq 10$.

For 40% of the tests, $1 \leq N, M \leq 50$.

It is guaranteed that step $0$ can always be executed.

It is guaranteed that no cell will be marked twice.

Cell coordinates are indexed from $1$.

Fast output: Since the generated output files can be large, it is recommended to parse the output. To help you, we provide the following code:
```cpp
#include <fstream>
using namespace std;

class Writer {
public:
    Writer(const char *name): m_stream(name) {
        memset(m_buffer, 0, sizeof(m_buffer));
        m_pos = 0;
    }

    Writer& operator<<(int a) {
        int many = 0;
        do {
            digit_buffer[many++] = a % 10 + '0';
            a /= 10;
        } while (a > 0);
        for (int i = many - 1; i >= 0; --i) putchar(digit_buffer[i]);
        return *this;
    }

    Writer& operator<<(const char *s) {
        for (; *s; ++s) putchar(*s);
        return *this;
    }

    ~Writer() {
        m_stream.write(m_buffer, m_pos);
    }

private:
    void putchar(char c) {
        m_buffer[m_pos++] = c;
        if (m_pos == kBufferSize) {
            m_stream.write(m_buffer, m_pos);
            m_pos = 0;
        }
    }

    static const int kBufferSize = 32768;
    ofstream m_stream;
    char m_buffer[kBufferSize];
    char digit_buffer[30];
    int m_pos;
} fout("ciocolata2.out");
```
This class can only display non-negative natural numbers and character strings. For example, to display a pair of numbers separated by space, and the number $-1$, use:
```cpp
fout << a << " " << b << "\n";
fout << "-1\n";
```

## Example

`ciocolata2.in`

```
2 3 4
2
2 1
1 3
2
1 1
2 3
1
1 2
1
2 1
```

`ciocolata2.out`

```
3
1 1 1 2
2 1 2 2
1 3 2 3
2
2 1 2 2
1 3 2 3
1
2 2 2 3
2
1 1 1 2
2 2 2 3
1
1 2 2 2
-1
```

## Explanation

The set $A_0$ initially added is composed of pieces $((1,1),(1,2))$, $((2,1),(2,2))$, $((1,3),(2,3))$. 

At step $1$, the cells $(2,1)$ and $(1,3)$ are marked. We remove the set $E_1 = \{ ((2,1),(2,2)), ((1,3),(2,3)) \}$ and add the set $A_1 = \{ ((2,2),(2,3)) \}$ at the first step. 

At step $2$, the cells $(1,1)$ and $(2,3)$ are marked. We remove the set $E_2 = \{ ((1,1),(1,2)), ((2,2),(2,3)) \}$ and add the set $A_2 = \{ ((1,2),(2,2)) \}$ at the second step. 

At step $3$, the cell $(1,2)$ is marked. No variant exists to form sets $E_3$ and $A_3$, so we display $-1$. We ignore step $4$.