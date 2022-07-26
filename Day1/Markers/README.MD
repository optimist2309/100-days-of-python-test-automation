# Markers

---
> #### PyTest allows us to use preset or create custom attributes for the test methods using PyTest markers.
> #### Grouping of tests is an effective way to perform testing because it helps us to execute or skip certain tests based on criteria.
> #### There are two types of markers.
> #### &nbsp; &nbsp; &nbsp; &nbsp;  1. Built-in Markers
> #### &nbsp; &nbsp; &nbsp; &nbsp;  2. Custom Markers
> #### To use markers, first import pytest in the test file and add the marker just above the test declaration.
>#### Syntax to set a marker.
> ### ```@pytest.mark.<marker-name>```
>#### Command to run a marker.
> ### ```pytest -m <marker-name>```
----
# Example of custom markers.

---
 ``` py
import pytest 
 
@pytest.mark.smoke 
def test_smoke1():
    assert 20 == 23

@pytest.mark.smoke 
def test_smoke2():
    assert 23 == 23

@pytest.mark.regression
@pytest.mark.smoke 
def test_smoke3():
    assert 100 == 23

@pytest.mark.regression
def test_rig3():
    assert 10009 == 23
    
# We can run test cases as per our grouping need with command pytest -m <marker-name>  
```
> #### When using custom markers in PyTest we need to register them before using otherwise will get below error.
> #### PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
> #####    @pytest.mark.regression-- Docs: https://docs.pytest.org/en/latest/warnings.html

----
# Registering markers.

---
> #### You can register custom marks in your pytest.ini file like this.
``` py
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial

```
> #### or in your pyproject.toml file like this.
``` py
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "serial",
]
```
> #### Note that everything past the : after the mark name is an optional description.

> #### Alternatively, you can register new markers programmatically in a pytest_configure hook.
``` py
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )
```
> #### Registered marks appear in pytest’s help text and do not emit warnings.

----

# Example of Built-in Markers.

---
> #### You can list all the markers, including builtin and custom, using the CLI - pytest --markers.
> #### @pytest.mark.filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/stable/how-to/capture-warnings.html#pytest-mark-filterwarnings
> #### @pytest.mark.skip(reason=None): skip the given test function with an optional reason. Example: skip(reason="no way of currently testing this") skips the test.
> #### @pytest.mark.skipif(condition, ..., *, reason=...): skip the given test function if any of the conditions evaluate to True. Example: skipif(sys.platform == 'win32') skips the test if we are on the win32 platform. See https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-skipif
> #### @pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=xfail_strict): mark the test function as an expected failure if any of the conditions evaluate to True. Optionally specify a reason for better reporting and run=False if you don't even want to execute the test function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a true failure. See https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-xfail
> #### @pytest.mark.parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.see https://docs.pytest.org/en/stable/how-to/parametrize.html for more info and examples.
> #### @pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures. see https://docs.pytest.org/en/stable/explanation/fixtures.html#usefixtures 
> #### @pytest.mark.tryfirst: mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible.
> #### @pytest.mark.trylast: mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible.

----

# Skipping test functions.

---
> #### The simplest way to skip a test function is to mark it with the skip decorator which may be passed an optional reason.
``` py
import pytest 

@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():

```
> #### Alternatively, it is also possible to skip imperatively during test execution or setup by calling the pytest.skip(reason) function:
``` py
def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")

```
> #### The imperative method is useful when it is not possible to evaluate the skip condition during import time.
> #### It is also possible to skip the whole module using pytest.skip(reason, allow_module_level=True) at the module level:
``` py
import sys
import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)

```
----

# Skipping test cases on some conditions.

---
> #### If you wish to skip something conditionally then you can use skipif instead. Here is an example of marking a test function to be skipped when run on an interpreter earlier than Python3.10:
``` py
import sys
import pytest 

@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_function():
    
```
> #### If the condition evaluates to True during collection, the test function will be skipped, with the specified reason appearing in the summary when using -rs.
> #### If you want to skip all test functions of a module, you may use the pytestmark global.

``` py
# test_module.py
# Skip all tests in a module unconditionally:
pytestmark = pytest.mark.skip("all tests still WIP")

# Skip all tests in a module based on some condition:
pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
# If multiple skipif decorators are applied to a test function, it will be skipped if any of the skip conditions is true.

#Skip all tests in a module if some import is missing:
pexpect = pytest.importorskip("pexpect")
   
```

----

# Mark test functions as expected to fail.

---

> #### You can use the xfail marker to indicate that you expect a test to fail.
``` py
# test_module.py
import pytest 
@pytest.mark.xfail
def test_function():
    ...
  
```
> #### This test will run but no traceback will be reported when it fails. Instead, terminal reporting will list it in the “expected to fail” (XFAIL) or “unexpectedly passing” (XPASS) sections.
> #### Alternatively, you can also mark a test as XFAIL from within the test or its setup function imperatively:
``` py
# test_module.py
import pytest 

def test_function():
    if not valid_config():
        pytest.xfail("failing configuration (but should work")

def test_function2():
    import slow_module

    if slow_module.slow_function():
        pytest.xfail("slow_module taking too long")
           
```
> #### These two examples illustrate situations where you don’t want to check for a condition at the module level, which is when a condition would otherwise be evaluated for marks.
> #### This will make test_function XFAIL. Note that no other code is executed after the pytest.xfail() call, differently from the marker. That’s because it is implemented internally by raising a known exception.

> ## Condition parameter.
> #### If a test is only expected to fail under a certain condition, you can pass that condition as the first parameter.
``` py
# test_module.py
import pytest 

@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_function():
    ...
           
```
> #### Note that you have to pass a reason as well.

> ## Reason parameter.
> #### You can specify the motive of an expected failure with the reason parameter.
``` py
# test_module.py
import pytest 

@pytest.mark.xfail(reason="known parser issue")
def test_function():
    ...
           
```

> ## Raises parameter.
> #### If you want to be more specific as to why the test is failing, you can specify a single exception, or a tuple of exceptions, in the raises argument.
``` py
# test_module.py
import pytest 

@pytest.mark.xfail(raises=RuntimeError)
def test_function():
    ...
           
```
> #### Then the test will be reported as a regular failure if it fails with an exception not mentioned in raises.

----

# Parametrizing test functions.

---
> #### The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function. Here is a typical example of a test function that implements checking that a certain input leads to an expected output:

``` py
# test_module.py
import pytest 

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
           
```
> #### Here, the @parametrize decorator defines three different (test_input,expected) tuples so that the test_eval function will run three times using them in turn.
>  #### Parameter values are passed as-is to tests (no copy whatsoever).
>  #### For example, if you pass a list or a dict as a parameter value, and the test case code mutates it, the mutations will be reflected in subsequent test case calls.
>  #### It is also possible to mark individual test instances within parametrize, for example with the builtin mark.xfail:

``` py
# test_module.py
import pytest 

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
               
```
