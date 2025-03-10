# In fact, we are just two...

Now that they managed to make Constanța great again, the four of them are faced with a new challenge: the next round at OOIT. Thus, Rara decides to call his magic mace to his home to prepare for the contest. The problem is that, with the arrival of the cold and the rains, the power went out throughout the entire city. It is engulfed in total darkness, and the two friends can no longer find each other. It seems that Constanța is not that great after all...

The city is in the form of a rectangular matrix of dimensions $N \times M$, where each element represents a piece of road. Fortunately, Rara knows $K$ positions of streetlights that he can turn on, even without power, using his magic battery.

Each streetlight $i \ (1 \leq i \leq K)$ is located on row $X_i$ and column $Y_i$ and has a lighting radius $R_i$. If it is on, it will illuminate all road pieces $(X_d, Y_d)$ for which $|X_d - X_i| + |Y_d - Y_i| \leq R_i$.

Additionally, the streetlights are connected by a magic wire such that if streetlight $i$ is on, then the preceding streetlights will also be turned on. Formally, turning on a streetlight $i$ leads to the lighting of streetlights $j$ with the property that $1 \leq j \leq i$.

# Task

Since Rara is a very lazy boy, he asks for your help to find the minimum number of streetlights that need to be turned on so that his friend can reach him from the starting point $(1, 1)$ to $(N, M)$, walking only in the $N$, $S$, $E$, and $W$ directions and only on road pieces illuminated by streetlights.  

# Input data

The first line contains, separated by a space, $N$ and $M$ (the dimensions of the city) and $K$ (the number of streetlights).  
The next $K$ lines contain the characteristics of the streetlights. Thus, line $i + 1$ contains $X_i$, $Y_i$, and $R_i$, the characteristics of the $i$-th streetlight, separated by a space.  

# Output data

The first line will contain the minimum number of streetlights that need to be turned on so that the two friends can meet.  

# Constraints and clarifications

- $1 \leq N, M \leq 1000$.
- $1 \leq K \leq N \cdot M$.
- $1 \leq X_i \leq N$. 
- $1 \leq Y_i \leq M$.  
- $0 \leq R_i \leq 2000$.
- It is guaranteed that if Rara turns on all the streetlights, his friend will reach $(N, M)$.
- It is guaranteed that at most one streetlight will be on a piece of road.
- For fast input and output, it is recommended to use the following lines of code at the beginning of the `main` function:
```cpp
ios::sync_with_stdio(false);  
cin.tie(NULL);  
cout.tie(NULL);  
```  

| # | Points | Restrictions |  
|:---:|:----:|:----:|  
| 0 | 0 | Example |
| 1 | 21 | $1 \leq N, M \leq 100$ |
| 2 | 17 | $0 \leq R_i \leq 5$ |
| 2 | 62 | Without additional restrictions |  

# Example  

`stdin`  
```
5 4 6
1 1 2
4 2 1
5 1 1
5 3 1
2 4 0
3 4 1
```  

`stdout`  
```
4
```  

## Explanation

After Rara turns on the first $4$ streetlights, the city looks like this:

$$
\begin{bmatrix}
   1 & 1 & 1 & 0 \\
   1 & 1 & 0 & 0 \\
   1 & 1 & 0 & 0 \\
   1 & 1 & 1 & 0 \\
   1 & 1 & 1 & 1 \\
\end{bmatrix}
$$

In this matrix, we have marked road pieces with $1$ if they are illuminated and with $0$ otherwise.
One can observe that there is a path that Rara's friend can take from $(1, 1)$ to $(5, 4)$, walking only on illuminated road pieces. 
Such a path is the following: $(1, 1) \rightarrow (2, 1) \rightarrow (3, 1) \rightarrow (4, 1) \rightarrow (5, 1) \rightarrow (5, 2) \rightarrow (5, 3) \rightarrow (5, 4)$.