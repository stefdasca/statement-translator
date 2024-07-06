> "It's easy to write verses,  
When you have nothing to say,  
Stringing empty words  
That will echo in the end."

The following list of functions is considered as defined:

* $reverse(s)$: reverses the word $s$;
* $order(s)$: rearranges the letters of the word $s$ such that the letters are sorted alphabetically;
* $concat(s_1,s_2)$: concatenates all the vowels in the word $s_2$ to the vowels in the word $s_1$, in order;
* $substr(s,x,y,p)$: extracts the subsequence found between positions $x$ and $y$ in the word $s$, going from $x$ to $y$ by steps of $p$ (starting at position $x$), $ 1 \\leq x \\leq y \\leq strlen(s)$.

Examples:
* $reverse("hello")$: "olleh";
* $order("hello")$: "ehllo";
* $concat("hello", "world")$: "eoo";
* $substr("helloworld", 2, 9, 3)$: "eor";

# Task

The task is to evaluate an expression composed of calls to these functions.

# Input data

The first line will contain the expression to evaluate.

# Output data

The first line will contain the result obtained from the evaluation, within $" "$.

# Constraints and clarifications

* $1 \\leq strlen(expression) \\leq 30 \ 000$;
* $1 \\leq strlen(s) \\leq 100$, for any word $s$;
* In the tests, all words $s$ are enclosed within $" "$;

# Example 1

`stdin`
```
"helloworld"
```

`stdout`
```
"helloworld"
```

## Explanation

There are no transformations to perform.

# Example 2

`stdin`
```
reverse(order(concat("hello",substr("world",1,5,1))))
```

`stdout`
```
"ooe"
```

## Explanation

$substr("world",1,5,1)$: "world"  
$concat("hello",substr("world",1,5,1))$: "eoo"  
$order(concat("hello",substr("world",1,5,1)))$: "eoo"  
$reverse(order(concat("hello",substr("world",1,5,1))))$: "ooe"