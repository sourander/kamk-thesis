# Thesis - Playground

This repository is a collection of scripts used while writing my thesis. Instead of running Spark on Databricks clusters or on MacBook Pro, I ran this project on my Windows 10 laptop due to better support for Office 365 package. Nevertheless, the code should be cross-OS supported.

Most of the code is in Jupyter Notebook files and can be browsed without running anything locally. Thus, have fun browsing!

## How to run the code?

To run the code, you will need Spark. A standalone Spark can be installed on Windows machine by:
* Install [Oracle Java 8](https://java.com/en/download/)
  * Make sure java is in PATH by running `java -version` in command prompt.
* Download [Apache Spark](https://spark.apache.org/downloads.html)
  * Version used: *Spark 3.1.1 Pre-Built for Hadoop 3.2 and later*
  * Extract to wherever you want your SPARK_HOME 
    * e.g. `D:\spark\spark-3.1.1-bin-hadoop3.2\`
* Download the matching version of [Winutils.exe](https://github.com/cdarlint/winutils/tree/master/hadoop-3.2.1/bin)
  * Move the exe to `HADOOP_HOME\bin`
* Set Windows Environment Variables: 
  * SPARK_HOME to path above
  * HADOOP_HOME to path SPARK_HOME\hadoop\
    * Test: `echo %SPARK_HOME%`
    * Test: `echo %HADOOP_HOME%`

Also, make sure your `sys.path` includes `SPARK_HOME\python` location. If you use PyCharm, this can be added in the [Settings](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-reloading-interpreter-paths.html). Alternatively, you can add it by defining PYTHONPATH environment variable or by inserting the path using sys.path.insert() function in the beginning of your code.

When you initialize the SparkSession, it downloads the Delta Lake jars from Maven. There is no need to download those manually.