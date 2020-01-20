


## Documenting a code

 "_Code is read much more often than it is written_." - `Guido van Rossum` (founder of Python)
 
 As code is read multiple times by your future version and potentially by many others, readable quality of a code is critical. In the [Section 3.2](weekly_materials/week3/docs/style-guide-for-python-code.md), we learnt that following a consistent style improves code readability. In this section, we will learn to clarify the purpose, functionality, and behaviour of a code using `docstring`.

A `docstring` is an abbreviation for documentation string, and describes the objects defined in your source code - i.e. what your function, module, or class does. The docstring is written as the first line of the code after the object definition. [Python Enhancement Proposal -257 (PEP 257)]() prescribes a set of standards to write a proper docstring. 


Docstring can be both `single-lined` or `multi-lined`. In both cases, docstrings should use the triple-double quote (""") string format.

`Single-lined` docstring is used to describe obvious cases. 

```python
def math_sum(var1, var2):
    """Returns the sum of two numbers."""
    return var1 + var2
```

Typing `help(math_sum)` in python console prints out the docstring for the function.
```
Help on function math_sum in module __main__:
math_sum(var1, var2)
    Returns the sum of two numbers.
```

The docstring is stored as an `__doc__` attribute of the object. Hence typing `math_sum.__doc__` returns:

```bash
'Returns the sum of two numbers.'
```

It means that the docstring can be directly manipulated with an assignment statement.

```python
math_sum.__doc__ = "Returns the addition of two numbers."
```

`Multi-lined` docstrings consist of a summary line just like a single-lined one, followed by a blank line and a more elaborate description. 

Here is an example of multi-lined docstring:

```python
def softmax(x, axis=-1):
    """Softmax activation function.
    
    Arguments
        x: Input tensor.
        axis: Integer, axis along which the softmax normalization is applied.
    Returns
        Tensor, output of softmax transformation.
    Raises
        ValueError: In case `dim(x) == 1`.
    """
 ```

## Function docstring

- Should summarize <ul> 
    - behavior
    - arguments
    - return values
    - side effects
    - exceptions raised
    - restrictions on when it can be called  
</ul>
- Should indicate optional arguments


## Class docstring

- Should summarize its behavior and list the public methods and instance variables
- Should document the class constructor in the docstring for its __init__ method
- Should document individual menthods by their own docstring.

## Module docstring

-  Should list the classes, exceptions and functions (and any other objects) that are exported by the module, with a one-line summary of each 


## Script docstring

- Should print out a message of correct number and type of arguments when invoked with incorrect ones.

- Should document the script's function and command line syntax, environment variables, and files. 

