## Top ten coding best-practices in data science

Data scientists typically struggle when it comes to writing elegant and reproducible codes. We mostly work with proof-of-concept mindset at least in the early life cycle of the project. Automation and productionalization are the last things we worry about when we are busy running experiments on prototypes. However, having a production mindset and following the best coding practices even during the exploration and experimental phases could pay a lot of dividends. At minimum, it allows for timely identification of bugs in the code, improves reproducibility, and foster better communication among team members. Furthermore, it enables smooth integration of your model into production and facilitates easy handover of the project. 


### 1. Start a code repository with version control right off the bat.

Version control is a systematic way of keeping track of changes in files. It is an important part of code development. It gives us a peace of mind, provides an ability to go back and forth between versions, prevents loosing or writing over files, helps find bugs, and allows collaborating with others in a project. It is recommended to start version controlling your code right from the outset and keep committing and pushing the codes in a short and regular interval. I have written [here](version-control.md) a brief introduction to version control and on how to get started with git and GitHub.

### 2. Create a well-defined project structure.

A data science project is an iterative process of extracting data, preprocessing, model training, and model evaluation. Multiple experiments are run with various methods and subsets of data. Having the folders structure for codebase and data mirrored with the processing and modeling steps helps automate such experiments in an efficient manner.

A well-defined structure also enhances replicability and reproducibility of the outcomes of your analysis. A new team member can swiftly understand the project at a higher level without digging into extensive documentation. It also improves the search process for specific code components as someone doesn't need to go through everything before knowing where to look for very specific things. Well organized code tends to be self-documenting as the organization itself provides the contexts for the codes.

The package `cookiecutter` provides an easy way of creating a project structure using a standard template. Learn more about the data science project structure using the package [here](https://drivendata.github.io/cookiecutter-data-science/) and an example and description of the implementation of such project [here](https://medium.com/swlh/how-to-structure-a-python-based-data-science-project-a-short-tutorial-for-beginners-7e00bff14f56).


### 3. Create a  readable README document.

A README document is often kept in the root directory of the project and is written in Markdown language. The README file provides others the first glimpse into what your work is about. It should typically contain a project summary, project dependencies, installation instructions, and example codes. Visit this [site](https://github.com/sfbrigade/data-science-wg/blob/master/dswg_project_resources/Project-README-template.md) to learn more about what a typical README looks like for a data science project and to download a template for the document.


### 4. Work inside a virtual environment.

A virtual environment is an isolated environment that maintains a clean installation of Python packages and resolves project dependencies. It also helps others recreate the same environment in their computer quickly and in a hassle-free manner. Visit this [site](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to learn how to create a virtual environment with Conda or [here](https://realpython.com/python-virtual-environments-a-primer/) with virtualenv package.


### 5. Adopt a consistent coding style.

Data scientists are not renowned for writing readable codes. However, code readability in data science is very important as they are read multiple times by your future version and potentially by others. One way of improving the readability is by following a consistent style throughout a code base. I have summarized [here](style-guide-for-python-code.md) some guidelines and the best practices on how to maintain style consistency and added some useful references to the topic at the end of the article.

### 6. Document your code.

Documenting code is describing the purpose,  behaviour, and the use of a code to the potential users. An important rule to remember is that both the code and documentation should live in the same place. Python provides a convenient way of combining the two through  `docstring` -  an abbreviation for documentation string that describes functions, classes, and modules in your source code. I have summarized [here](documenting-python-code.md) a set of standards to write a docstring based upon the guidelines by PEP-256.

### 7. Embrace modularity in your code.

Modular programming is the process of breaking up a large body of code into smaller chunks in the form of functions and modules. Modularity helps in managing code complexity, facilitate easier debugging, and ensures the reusability of the codes. One way of achieving modularity in Python is by writing function that only does a single thing to input. Another way is to split the code into modules and group functions in a logical manner in each module. For example, separate modules could be written for importing data, preprocessing, training, and evaluation of a model. 


### 8. Optimize your code for performance.

The goal of code optimization is to make code perform better such that it uses the least possible memory or disk space, minimizes CPU time, and runs faster. Sometimes, it could just mean utilizing as many possible CPU cores as available to make your code run faster. In projects with a very large dataset, writing a CPU and memory efficient code could be critical for quick prototyping. This [article](https://e2eml.school/code_optimization.html) by Brandon Rohrer summarizes some excellent general tips for running codes faster. Additionally, pay attention to library specific tips and tricks such as working with a huge file in Pandas and when to switch from Pandas dataframe to Numpy array based analysis etc. 


### 9. Perform unit testing.

The goal of a software testing is to find bugs and get them fixed. Unit testing is a way of testing individual pieces of code(such as function) in isolation with the rest of the components. It is required to ensure quality control such that your code would not cause unexpected impact and works properly before deployment to a production environment. Writing modular codes as discussed above facilitate better implementation of unit testing. There are many packages in Python for automated unit testing;`Unittest` and `pytest` are the two most common ones. 


### 10. Integrate logging with your codes.

Logging is recording useful information during runtime for the identification of bugs and critical failures and performance improvement. Logging provides better insight into  the flow of a program and discover unforeseen consequences. It also helps others understand what your code actually does and whether it behaves in the intended way. The`logging` module in the standard library provides an easy and flexible way for emitting log messages from Python programs.
