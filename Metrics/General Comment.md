# Metrics

For the metrics part of the project, I have used the radon library (https://pypi.org/project/radon/).
It seemed to be the most natural way for Python. Radon supports:

- McCabe’s complexity, i.e. cyclomatic complexity
- Raw metrics (these include SLOC, comment lines, blank lines...)
- Halstead metrics (all of them)
- Maintainability Index

Here is a short guideline how to interpret the result,
please have a look at the individual files (Newscounter, Preprocess, Visuals), in order to see the respective results:

**Cyclomatic complexity**

| CC score | Rank | Risk                                    |
|----------|------|-----------------------------------------|
| 1-5      | A    | low - simple block                      |
| 6-10     | B    | low - well structured and stable block  |
| 11-20    | C    | moderate - slightly complex block       |
| 21-30    | D    | more than moderate - more complex block |
| 31-40    | E    | high - complex block, alarming          |
| 41+      | F    | very high - error-prone, unstable block |

| Block type | Letter |
|------------|--------|
| Function   | F      |
| Method     | M      |
| Class      | C      |



**Maintainability Index**

| MI score | Rank | Maintainability |
|----------|------|-----------------|
| 100 - 20 | A    | Very high       |
| 19 - 10  | B    | Medium          |
| 9 - 0    | C    | Extremely low   |

| Construct        | Effect on CC | Reasoning                                                                               |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| if               | +1           | An if statement is a single decision.                                                   |
| elif             | +1           | The elif statement adds another decision.                                               |
| else             | +0           | The else statement does not cause a new decision. The decision is at the if.            |
| for              | +1           | There is a decision at the start of the loop.                                           |
| while            | +1           | There is a decision at the while statement.                                             |
| except           | +1           | Each except branch adds a new conditional path of execution.                            |
| finally          | +0           | The finally block is unconditionally executed.                                          |
| with             | +1           | The with statement roughly corresponds to a try/except block (see PEP 343 for details). |
| assert           | +1           | The assert statement internally roughly equals a conditional statement.                 |
| Comprehension    | +1           | A list/set/dict comprehension of generator expression is equivalent to a for loop.      |
| Boolean Operator | +1           | Every boolean operator (and, or) adds a decision point.                                 |

**Raw metrics**

| Abbreviation | Explanation                                         |
|--------------|-----------------------------------------------------|
| LOC          | total number of lines of code                       |
| LLOC         | number of logical lines of code                     |
| SLOC         | number of source lines of code                      |
| comments     | number of Python comment lines                      |
| multi        | the number of lines representing multi-line strings |
| blank        | the number of blank lines                           |

**Halstead metrics**

| Name              | Description                          |
|-------------------|--------------------------------------|
| h1                | number of distinct operators         |
| h2                | number of distinct operands          |
| N1                | total number of operators            |
| N2                | total number of operands             |
| Vocabulary        | Program vocabulary:η=η_1 + η_2       |
| length            | Program length: N=N_1 + N_2          |
| calculated_length | Calculated program length            |
| volume            | V = N log_2(η)                       |
| difficulty        | D = (η_1 / 2) * (N_2 / η_2)          |
| effort            | E = D * V                            |
| time              | Time required to program: T = E/18   |
| bugs              | Number of delivered bugs: B = V/3000 |