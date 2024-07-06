```markdown
# Task

We have a hidden number $x$ and you need to find its value using the following function:

```cpp
int compare (int guess) {
    return guess > x;
}
```

In other words, the function returns $1$ if the number you guessed is greater than the number you are trying to find, otherwise $0$.
\
You need to implement the `solve` function with the following prototype:

```cpp
int solve()
```

# Constraints and clarifications

* $1 \leq x \leq 1 \ 000 \ 000 \ 000$
* The problem can only be solved using C++ and you must include the file `compare.h` using `#include "compare.h"`.

# Example

```cpp
#include "compare.h"
int solve() {
    int x = 2;
    if (compare(x))
        return 1;
    return 1'000'000'000;
}
```

## Explanation
The function in the example returns the correct answer only when $x$ is $1$ or $1\ 000\ 000\ 000$.
```

I have translated the Romanian problem statement into English while preserving mathematics, variable names, and formatting, as well as the specified syntax for custom image formats. I also reviewed and corrected any potential grammar and/or syntax errors.