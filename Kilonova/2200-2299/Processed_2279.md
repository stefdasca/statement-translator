# Task

Dubota has graduated from the Police Academy and is preparing for his first mission as a police officer. The first step is to determine the teams. A team consists of $2$ police officers with different specializations. The $2$ specializations of the police officers are drivers and IT specialists. Drivers must know how to drive a car and use radio equipment, while IT specialists must know how to use radio equipment and a computer. The Academy graduated $NS$ police officers specializing in driving and $NI$ police officers specializing in IT. The police department has $M$ cars, $R$ radio equipment, and $C$ computers. Unfortunately, not all graduates know how to use the police equipment, meaning a driver knows how to drive only certain cars and use only certain radio equipment, and similarly, an IT specialist knows how to use only certain radio equipment and certain computers.

# Task

Given the lists of equipment that each graduate can use, determine the maximum number of police teams that can be formed.

# Input data

The first line of the input file `politia.in` contains $5$ integers separated by spaces: $NS \\ NI \\ M \\ R \\ C$. The next $2 \\cdot NS$ lines contain descriptions of the driver graduates. The first element on line $2 \\cdot i$ is $L_{iM}$, the number of cars the i-th driver graduate can use, followed by $L_{iM}$ numbers representing the indices of the cars they can use. On line $2 \\cdot i + 1$ is $L_{iR}$, the number of radio equipment the i-th driver graduate can use, followed by $L_{iR}$ numbers representing the indices of the radio equipment the driver can use. The next $2 \\cdot NI$ lines contain descriptions of the IT specialist graduates in a similar manner. On lines $2 \\cdot NS + 2 \\cdot i$ is the list of radio equipment that the i-th IT specialist graduate can use, and on lines $2 \\cdot NS + 2 \\cdot i + 1$ is the list of computers that the i-th IT specialist graduate can use.

# Output data

The output file `politia.out` will contain a single value, representing the maximum number of teams that can be formed.

# Constraints and clarifications

* A team consists of $2$ police officers: one driver and one IT specialist, and $3$ pieces of equipment: a car, radio equipment, and a computer.
* A car, radio equipment, or a computer cannot be used to form $2$ different teams.
* In a team, both the driver and the IT specialist must know how to use the same radio.
* $1 \leq NS, NI, M, R, C \leq 200$
* $0 \leq L_{iM} \leq M$
* $0 \leq L_{iR} \leq R$
* $0 \leq L_{iC} \leq C$

# Example

`politia.in`
```
2 3 2 4 2
1 1
2 1 2
2 1 2
2 3 4
1 1
1 1
2 2 3
1 1
1 4
1 2
```

`politia.out`
```
4
```

## Explanation

The first driver knows how to use car $1$ and radio equipment $1$ and $2$. The second driver knows how to use cars $1$ and $2$ and radio equipment $3$ and $4$. The first IT specialist knows how to use radio equipment $1$ and computer $1$. The second IT specialist knows how to use radio equipment $2$ and $3$ and computer $1$. The third IT specialist knows how to use radio equipment $4$ and computer $2$. A possible way to form teams is (driver, IT specialist, car, radio, computer): $(1, 1, 1, 1, 1) \\ (2, 3, 2, 4, 2)$.

