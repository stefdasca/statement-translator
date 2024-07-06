After six years of work, Charles has finished cleaning the black carbon production facilities in Copșa Mică. To keep himself away from Blackjack tables, he got a job at CERN, where he will work on the new particle accelerator named the Even Larger Hadron Collider (ELHC).

ELHC is in the shape of a circular tunnel with a circumference of $P$ kilometers, $P$ being a prime number. Along the tunnel, there are $P$ sensors numbered from $0$ to $P-1$, the distance between two consecutive sensors being exactly $1$ kilometer.

An experiment conducted in the ELHC involves studying a particle of type $G$, $1 \le G < P$. If this particle is raised to an energy level $k$ and is launched from the position of sensor $0$ in the direction of sensor $1$, it will travel exactly $G^k$ kilometers through the tunnel and then disintegrate, triggering the sensor $s$ where the particle disintegration occurs.

The experiment is considered to have complete data if, by launching $P-1$ particles of type $G$ elevated to all energy levels $k$ from $1$ to $P-1$, it is possible to trigger all sensors $s$ numbered with values between $1$ and $P-1$, i.e., all sensors in the tunnel except sensor $0$.

# Task
Given $T$ pairs of numbers $G$ and $P$, determine if the experiment for studying the particle of type $G$ in a tunnel of circumference $P$ produces complete data.

# Input data
The input file `elhc.in` contains on the first line a number $T$, representing the number of experiments to be conducted. Each of the following $T$ lines contains two numbers $G$ and $P$ separated by a space, representing the execution of an experiment with a particle of type $G$ in a tunnel of circumference $P$.

# Output data
The output file `elhc.out` will contain a single line with $T$ bits written consecutively, i.e., without spaces between them. The $i$-th bit is $1$ if for the $i$-th experiment we can obtain complete data, and $0$ otherwise.

# Constraints and clarifications
- $1 \le T \le 1\ 000$;
- $1 \le G < P < 1\ 000\ 000\ 000$;
- $P$ is a prime number;
- **Subtask 1** - 7 points - $P \le 100$;
- **Subtask 2** - 14 points - $P \le 10\ 000$;
- **Subtask 3** - 53 points - $P \le 1\ 000\ 000$;
- **Subtask 4** - 26 points - no additional restrictions.

# Example
`elhc.in`
```
6
2 3
3 5
2 7
3 7
3 11
5 11
```
`elhc.out`
```
110100
```

## Explanation
The input file contains $T=6$ experiments.

The second particle is of type $3$ and will be launched through a tunnel with a circumference of $5$, with $5$ sensors numbered from $0$ to $4$. Raised to energy levels $1$, $2$, $3$, and $4$ respectively, and launched each time from the position of sensor $0$, the particle will travel $3$, $9$, $27$, and $81$ kilometers respectively and will trigger sensors $3$, $4$, $2$, and $1$. These are all the sensors that need to be triggered, therefore the experiment produces valid data, so the second bit in the output string is $1$.

The third particle is of type $2$ and will be launched through a tunnel with a circumference of $7$. Raised to energy levels $1$, $2$, $3$, $4$, $5$, and $6$ respectively, and launched each time from the position of sensor $0$, the particle will trigger sensors $2$, $4$, $1$, $2$, $4$, and $1$. Since sensors $3$, $5$, and $6$ are not triggered, the experiment does not have complete data, so the third bit in the output string is $0$.