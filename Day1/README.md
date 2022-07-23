
# Day 1 - Pytest

---
> #### Pytest is python based testing framework. It is used for write and execute test cases. 
> ####  Pytest requires: Python 3.7+ or PyPy3.
> #### It is open source. It supports parallel execution. 
> ####  Run the following command in your command line to install pytest. 
>>> ### ```pip install -U pytest```
>>> ### ```pytest --version```
---

# Create your first test.
> ###  Create a new file called test_sample.py, containing a function, and a test.
  ``` py
  # content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```
> ### To tun the test case just run the pytest  command into cmd or terminal.
> ### pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.More generally, it follows standard test discovery rules.
---

# Conventions for Python test discovery.
> ### pytest implements the following standard test discovery.
> ###  If no arguments are specified then collection starts from testpaths (if configured) or the current directory. Alternatively, command line arguments can be used in any combination of directories, file names or node ids.
> ###  Recurse into directories, unless they match norecursedirs.
> ### In those directories, search for test_*.py or *_test.py files, imported by their test package name.
> ### From those files, collect test items:
>  ### &emsp;  test prefixed test functions or methods outside of class.
>  ### &emsp;test prefixed test functions or methods inside Test prefixed test classes (without an __init__ method).
>  ### For test discovery test_*.py or *_test.py naming convention is must for .py file, and it is applicable for test function as well.
---
# Specifying which tests to run.
> ### Pytest supports several ways to run and select tests from the command-line.
> ### Run tests in a module
>>> ### ```pytest test_mod.py```
> ### Run tests in a directory
>>>### ```pytest testing/```
> ### Run tests by keyword expressions
>>>### ```pytest -k "MyClass and not method"```
>> #### This will run tests which contain names that match the given string expression (case-insensitive), which can include Python operators that use filenames, class names and function names as variables. The example above will run TestMyClass.test_something but not TestMyClass.test_method_simple.
> ### Run tests by node ids
> #### Each collected test is assigned a unique nodeid which consist of the module filename followed by specifiers like class names, function names and parameters from parametrization, separated by :: characters.
> #### To run a specific test within a module:
>>> ### ```pytest test_mod.py::test_func```
> #### Another example specifying a test method in the command line:
>>> ### ```pytest test_mod.py::TestClass::test_method```
> #### Run tests by marker expressions
>>> ### ```pytest -m slow```
> #### Will run all tests which are decorated with the @pytest.mark.slow decorator.
> #### Run tests from packages
>>> ### ```pytest --pyargs pkg.testing```
> #### This will import pkg.testing and use its filesystem location to find and run tests from.




