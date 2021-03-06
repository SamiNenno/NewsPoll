# Metrics

For the metrics part of the project, I have used the radon library (https://pypi.org/project/radon/).
It seemed to be the most natural way for Python. Radon supports:

- McCabe’s complexity, i.e. cyclomatic complexity
- Raw metrics (these include SLOC, comment lines, blank lines...)
- Halstead metrics (all of them)
- Maintainability Index

Here are the results and a short guideline how to interpret the results:

**Cyclomatic complexity**
radon cc /Users/macbook/Desktop/Python_Files/NewsPoll -s -a\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Preprocess.py**\
    M 72:4 Poll.parse_poll - C (14)\
    M 172:4 Keywords.create_searchterms - C (14)\
    C 9:0 Poll - B (6)\
    C 158:0 Keywords - B (6)\
    M 259:4 Relevance.search - A (4)\
    M 301:4 Frequency_Table.__init__ - A (4)\
    M 18:4 Poll.__init__ - A (3)\
    C 233:0 Relevance - A (3)\
    C 295:0 Frequency_Table - A (3)\
    M 164:4 Keywords.__init__ - A (2)\
    M 211:4 Keywords.save_searchterms - A (2)\
    M 239:4 Relevance.__init__ - A (2)\
    M 251:4 Relevance.create_search_dict - A (2)\
    M 309:4 Frequency_Table.compute_table_shape - A (2)\
    M 136:4 Poll.select_relevant_polls - A (1)\
    M 147:4 Poll.fit - A (1)\
    M 223:4 Keywords.fit - A (1)\
    M 277:4 Relevance.save_checked_newcollection - A (1)\
    M 286:4 Relevance.fit - A (1)\
    M 326:4 Frequency_Table.save_table - A (1)\
    M 334:4 Frequency_Table.fit - A (1)\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Newscounter.py**\
    M 32:4 Newscounter.count - B (6)\
    C 8:0 Newscounter - A (3)\
    M 59:4 Newscounter.party_count - A (3)\
    M 28:4 Newscounter.create_search_dict - A (2)\
    M 108:4 Newscounter.date_casting - A (2)\
    M 9:4 Newscounter.__init__ - A (1)\
    M 56:4 Newscounter.save_freq_count - A (1)\
    M 66:4 Newscounter.absolute_count - A (1)\
    M 73:4 Newscounter.relative_count - A (1)\
    M 101:4 Newscounter.create_relative_frame - A (1)\
    M 119:4 Newscounter.fit - A (1)\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Visuals.py**\
    M 41:4 Visuals.multiple_count - B (6)\
    M 16:4 Visuals.individual_count - A (5)\
    C 7:0 Visuals - A (4)\
    M 67:4 Visuals.party_count - A (4)\
    M 107:4 Visuals.compare_party_count - A (2)\
    M 8:4 Visuals.__init__ - A (1)\
    M 90:4 Visuals.plot_poll - A (1)\
    M 143:4 Visuals.compare_individual_count - A (1)\
/Users/macbook/Desktop/Python_Files/NewsPoll/Unittest_Scripts/**test_Preprocess.py**\
    C 4:0 MyTestCase - A (2)\
    M 6:4 MyTestCase.test_poll - A (1)\
    M 19:4 MyTestCase.test_keywords - A (1)\
    M 24:4 MyTestCase.test_relevance - A (1)\
    M 30:4 MyTestCase.test_frequency_table - A (1)\
/Users/macbook/Desktop/Python_Files/NewsPoll/DSL/**DSL.py**\
    F 94:0 match_phrase - B (7)\
    F 4:0 get_articles - A (1)\
    F 14:0 get_content - A (1)\
    F 24:0 limit_articles - A (1)\
    F 33:0 object - A (1)\
    F 44:0 onlyverb - A (1)\
    F 56:0 adjective - A (1)\
    F 68:0 verbobject - A (1)\
    F 81:0 verbadjective - A (1)\

54 blocks (classes, functions, methods) analyzed.\
Average complexity: A (2.611111111111111)\



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


**Maintainability Index**

radon mi /Users/macbook/Desktop/Python_Files/NewsPoll -s
/Users/macbook/Desktop/Python_Files/NewsPoll/Newsfeeler.py - A (100.00)\
/Users/macbook/Desktop/Python_Files/NewsPoll/Preprocess.py - A (48.20)\
/Users/macbook/Desktop/Python_Files/NewsPoll/Newscounter.py - A (48.14)\
/Users/macbook/Desktop/Python_Files/NewsPoll/Visuals.py - A (50.96)\
/Users/macbook/Desktop/Python_Files/NewsPoll/Unittest_Scripts/test_Preprocess.py - A (85.51)\
/Users/macbook/Desktop/Python_Files/NewsPoll/DSL/DSL.py - A (65.97)\



| MI score | Rank | Maintainability |
|----------|------|-----------------|
| 100 - 20 | A    | Very high       |
| 19 - 10  | B    | Medium          |
| 9 - 0    | C    | Extremely low   |


**Raw metrics**
radon raw /Users/macbook/Desktop/Python_Files/NewsPoll -s
/Users/macbook/Desktop/Python_Files/NewsPoll/**Newsfeeler.py**
    LOC: 9\
    LLOC: 7\
    SLOC: 7\
    Comments: 0\
    Single comments: 0\
    Multi: 0\
    Blank: 2\
    - Comment Stats\
        (C % L): 0%\
        (C % S): 0%\
        (C + M % L): 0%\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Preprocess.py**\
    LOC: 356\
    LLOC: 226\
    SLOC: 219\
    Comments: 19\
    Single comments: 19\
    Multi: 72\
    Blank: 46\
    - Comment Stats\
        (C % L): 5%\
        (C % S): 9%\
        (C + M % L): 26%\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Newscounter.py**\
    LOC: 134\
    LLOC: 107\
    SLOC: 108\
    Comments: 2\
    Single comments: 2\
    Multi: 4\
    Blank: 20\
    - Comment Stats\
        (C % L): 1%\
        (C % S): 2%\
        (C + M % L): 4%\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Visuals.py**\
    LOC: 178\
    LLOC: 94\
    SLOC: 159\
    Comments: 9\
    Single comments: 9\
    Multi: 0\
    Blank: 10\
    - Comment Stats\
        (C % L): 5%\
        (C % S): 6%\
        (C + M % L): 5%\
/Users/macbook/Desktop/Python_Files/NewsPoll/Unittest_Scripts/**test_Preprocess.py**\
    LOC: 37\
    LLOC: 25\
    SLOC: 25\
    Comments: 4\
    Single comments: 4\
    Multi: 0\
    Blank: 8\
    - Comment Stats\
        (C % L): 11%\
        (C % S): 16%\
        (C + M % L): 11%\
/Users/macbook/Desktop/Python_Files/NewsPoll/DSL/**DSL.py**\
    LOC: 144\
    LLOC: 71\
    SLOC: 65\
    Comments: 0\
    Single comments: 0\
    Multi: 55\
    Blank: 24\
    - Comment Stats\
        (C % L): 0%\
        (C % S): 0%\
        (C + M % L): 38%\
** Total **\
    LOC: 858\
    LLOC: 530\
    SLOC: 583\
    Comments: 34\
    Single comments: 34\
    Multi: 131\
    Blank: 110\
    - Comment Stats\
        (C % L): 4%\
        (C % S): 6%\
        (C + M % L): 19%\


| Abbreviation | Explanation                                         |
|--------------|-----------------------------------------------------|
| LOC          | total number of lines of code                       |
| LLOC         | number of logical lines of code                     |
| SLOC         | number of source lines of code                      |
| comments     | number of Python comment lines                      |
| multi        | the number of lines representing multi-line strings |
| blank        | the number of blank lines                           |

**Halstead metrics**
 radon hal /Users/macbook/Desktop/Python_Files/NewsPoll
/Users/macbook/Desktop/Python_Files/NewsPoll/**Newsfeeler.py**:\
     h1: 0\
    h2: 0\
    N1: 0\
    N2: 0\
    vocabulary: 0\
    length: 0\
    calculated_length: 0\
    volume: 0\
    difficulty: 0\
    effort: 0\
    time: 0.0\
    bugs: 0.0\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Preprocess.py**:\
    h1: 9\
    h2: 84\
    N1: 52\
    N2: 105\
    vocabulary: 93\
    length: 157\
    calculated_length: 565.4839885263967\
    volume: 1026.647933343961\
    difficulty: 5.625\
    effort: 5774.894625059781\
    time: 320.82747916998784\
    bugs: 0.34221597778132035\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Newscounter.py**:\
    h1: 8\
    h2: 43\
    N1: 26\
    N2: 51\
    vocabulary: 51\
    length: 77\
    calculated_length: 257.3293844521902\
    volume: 436.7767513318052\
    difficulty: 4.744186046511628\
    effort: 2072.1501691090293\
    time: 115.11945383939052\
    bugs: 0.14559225044393506\
/Users/macbook/Desktop/Python_Files/NewsPoll/**Visuals.py**:\
    h1: 3\
    h2: 30\
    N1: 17\
    N2: 34\
    vocabulary: 33\
    length: 51\
    calculated_length: 151.96160537041902\
    volume: 257.2641000872811\
    difficulty: 1.7\
    effort: 437.3489701483779\
    time: 24.297165008243216\
    bugs: 0.0857547000290937\
/Users/macbook/Desktop/Python_Files/NewsPoll/Unittest_Scripts/**test_Preprocess.py**:\
    h1: 1\
    h2: 2\
    N1: 1\
    N2: 2\
    vocabulary: 3\
    length: 3\
    calculated_length: 2.0\
    volume: 4.754887502163469\
    difficulty: 0.5\
    effort: 2.3774437510817346\
    time: 0.1320802083934297\
    bugs: 0.0015849625007211565\
/Users/macbook/Desktop/Python_Files/NewsPoll/DSL/**DSL.py**:\
    h1: 5\
    h2: 69\
    N1: 41\
    N2: 82\
    vocabulary: 74\
    length: 123\
    calculated_length: 433.09782799213053\
    volume: 763.762763972361\
    difficulty: 2.971014492753623\
    effort: 2269.150240787449\
    time: 126.06390226596939\
    bugs: 0.254587587990787\


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