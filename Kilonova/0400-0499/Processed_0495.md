# Task
Luka is driving his truck along a straight road with many traffic lights. For each traffic light, he knows how long it stays red and how long it stays green (like an ordinary traffic light, the colors alternate between red and green, and the traffic light operates indefinitely, with no yellow color).

When Luka begins his journey, all the traffic lights are red and at the start of their cycle. Starting on red, each traffic light will turn green after $R_k$ seconds, where $R_k$ is the time the respective traffic light stays red, after which it changes to green and will turn red again after $V_k$ seconds and the cycle repeats. Luka moves at a speed of one unit of distance per second. When a traffic light is red, Luka stops and waits until it becomes green.
Additionally, Luka is a very attentive driver and starts exactly when the traffic light turns green, and his truck is so powerful that it reaches cruising speed in negligible time.

Write a program that determines how long it takes Luka to reach the end of the road. He starts the journey at distance zero and reaches the end at distance $L$.

**Note: Input data is read from the keyboard, and output data is displayed on the console.**

# Input data
The first line contains two natural numbers $N$, the number of traffic lights, and $L$, the length of the road.

Each of the next $N$ lines contains three integers $D_k$, $R_k$, $V_k$, where $D_k$ represents the distance of the traffic light from the start of the road, $R_k$ represents how long the traffic light is red, and $V_k$ represents how long the traffic light is green.

The traffic lights will be ordered increasingly by $D$. No two traffic lights will be at the same position.

# Output data
Print the time (in seconds) Luka needs to reach the end of the road.

# Constraints and clarifications
- $ 1 \le N \le 100 \ ; \ 1 \le L \le 1000 $
- $ 1 \le D_k < L \ ; \ 1 \le R_k, V_k \le 100 $

# Example 1
  `stdin`
  ```
2 10
3 5 5
5 2 2
  ```
  `stdout`
  ```
  12
  ```

# Example 2
  `stdin`
  ```
4 30
7 13 5
14 4 4
15 3 10
25 1 1
  ```
  `stdout`
  ```
  36
  