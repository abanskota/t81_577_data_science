# Learning objective: 

Students will learn the utility of python programming language specifically in the context of data science and machine learning. Students will be able to install Anaconda Python distribution and manage packages using conda.


## What is Python?

- Python is a general-purpose, interpreted, dynamically typed, high-level programming language

- Python codes are easy-to-read, syntax are easy-to-learn, codes have fewer lines of code, thus have fewer bugs, and are easier to maintain.

    * General purpose: It can be used to build just about anything: frontend and backend web development, developing app and games,  server and administrative tools, scientific computing, artificial intelligence.
    * High-level: Highly abstracted from machine code.    
    * Interpreted: Code doesn't need a compiler, the python interpreter converts the code into low level machine code on the go [^1].
    * Dynamically typed: No need to define variable types.
    * Automatic memory management: No need for explicit memory allocation for variables.
   

## Why learn Python?

* Python is very conducive to rapidly prototyping and testing concepts. Its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.

* It is a great tool for interacting with interfaces, databases, APIs, and provides greater ability to automate stuffs.
* It is open-sourced and has large community of users - easy to find help and documentation.
* It has a large ecosystem of libraries and packages.
* Python has become exceptionally popular among scientists, engineers, and other researchers. Though Python itself is considered slower than other popular languages, most of the packages for scientific computation are highly optimized and written in C and Fortran.
* Python is perhaps the most suitable programming language to get started in the data science and machine learning field. 



##  What is python script?

- A text file containing python code
- The most basic way of sending instructions to the computer using python code
- Python script is normally saved with the suffix '.py'
- Python scripts are normally written with editors that provide an "integrated development environment" (IDE) for writing code. 


## Python Interpreter

The python interpreter is a program that reads and execute the python code in files passed to it as arguments. At the command prompt, the command python is used to invoke the Python interpreter.

For example, to run a file my-script.py with python codes in command line:

```shell
python my_script.py
```

Another way to start the interpreter is by simply typing python at the command line. CPython is the first Python interpreter written in the programming language C.


## Python versions


There are two general versions of python: Python 2 and Python 3. As mentioned [here](https://wiki.python.org/moin/Python2orPython3), Python 2 will be in EOL (End of Life) status and receive no further support, and Python 2 is well on its way to obsolescence. As such, this course will use Python 3.

To check the version of Python installed in your computer, run:

```shellscript
python --version
```

## Installing Python

Installing python involves installing an executable python interpreter (python.exe) and creating standard python libraries. The open-source Anaconda Distribution is the easiest way to install and manage packages on Linux, Windows, and Mac OS X. 

- Installing the Anaconda platform will install the following:

     - Python; specifically the CPython interpreter 
     - A number of very popular python libraries like matplotlib, NumPy, and SciPy.
     - Jupyter, which provides an interactive "notebook" environment for prototyping code.
     - Package managers for downloading/updating Python packages
     - An environment manager for maintaining independent installations of Python side-by-side.  

Installing Anaconda
Navigate to this page (https://www.anaconda.com/distribution/), and click the “Download” button for Python 3.

After the download is complete, begin the installation process. There will be an installation option: `Add Anaconda to the system PATH environment variable`; Enable this installation option.

The default install location for Anaconda is:

(Linux): /home/<your_username>/Anaconda3
(Windows): C:\Users\<your_username>\Anaconda3
(Mac): /Users/<your_username>/Anaconda3

## Package Management

There are two main systems for downloading and installing python packages: Conda and PIP.  Both pip and conda are included in Anaconda.


`conda` is the preferred system for managing Python package for this course. 

- Using `conda` make package management easier and [can boost the performance as well!](https://towardsdatascience.com/stop-installing-tensorflow-using-pip-for-performance-sake-5854f9d9eb0c).

- Conda packages are binaries and doesn't require compilers to install them.

To search for a specific conda package, run:
```shellscript
conda search <package-name>
```

To install the package, run
```shellscript
conda install <package-name>
```

To install specific version of the package scuh as scipy 0.15.0, run
```shellscript
conda install scipy=0.15.0
```
If a package is not available from conda or Anaconda.org,  install the package via conda-forge or with pip. Read more about installing packages [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html).

[^1]: The interpreter itself compiles the code into low-level bytecode, which is then interpreted into machine code. Go [here](https://stackoverflow.com/questions/6889747/is-python-interpreted-or-compiled-or-both) for further reading.

Further readings:

[Is Python interpreted or compiled](https://nedbatchelder.com/blog/201803/is_python_interpreted_or_compiled_yes.html)

[Module 1: Getting Started with Python](https://www.pythonlikeyoumeanit.com/module_1.html)

[Why choose Python](https://realpython.com/python-introduction/)

