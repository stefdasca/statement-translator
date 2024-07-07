## Automatic Theorem Proving and Satisfiability Checking

The automatic demonstration of theorems and satisfiability checking of a formula are two important chapters within mathematical logic. Propositional formulas are composed of propositional variables (variables that can only take two values: "true" or "false") and logical operators "and", "or", "negation", "equivalent", "implies".

Here are some examples of propositional formulas:

* `~p&(q\leq>p)=>q`
* `p|q\leq>~p&~q`
* `p`
* `p=>q=>a=>t=>~p`

In this example, `p` and `q` are the propositional variables, `~` is the unary operator "negation", `&` is the binary operator "and", `|` is the binary operator "or", `=>` is the logical implication (and appears only in this sense, not as `\leq`), and `\leq>` is the logical equivalence. Additionally, parentheses can appear in a propositional formula to establish the order of operations. In the absence of parentheses, the operators in their order of priority are `~`, `&`, `|`, `=>`, `\leq>`.

In formulas of the form $[A_1 \ op \ A_2 \ op \ \dots \ op \ A_K]$, the associations are made from right to left, meaning $[A_1 \ op \ (A_2 \ op \ (\dots \ op \ A_K))]$, where $op$ is one of `&`, `|`, `=>`, `\leq>` and $A_i$ are propositional variables. In general, a propositional formula is defined as follows:
* any propositional variable is a propositional formula;
* if `A` and `B` are propositional formulas, then `(A)`, `~A`, `A&B`, `A|B`, `A=>B`, `A\leq>B` are propositional formulas.

If we substitute all variables in a propositional formula with truth values ("true" or "false"), we obtain a statement. The truth value of a statement is given by the following definition:
* if the statement consists of a single truth value, the statement takes that value;
* if `A` and `B` are statements, then:
  - `A` is true if and only if its truth value is "true";
  - `(A)` is true if and only if `A` is true;
  - `~A` is false if and only if `A` is true;
  - `A&B` is true if and only if both `A` and `B` are true;
  - `A|B` is false if and only if `A` is false and `B` is false;
  - `A=>B` is true if and only if `~A|B` is true;
  - `A\leq>B` is true if and only if `(A=>B)&(B=>A)` is true.

A solution of the propositional formula $P$ (a formula containing only the distinct propositional variables $A_1, A_2, \dots, A_N$) is any $N$-tuple $(v_1, v_2, \dots, v_N)$ consisting only of truth values for which, replacing each variable $A_i$ with the value $v_i$, the resulting statement is true.

# Task

Since logic is an unattractive subject for computer science students, they call upon ninth-grade computer science students to help them count how many distinct solutions a given propositional formula has.

# Input data

In the input file `logic.in`, there is a propositional formula where the propositional variables are represented by small letters of the English alphabet.

# Output data

In the output file `logic.out`, the number of solutions for the propositional formula from the input file will be printed.

# Constraints and clarifications

* The input will always contain a syntactically correct propositional formula.
* The formula contains fewer than $232$ characters.
* The formula contains at most $10$ small letters of the Latin alphabet.

# Example 1

`logic.in`
```
p|q\leq>~p&~q
```

`logic.out`
```
4
```

# Example 2

`logic.in`
```
a
```

`logic.out`
```
1
```
