# Robo

ROBO is a robot that can execute a sequence of actions to repair a space station. ROBO has sensors that allow it to detect the "current state" of the station. A success state corresponds to the situation where the station has been repaired. The current state and the action chosen by ROBO uniquely determine the next state. An example is illustrated below: In the example above, states are represented by nodes (circles). Actions label the edges between nodes. The initial state is $0$, and the success state is $4$.

Analyzing the model above, ROBO observes that it can achieve the repair if it executes the sequence of actions $aba$ (passing through states $0, 1, 4$), but also if it executes $bbba$ (passing through states $0, 2, 3, 2, 4$). ROBO believes it can replace its internal model, illustrated above, with a better model, that is, one in which:

* the number of states is smaller;
* exactly the same action sequences lead to the repair of the station;

An example of a better model is given below: ROBO observes that (for example) $aba$ and $bbba$ are action sequences that lead to the repair of the station in the improved model as well. ROBO is convinced it can find an even better model. This is the one in the following figure: ROBO cannot find a better model than this - one with fewer states than $3$.

For any given model $M$, ROBO searches for the number of states of the best model - that is, the minimum number of states with which we can represent $M$ so that exactly the same action sequences from $M$ lead to the repair of the station in the improved model. The models have the following properties:

* The initial state is always labeled $0$;
* For every state and action, there is always a next state;
* There are no inaccessible states (states that cannot be reached through any action sequence);

## Input data

The input data is read from the file `robo.in`. The first line contains the number of tests, $T$. After that, for each test, the following information is read:

* The first line contains the number of states followed by the number of possible actions;
* The second line contains a sequence of numbers representing the states in which the station is repaired;
* Each subsequent line contains a triplet of the form $state \ action \ next_{state}$, where $state$ and $next_{state}$ are numbers and $action$ is an alphabetic character.

## Output data

The output file `robo.out` will contain, for each test, one line to standard output, which contains the number of states of the best model.

## Constraints

$1 \leq T \leq 10$

$1 \leq number \ of \ states \leq 5200$

$1 \leq number \ of \ actions \leq 10$

## Example

`robo.in`
```
1
5 2
4
0 a 1
0 b 2
1 b 1
1 a 4
2 a 4
2 b 3
3 a 4
3 b 2
4 a 4
4 b 4
```

`robo.out`
```
3
```