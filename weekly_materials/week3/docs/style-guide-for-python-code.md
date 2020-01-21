 "_Code is read much more often than it is written_." - `Guido van Rossum` (founder of Python)
 
 As code written by you is read multiple times by your future version and potentially by many others, readability of code is critical. Readability of a code can be improved upon by following a consistent style through out a code base. Python Enhancement Proposals - 008 ([PEP 8](https://www.python.org/dev/peps/pep-0008/)) provides guidelines and best practices on how to maintain style consistency. Here are the list of some common ones.
 
 
**Indentation**

Use 4 spaces per indentation level. Use `spaces` instead of `tab` while indenting.

```python
def square_num(x):
    return x*x
```

**Line length**

- Limit line to 79 characters, but don't fret over the exact length. 
- Wrap comments and docstrings into 72 characters.
- Use only one statement per code line

 
**Naming**


- Names to Avoid <ul> 
    - Avoid single letter variable name such as `l`, `c` 
</ul>
  
- Variables, functions, methods <ul> 
    - `lower_case_with_underscores` 
</ul>

- packages, modules <ul>
    - `lower_case` <br>
    - `lower_case_with_underscore` only if improves readability
</ul>

- Classes and Exceptions <ul>
    - `CapWords`
</ul>

- Protected methods and internal functions <ul>
    - `_single_leading_underscore(self, ...)`
</ul>

- Private methods <ul>
    - `__double_leading_underscore(self, ...)`
</ul>

- Constants <ul>
    - `ALL_CAPS_WITH_UNDERSCORES`
 </ul>
    
- Function and Method Arguments <ul>
    - Always use `self` for the first argument to instance methods.
    - Always use `cls` for the first argument to class methods.

</ul>

**Imports**

- Use `import x` for importing packages and modules.
- Use `from x import y` where x is the package prefix and y is the module name with no prefix.
- Use `from x import y as z` if two modules named y are to be imported or if y is an inconveniently long name.
- Use `import y as z` only when z is a standard abbreviation (e.g., np for numpy).
 
**Exceptions**
- When catching exceptions, mention specific exceptions whenever possible instead of using a bare except: clause

```python
try:
    with open('example.txt') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
```

**Global variables**
- Avoid global variables.

**Default Arguement**
- Don't use mutable object as default values in the function definition

```python
def foo(a, b=[]):
    .....
```
**True False evaluation**

- Use the “implicit” false

`if foo: rather than if foo != []:`

` if foo is None: (or is not None)`

- Never compare a boolean variable to False using ==. Use `if not x:` instead. 

- Use `if seq:` and `if not seq:` instead of `if len(seq)`: and `if not len(seq)` for sequences


**References:**

[Best of the Best Practices" (BOBP) guide to developing in Python](https://gist.github.com/sloria/7001839)<br>
[Google Python Style Guide](http://google.github.io/styleguide/pyguide.html)<br>
[PEP 8](https://www.python.org/dev/peps/pep-0008/)
[THe Elements of Python Style](https://github.com/amontalenti/elements-of-python-style)
