# Nine best-practices

## 1. Start a code repository and version control of the project right off the bat.

 
Code repository and version control keep and track changes in the code and other files. They are also excellent collaboration tools. Version control with git and GitHub repositories will be covered in detail in the [section 3.1]().

## 2. Create a well-defined project structure


As we will learn in the upcoming weeks, most data science /machine learning projects follow sequential steps from extracting data, preprocessing, model training, and model evaluation. These are iterative steps: we run the experiment multiple times with different samples of data and various methods. Having the folders structure for codebase and data mirrored  with the processing and modeling pipeline will help automate such experiments.

A well-defined project structure also improves project comprehension and thus enhances replicability and reproducibility. A new team member can swiftly understand the project at a higher level without digging in to extensive documentation. It also improves search process for specific code components as someone doesn't need to go through everything before knowing where to look for very specific things. Well organized code tends to be self-documenting as the organization itself provides the contexts for the codes.

The package `cookiecutter` provides an easy way of creating a standard project template. Learn more about the data science project structure using the package [here](https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/0_before_you_start/pipelines-and-project-workflow) and an example and description of the implementation of such project [here](https://medium.com/swlh/how-to-structure-a-python-based-data-science-project-a-short-tutorial-for-beginners-7e00bff14f56).


## 3. Create a readable README document that describes the overall objective of the project and codebase with example. 

The README documents are often kept in the root directory of the project repository and are often rendered with Markdown language. It typically contains a project summary, requirements and installation instructions, and example codes. A README document is essential for the completeness of any python based data science project.


## 4. Create a virtual environment for the project

A virtual environment is an isolated python environment that maintains and resolve all dependencies required by the project independent of other projects and python environment. It helps to manage a clean installation of a project-specific version of python packages and allow the usage of some packages and version of the packages that might conflict with other packages installed with the base python. On top of that, it helps others to recreate the same environment quickly and in a hassle-free manner to run the project in their computing environmnt. Click [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to learn how to create a virtual environment with Conda and [here](https://realpython.com/python-virtual-environments-a-primer/) with virtualenv package.


## 5. Adopt a Consistent Coding Style by following style guidelines

This is covered in [Section 3.2]()

## 6. Embrace modularity in your code

Modular programming is the process of dividing a computer program into separate sub-programs based upon functionality. Modularity helps in managing code complexity, facilitate easier debugging, and ensures the reusability of the parts of the codes in the same or different projects. 

In python, modularity can be achieved by breaking a large body of code into smaller, more manageable chunks or functions. A module is just another file containing legitimate code and with a name with .py extension. Generally, a module contains a grouping of similar functions or classes. The module can be imported in a similar way as python package in your python script by using import statement. In fact, a python package is just a collection and organization of modules as module are to the functions.

Click [here](https://www.python-course.eu/modules_and_modular_programming.php) for further readings about creating a module and [Real Python](https://realpython.com/python-modules-packages/#python-modules-overview) for a detailed overview about module and packages.



## 7. Integrate logging with your codes

Logging is recording useful information from the code execution for identification of bugs and critical failures and performance improvement. Basically, logging provides the insight on what and how your code is doing. It can provide better understanding of the flow of a program and discover unforeseen consequences. It also allows other people to see what your code acutally does and whether it behaves in the intended way. Python provides an inbuilt module named `logging`, which is a ready-to-use and powerful tool that meets the needs of beginners as well as enterprise teams.  



## 8.  Optimize your code for performance

The most common goal of code optimization is to make python code run faster and in other times to reduce memory usage. In data science projects with very large dataset, code speed and memory usage can be huge bottlenecks for quick prototyping. Dataset could be very large even for distributed systems and servers with high memory and compute process; and can significantly slow down the runtime of a code. While there are packages-specific best-practices that we will go over for pandas and numpy in Week 5, some tricks and tips for general python programming can be found [here](https://www.geeksforgeeks.org/optimization-tips-python-code/) and [here](https://www.techbeamers.com/essential-python-tips-tricks-programmers/).


## 9. Perform unit testing

The goal of a software testing is to find bugs as early as possible and get them fixed. Unit testing is a way of testing individual pieces of code(unit) in isolation with the rest of the components. A unit could be an entire module or a single class or function. It’s a longstanding best practice for building software. Data science works typically involve writing custom functions for data preparation in addition to calling standard libraries. It is the best practice to develop a habit to integreate unit testing for custom functions even for exploratory work. Writing modular codes discussed above ensures better implementation of unit testing. `Unittest` and `pytest` are two popular python packages for automated testing. Go to this (youtube video)[https://www.youtube.com/watch?v=l32bsaIDoWk] to learn how to perform unitesting using `pytest`. Read more [here](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/) for an elaborative explanation of unit testing.

