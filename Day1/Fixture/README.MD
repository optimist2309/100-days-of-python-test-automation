# Fixtures

---
> #### pytest fixtures are functions attached to the tests which run before the test function is executed. Fixtures are a set of resources that have to be set up before and cleaned up once the test automation execution is completed.
> #### pytest fixture function is automatically called by the pytest framework when the name of the argument and the fixture is the same.
>  #### A function is marked as fixture using the following marker:-  ```@pytest.fixture```
> #### Below is example of fixture. 
``` py
import pytest 

@pytest.fixture
def fixture_func():
   return "fixture test"
def test_fixture(fixture_func):
    assert fixture_func == "fixture test"
```