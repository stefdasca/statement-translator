*March 1993,*  
Tradition made the little rms spend his time in the better text editor again. Noticing his worrying obsession, those around him might say: "Why don't you ever get out of that editor? Other kids your age do other things; they spend time on their mobile phones, go online in a browser!" rms didn’t see any problem; even others his age couldn't leave the editor because they didn't know the command. However, it was a special day, on Saint IGNUcius day, rms wouldn't have thought of dealing with superficial tasks. The heated email discussions with other pedants seemed to have no resolution and had captured his entire attention. He was about to present the latest functionality he had worked on, M-x compose-a-random-problem and the resulting output (we dare to say, as much!), obtained.

We consider two arrays of `N` natural numbers, `V` and `E`. It is required to find the sum of the maximum values in `V` for all subarrays determined by the endpoints $1 \leq i_1 \leq i_2 \leq N$ where $E_{i_1} = E_{i_2}$.

# Input data
The first line contains the number of elements `N`. Each of the next two lines contains `N` natural numbers, representing the elements of arrays `V` and `E`, respectively.

# Output data
The first line will contain the required result, modulo `1 000 000 007`.

# Constraints and clarifications
* $1 \leq N \leq 3 \cdot 10^5$
* $1 \leq V_i, E_i \leq 10^9$ for `1 \leq i \leq N`
* A subarray is a subsequence consisting of elements with consecutive indices.

## Subtask 1 (8 points)
* `N \leq 2 000`
## Subtask 2 (11 points)
* $E_i = 1$ for `1 \leq i \leq N`
## Subtask 3 (12 points)
* $E_i \leq 20$ for `1 \leq i \leq N`
## Subtask 4 (12 points)
* $V_i \leq 20$ for `1 \leq i \leq N`
## Subtask 5 (19 points)
* $N \leq 5 \cdot 10^4$
## Subtask 6 (38 points)
* Without additional constraints.

## Example

`stdin`

```
5
5 29 3 28 30
9 8 9 9 8
```

`stdout`

```
211
```

Explanation
---

The subarrays that contribute to the answer are those where the endpoints have equal values in `E`. In this case, the tuples containing the two endpoints and the maximum value in `V` are `(1, 1, 5), (1, 3, 29), (1, 4, 29), (2, 2, 29), (2, 5, 30), (3, 3, 3), (3, 4, 28), (4, 4, 28), (5, 5, 30)`.

Summing these values gives `211`.