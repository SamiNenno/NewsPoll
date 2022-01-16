![alt text](https://github.com/SamiNenno/NewsPoll/blob/master/Images/Party_Newspaper_vs_Poll.png)


# NewsPolls


Compares news coverage of German politicians/parties to election polls.

All core scripts can be found [here](Scripts). Note that due to time constraints, I could not finish the Newsfeeler.py
that would classify the sentiment towards specific politicians/parties. Newscounter.py, however, works just
fine. You can use it to compare mentions and poll results of specific politicians/parties as displayed in the
plot above and below.


**1.** Use and understand Git!\

**2.** UML at least 3 good diagrams. "good" means you can pump it up artificially as written in DDD. You have 10 million $ from me! Please export the pics. I can not install all tools to view them!\
    *-->* [see folder UML](UML) I have chosen Class Diagrams, Object Diagrams, and Use-case Diagrams

**3.** DDD If your domain is too small, invent other domains around and document these domains (as if you have 10 Mio € from Edlich-Investment!) Develop a clear strategic design with mappings/relationships with 5-0 Domains. It would be nice if these domains are derived from an Event-Storming (but not mandatory).\

**4.** Metrics at least two. Sonarcube would be great. Other non trivial metrics are also fine.\
    *-->* [see folder Metrics](Metrics) I have chosen radon as a tool for metrics. Radon is a python library
    for cyclomatic complexity, Halstead metrics, and others. More information and documentation of the tests
    can be found [here](https://github.com/SamiNenno/NewsPoll/blob/1a93daafec718cc3cc2b9b5444f3245fee97510c/Metrics/Metrics_Summary.md)

**5.** Clean Code Development: at least 5 points you can show me + >>10 points on your personal cheat sheet\
    *-->* [see folder CleanCode](CleanCode) Explanation can be found in the same folder or [here](https://github.com/SamiNenno/NewsPoll/blob/56fd9289c56c24ce1abfff076c4628915275760b/CleanCode/WhyIsThisCleanCode.txt)

**6.** Build Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc.\
    *-->* I chose [Pybuilder](https://pybuilder.io/) as a build management tool. The tool is specifically designed for python
    and allows to integrate libraries such as flake8 and it performs unit test. You can find the results of the successful build [here](https://github.com/SamiNenno/NewsPoll/blob/master/Pybuilder_doc.txt).
    

**7.** Integrate some nice Unit-Tests in your Code to be integrated into the Build\
    *-->* [see folder Unittest_Scripts](Unittest_Scripts). I have written some unit-tests for the Preprocess.py
    script. Since Preprocess.py is mostly concerned with scraping and loading the poll and newspaper data
    the unit tests make sure that the loaded/scraped data has the right format.

**8.** Continuous Delivery: show me your pipeline in e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc.\
    *-->* [see folder CICD](CICD). I have chosen Circle-CI as a tool. Circle-CI automatically calls flake8 (python library for style checking)
    pytest, and my self-modelled unit tests.

**9.** Use a good IDE and get fluent with it as e.g. IntelliJ. What are your favorite Key-Shortcuts?!\
    *-->* Pycharm: Probably, ^+alt+r for run, cmd+k for commit, shift+cmd+K for push
        Furthermore, it is helpful to add big data files to the gitignore file (no shortcut, though)*

**10.** DSL Create a small DSL Demo example snippet in your code even if it does not contribute to your project\
    *-->* I have chosen Regular Expressions as DSL. [See folder DSL](DSL). I have implemented a function
    that allows to search through the news corpus. The searchphrase is modelled as a natural sentence with a
    common syntax like subject-verb-object or subject-adjective. You can see some example results as csv files.

**11.** Functional Programming (prove that you have covered all functional aspects in your code as\
    *-->* only final data structures\
    *-->* (mostly) side effect free functions. See [Newscounter.py](Newscounter.py) "relative_count()"\
    *-->* the use of higher-order functions. See [Newscounter.py](Newscounter.py) "relative_count()"\
    *-->* functions as parameters and return values. See [Newscounter.py](Newscounter.py) "relative_count()"\
    *-->* use closures / anonymous functions. See Lambda Function in [Newscounter.py](Newscounter.py) "datecasting()"\



![alt text](https://github.com/SamiNenno/NewsPoll/blob/master/Images/Party_Newspaper.png)

![alt text](https://github.com/SamiNenno/NewsPoll/blob/master/Images/Party_Poll.png)

![alt text](https://github.com/SamiNenno/NewsPoll/blob/master/Images/Merkel.png)

![alt text](https://github.com/SamiNenno/NewsPoll/blob/master/Images/Laschet_Scholz_Baerbock.png)

![alt text](https://github.com/SamiNenno/NewsPoll/blob/master/Images/Scholz_vs_SPD.png)

![alt text](https://github.com/SamiNenno/NewsPoll/blob/master/Images/Baerboch_vs_Gruen.png)

![alt text](https://github.com/SamiNenno/NewsPoll/blob/master/Images/Laschet_vs_CDU.png)
