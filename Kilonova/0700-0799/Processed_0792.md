# Task

Given a recipe, determine the total preparation time as well as the quantities required for each ingredient.

# Input data

The input file `reteta.in` contains a string on the first line representing a recipe.

# Output data

The output file `reteta.out` will contain on the first line the total time required for preparing the recipe. The following lines will contain the ingredients in lexicographical order (dictionary order), one ingredient per line. For each ingredient, its name is followed by a space and then the total quantity required.

# Constraints and clarifications

* $0 < $ Length of a recipe $ \leq 1 \ 000$
* $1 \leq$ Number of ingredients $ \leq 100$
* The name of an ingredient is written with a maximum of 20 lowercase English letters.
* Preparation times are natural numbers $< 100$
* The quantities specified in the recipes are natural numbers $< 1 \ 000$
* $30\%$ of the score for a test is awarded for correctly determining the total time; the full score for a test is awarded for correctly determining the total time and correctly displaying the ingredients (in lexicographical order).

# Example

`reteta.in`
```
(((zahar 100 ou 3)5 unt 100 nuca 200)4 (lapte 200 cacao 50 zahar 100) 3)20
```

`reteta.out`
```
32
cacao 50
lapte 200
nuca 200
ou 3
unt 100
zahar 200
