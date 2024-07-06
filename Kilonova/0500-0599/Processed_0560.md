Here is the translated text:

---

It is Maria's birthday and she wants to bring candies to school. She wants to make her classmates' day sweeter, especially since there is a math test ahead. She has taken several boxes of candies. However, not wanting to differentiate between her classmates, she wants to bring a number of candies such that everyone gets the same number of candies, regardless of the final number of candies. She has tried to figure out in how many ways she can choose from the boxes of candies so that she gives a fixed number of candies per classmate, but she does not get the correct total number of possibilities.

# Task
Help Maria find the correct final result. She sent you the C++ program she wrote, and you need to fix her program. You can see the source [here](sumgen.cpp) or in the "Attachments" section on the side.

# Input data
The terminal will contain on the first line the number of boxes and the number of classmates, $n$ and $m$ respectively, and then on the next line an array of $n$ integers representing the candies in each box.

# Output data
The terminal will contain the total number of possibilities to bring the boxes to school.

# Constraints and clarifications
- $3 \leq n \leq 20$;
- $3 \leq m \leq 35$;
- A box can contain at least one candy and at most $20\ 000$ candies (not too many).

# Example 1
`stdin`
```
4 23
13 10 7 16
```
`stdout`
```
3
```

## Explanation
Maria can either take the boxes containing $13$ and $10$ candies, or the boxes with $7$ and $16$ candies, thus giving one candy per student, or all four boxes, giving $2$ candies per student.

# Example 2
`stdin`
```
8 20
14 6 14 13 5 10 20 7
```
`stdout`
```
13
```
