```markdown
At Tesla's latest event, Paul Musk announced a new innovative product: autonomous parking. Known for launching incomplete products, the parking system is also incomplete, requiring automation to assign a parking spot to the cars that want to use it.

The parking lot consists of $N$ places, numbered from $1$ to $N$, and is open for $T$ seconds, starting from the $1^{st}$ second.
Throughout the day, $M$ cars arrive wanting to use the parking lot. For each of these cars, the arrival time $s_i$ and the departure time $p_i$ are known. The cars arrive in the order of their arrival time $s_i$ and occupy the parking spot in the time interval $[s_i, p_i]$. For each of them, you must display a free parking spot (if there are more, you can display any of them) where it can park, or $−1$ if the parking lot is full at the arrival time of the car. If a car cannot find a parking spot at the arrival time, it will not enter the parking lot at any future time.

At the end, Paul is interested in the cars that are still in the parking lot at the closing time, so he asks you to display the configuration of the parking lot at time $T$.

# Input data
The first line contains three integers $N$, $M$ and $T$, representing the number of parking spots, the number of cars that want to use the parking lot, and the number of seconds the parking lot is open, respectively.

The following $M$ lines each contain two integers $s_i$, $p_i$, representing the arrival of a car at second $s_i$ which will leave at second $p_i$.

The cars appear in the input file in increasing order of arrival time $s_i$.

# Output data
$M + 1$ lines will be displayed in total: the first $M$ lines each containing an integer between $1$ and $N$ representing the parking spot that the car will occupy, or $−1$ if there is no parking spot available.

The last line will contain $N$ integers, representing the configuration of the parking lot at closing time, where the $i^{th}$ number represents **the arrival time** of the car in the $i^{th}$ parking spot, or $−1$ if the $i^{th}$ parking spot is empty.

# Constraints and clarifications
- $1 \leq N, M, T \leq 200\ 000$
- $1 \leq s_i \leq T$
- $1 \leq s_i < p_i \leq 200\ 000$
- Considering the following $2 \times M$ values: $s_1, s_2, ..., s_M, p_1, p_2, ..., p_M$, these are pairwise distinct.
- **If there are multiple solutions, any of them can be displayed.**
- For 24 points, $s_i + 1 = p_i$, meaning each car stays exactly one second.
- For 26 points, $p_i > s_j$, meaning all cars arrive before any car leaves.
- For 26 points, $N \leq 1\ 000$.
- For 24 points, the initial constraints are respected.

# Example
`parcare.in`
```
2 4 6
1 3
2 10
4 6
5 8
```
`parcare.out`
```
2
1
2
-1
2 -1
```

# Explanations
The first car arrives at the $1^{st}$ second and is parked in spot $2$.
The second car arrives at the $2^{nd}$ second and is parked in spot $1$.
At the $3^{rd}$ second, spot $2$ is freed.
The third car arrives at the $4^{th}$ second and occupies spot $2$.
The car arriving at the $5^{th}$ second does not find a free spot.
At the $6^{th}$ second, spot $2$ is freed.
After the parking lot closes, in spot $1$ there will be the car that arrived at the $2^{nd}$ second; the second spot will be free.
```
