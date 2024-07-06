Gigel is playing Kerbal Space Program and wants to build a fleet of rockets. A rocket consists of $3$ components: engine, capsule, and crew. He knows, for each component, how many models exist, and for each model of component, he knows how many pieces are available. Additionally, Gigel wants to test his computer's capabilities, so he imposes some limits regarding the pairs of $(\\text{model}:\\text{engine},\\:\\text{model}:\\text{capsule})$ and $(\\text{model}:\\text{capsule},\\:\\text{model}:\\text{crew})$ that can be found in the rockets he builds (the game does a lot of caching if pairs repeat). If a pair $(\\text{model}:\\ \\text{engine},\\:\\text{model}:\\ \\text{capsule})$ or $(\\text{model}:\\ \\text{capsule},\\:\\text{model}:\\ \\text{crew})$ does not appear in the list of limitations, it is implicitly considered that pairs of this type **cannot** appear in rockets.

# Task

Gigel wants to calculate the maximum number of rockets he can build for his fleet.

# Input data

The first line contains three natural numbers, $N_1$, $N_2$, and $N_3$, which represent the number of models for engine, capsule, and crew, respectively.
The second line contains $N_1$ natural numbers, which represent the number of pieces available for each engine model.
The third line contains $N_2$ natural numbers, which represent the number of pieces available for each capsule model.
The fourth line contains $N_3$ natural numbers, which represent the number of pieces available for each crew model.
The fifth line contains a natural number, $M$, which represents the number of pairs' limitations.
The next $M$ lines contain 4-tuples of natural numbers $(\\text{type},\\:\\text{model}_1,\\:\\text{model}_2,\\:\\text{lim})$, which are interpreted as follows:
* if $\\text{type}$ is $1$, then $\\text{model}_1$ is an engine model, $\\text{model}_2$ is a capsule model, and the maximum number of occurrences of a pair $(\\text{model}_1,\\:\\text{model}_2)$ is $\\text{lim}$;
* if $\\text{type}$ is $2$, then $\\text{model}_1$ is a capsule model, $\\text{model}_2$ is a crew model, and the maximum number of occurrences of a pair $(\\text{model}_1,\\:\\text{model}_2)$ is $\\text{lim}$.

# Output data

The first line will contain a single natural number, the maximum number of rockets.

# Constraints and clarifications

* $1 \\leq N_1, N_2, N_3 \\leq 150$;
* $1 \\leq M \\leq 45 \ 000$;
* $1 \\leq \text{lim} \\leq 1 \ 000$;
* $1 \\leq \text{pieces\_model\_engine} \\leq 1 \ 000$;
* $1 \\leq \text{pieces\_model\_capsule} \\leq 1 \ 000$;
* $1 \\leq \text{pieces\_model\_crew} \\leq 1 \ 000$;
* For tests worth $20$ points: 
    - $1 \\leq N_1, N_2, N_3 \\leq 2$;
    - $1 \\leq M \\leq 8$;
    - $1 \\leq \text{lim} \\leq 2$;
    - $1 \\leq \text{pieces\_model\_engine} \\leq 3$;
    - $1 \\leq \text{pieces\_model\_capsule} \\leq 3$;
    - $1 \\leq \text{pieces\_model\_crew} \\leq 3$;
* For the remaining $80$ points, there are no additional restrictions.

# Example

`stdin`
```
2 2 1
2 3
3 3
3
5
1 2 2 1
1 1 2 2
2 2 1 2
2 1 1 2
1 1 1 2
```

`stdout`
```
3
```

## Explanation

Only $3$ rockets can be built, one way being the following (in the format $(\\text{model\_engine}, \\text{model\_capsule}, \\text{model\_crew})$):

$(2, 2, 1)$
$(1, 2, 1)$
$(1, 1, 1)$