Certainly! Here is the translated competitive programming problem statement:

```markdown
Since the data structures in the C++ standard were too simple and couldn't help him in all situations, Gicu decided to dive into research to avoid getting too bored.

He is dissatisfied with the way a dictionary is implemented in C++ and wants to propose a new structure for the upcoming C++26 standard: an interval dictionary.

Concretely, he wants to base it on the implementation of `std::map<K, V>`, which he will extend to store the same value for a consecutive grouping of keys.

Gicu's structure should support the following operations:
* `assign(start, end, value)` — all keys in the dictionary within the interval `[start, end)` will have the value `value`;
* overload on the operator `[]` — it will return the value associated with a key in the dictionary.

# Task

To have a chance of being accepted by the C++ committee, he writes a generic implementation for the data structure. However, it has some mistakes; your task is to correct the source. It can be found [here](dictionar.cpp) or in the "Attachments" section on the side.

## Internal Data Representation

Gicu wants to create an efficient implementation from the start to confidently present his proposal. Therefore, he uses an implementation of `std::map` in which he only remembers the start of the interval.

Initially, all keys in the dictionary have the same initial value, `A`.

If he wants to set the interval $[5, 7)$ to the value `B`, in his internal representation he will add the entries `(5, 'B')` and `(7, 'A')` to the dictionary.

In practice, each pair of the type `(key, value)` in the internal representation of the dictionary indicates that from the key `key` up to (but not including) the next key in the dictionary, all values will have the value `value`.

Let's assume that at some point the `interval_map` structure with keys of type `int` contains: `(1, 'C')`, `(4, 'B')`, `(8, 'C')`, `(15, 'A')`.

Then:

* for any key between `INT_MIN` and $0$ inclusive, the default value `A` will be returned;
* for keys $1$, $2$, $3$, the value `C` will be returned;
* for keys $4$, $5$, $6$, $7$, the value `B` will be returned;
* for keys between $8$ and $14$, inclusive, the value `C` will be returned;
* for keys between $15$ and `INT_MAX`, the value `A` will be returned.

An empty dictionary:
~[interval_example1.png]

A dictionary after applying `assign(5, 7, 'B')`:
~[interval_example2.png]

A dictionary after several insertions:
~[interval_example3.png]

A dictionary that is not in canonical form:
~[interval_non_example4.png]

## Manual Testing

The information in this section is not required to solve the problem, it is intended to facilitate the debugging process.

If you need to display template variables from a method, you must specialize the method.

A specialization is a way to specify which implementation should be used for certain instantiations.

Documentation for this can be found in `reference/en/cpp/language/template_specialization.html`, and the necessary information is present in the sections `Explicit specializations of function templates` and `Members of specializations`.

## Templates

The information in this section is not required to solve the problem. But it is helpful to understand the context for the source code.

A template represents special syntax through which we define a family of classes or functions.

The first section specifies the template variables that can be used. These can replace data types in the respective function or class.

Code written in a template class does not represent an actual class but a prototype. It can be transformed into multiple classes by the compiler when the template is instantiated.

For example, the three declarations below each represent one instantiation of the template for the `pair` class:
```c++
pair<int, int> a;
pair<char, int> b;
pair<char, long long> c;
```
In total, there are 3 instantiations. Thus, the compiler will create 3 different `pair` classes, using the same prototype.

More information on templates: `reference/en/cpp/language/templates.html`.

# Input data

The first line contains the number of operations $n$ that will be performed on the structure.

The next $n$ lines contain the description of the operations. The operations can be of 3 types:
- Operation of type `0` — reads 3 values `interval_start`, `interval_end` and `key` representing the start of the interval, the end of the interval, and the key.
- Operation of type `1` — reads a key `key` and prints the value associated with this key.
- Operation of type `2` — prints the internal content of the interval dictionary.

Reading is already done and does not contain implementation problems.

# Output data

Prints the result for operations of type `1` and `2`.

# Constraints and clarifications

- The implementation for the interval dictionary must be canonical, meaning two consecutive entries in the interval dictionary must NOT have the same value. It is not allowed to have an interval dictionary containing consecutive entries `(5, 'A')`, `(8, 'A')`.
- Initially, all keys in the interval dictionary will have a value received in the constructor.
- Do not delete/modify lines marked with `DO NOT MODIFY`. Do not insert new lines between lines that form a continuous block of `DO NOT MODIFY`.
- It is not allowed to use the characters `[` and `]` in your implementation.
- The variables `interval_start` and `interval_end` in operation `0` will not be `INT_MIN` or `INT_MAX`.
- If all values in the interval have the default value, then it will not appear in the internal representation.

# Example
`stdin`
```
5
0 95 100 Z
0 57 64 A
0 17 52 P
0 18 55 R
2
```
`stdout`
```
17 P
18 R
55 A
95 Z
100 A
```

## Explanation 

We have $5$ operations on the structure:
* $4$ operations to set values for intervals;
* one operation to display the internal representation.

1. Set the values in the interval $[95, 100)$ to the value `Z`;
1. Set the values in the interval $[57, 64)$ to the value `A`;
1. Set the values in the interval $[17, 52)$ to the value `P`;
1. Set the values in the interval $[18, 55)$ to the value `R`.
```

Please let me know if you need any further adjustments or clarifications!