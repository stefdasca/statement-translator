Sure, here is the translated text:

Although he fell in love with Miruna, Tassadar does not neglect his duties as a commander and is planning an assault on the planet Tarsonis. On this planet, there are $N$ capitals numbered from $0$ to $N-1$, represented as points in the plane. Tassadar has infiltrated a spy into each capital. The spies are connected to the telepathic network called Khala and can communicate in this way. They do not know their coordinates, but they can sense the distance between themselves and any other spy.
To determine the distance between two spies, Tassadar needs to concentrate intensely and connect to the minds of both spies simultaneously. He wants to reconstruct the map of the $N$ capitals by querying a minimal number of pairs of spies because he wants to save his strength for Miruna's challenges.
Help Tassadar reconstruct the map and conquer the planet!

# Interaction

To solve this problem, you need to include the following function in your source code:

```cpp
void recover(int N);
```

This function will be called once at the beginning of the program execution and will receive as a parameter the number of capitals. Within it, you can call the following function as many times as you want, which is provided by the judging system:

```cpp
double query(int a, int b);
```

By calling this function, you perform a query between the spies with indices $a$ and $b$. The function returns the distance between the capitals where the two spies are located. Both $a$ and $b$ must be distinct numbers, greater than or equal to $0$ and less than $N$. To reconstruct the map, you will need to call the following function:

```cpp
void sendRecovered(double *x, double *y);
```

This function receives as parameters two arrays of length $N$ indexed from $0$, representing the coordinates of the $N$ capitals. The call to this function will terminate the execution of the program.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* A map is considered valid if the distance between any two capitals corresponds to reality and if all capitals have coordinates that are real numbers within the interval $[-10^9, 10^9]$
* The distance between two capitals whose coordinates have been reconstructed is considered correct if it differs by an absolute or relative error of at most $0.0001$ from the real distance.
* There is at least one solution where all capitals have coordinates within the interval $[-1\ 000, 1\ 000]$
* For $15\%$ of the tests, all capitals are collinear
* Let $Q$ be the number of queries made. The score awarded for a test will be:
    * $100\%$ of the score if $Q \leq 3 \cdot N$
    * $60\%$ of the score if $3 \cdot N < Q \leq 10 \cdot N$
    * $20\%$ of the score if $10 \cdot N < Q$

# Example 1

`Grader actions:`
```
recover(2)
return 2.1
-
```

`Competitor actions:`
```
-
query(0, 1)
sendRecovered({0.0, 2.1}, {1.0, 1.0})
```

## Explanation

Tassadar queries the spies $0$ and $1$. They are at a distance of $2.1$ from each other. Since there are only two capitals, any pair of points located at a distance of $2.1$ is correct. For example, the points $(0.0, 1.0)$ and $(2.1, 1.0)$.