# Metrics

For the metrics part of the project, I have used the radon library (https://pypi.org/project/radon/).
It seemed to be the most natural way for Python. Radon supports:

- McCabe’s complexity, i.e. cyclomatic complexity
- Raw metrics (these include SLOC, comment lines, blank lines...)
- Halstead metrics (all of them)
- Maintainability Index

Here is a short guideline how to interpret the result,
please have a look at the individual files (Newscounter, Preprocess, Visuals), in order to see the respective results:

##Cyclomatic complexity
| CC score | Rank | Risk                                    |
|----------|------|-----------------------------------------|
| 1-5      | A    | low - simple block                      |
| 6-10     | B    | low - well structured and stable block  |
| 11-20    | C    | moderate - slightly complex block       |
| 21-30    | D    | more than moderate - more complex block |
| 31-40    | E    | high - complex block, alarming          |
| 41+      | F    | very high - error-prone, unstable block |

Block type	Letter
Function	F
Method	    M
Class	    C