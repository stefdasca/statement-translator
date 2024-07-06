Miruna's passion is coloring. Last vacation, she spent her time at her grandmother's countryside home and, because she was a bit bored, she decided to paint the fence of her grandmother's house.

The fence is composed of $N$ boards placed next to each other. Miruna found in her grandmother's garage $5$ boxes of paint in different colors: **white**, **blue**, **red**, **green**, and **yellow**. When painting the fence, Miruna followed these rules:
- If a board was painted **white**, the next board was painted **blue**.
- If a board was painted **blue**, then the next board was painted either **white** or **red**.
- If a board was painted **red**, then the next board was painted either **blue** or **green**.
- If a board was painted **green**, then the next board was painted either **red** or **yellow**.
- If a board was painted **yellow**, then the next board was painted **green**.

After finishing her work, Miruna admired her "work of art" and wondered in how many different ways she could have painted her grandmother's fence.

# Task

Help Miruna find the answer to her question.

# Input data

The file `culori.in` contains on its first line a single natural number $N$.

# Output data

The output file `culori.out` will contain on its first line a single integer representing the number of different ways Miruna could have painted her grandmother's fence.

# Constraints and clarifications

* $1 \leq N \leq 5 \ 000$;
* For $25 \%$ of the tests $N \leq 45$.

# Example

`culori.in`
```
4
```

`culori.out`
```
24
```

## Explanation

The fence can be painted as follows:
1. (white, blue, white, blue); 
2. (white, blue, red, blue);
3. (white, blue, red, green); 
4. (blue, white, blue, white);
5. (blue, white, blue, red); 
6. (blue, red, blue, white);
7. (blue, red, blue, red); 
8. (blue, red, green, red);
9. (blue, red, green, yellow); 
10. (red, blue, white, blue);
11. (red, blue, red, blue); 
12. (red, blue, red, green);
13. (red, green, red, blue); 
14. (red, green, red, green);
15. (red, green, yellow, green); 
16. (green, red, blue, white);
17. (green, red, blue, red); 
18. (green, red, green, red);
19. (green, red, green, yellow); 
20. (green, yellow, green, red);
21. (green, yellow, green, yellow); 
22. (yellow, green, red, blue);
23. (yellow, green, red, green); 
24. (yellow, green, yellow, green).