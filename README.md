# LEA Budget Balance Tracking
Data extraction, cleaning, and manipulation to track budget line items and campus budgets from PDFs exported from accounting software using the tabula-py package.

The tabula-py package is a wrapper of [tabula-java](https://github.com/tabulapdf/tabula-java) and requires java on your machine. I recommend installing [OpenJDK](https://jdk.java.net/22/) and setting the **JAVA_HOME** and **PATH** enivronment variables in python using the os package which creates an instance of the JAVA_HOME and PATH variables. For a more permanent instance set the environment variables in the command prompt (Windows) or terminal (Mac)

- The **JAVA_HOME** variable points to the installation location of OpenJDK
- The **PATH** varible points to the location of the Java Virtual Machine (JVM DLL)
