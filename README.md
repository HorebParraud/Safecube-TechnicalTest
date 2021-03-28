# Safecube-TechnicalTest

### Built With
* Python 3.8

#### Python dependancies `requirement.txt`
###### essential for running main.py
* **`haversine`** *Calculate the distance (in various units) between two points on Earth using their latitude and longitude*
* **`requests`** *simple HTTP library, need in revercegeocoding.py*
* **`requests_oauthlib`** *first-class OAuth library support for Requests*

> simply run `./main.py`, no need for parameters

###### not ettential but used in this project
* **`pycodestyle`** *tool to check Python code against some of the style conventions in PEP 8*
* **`pytest`** *Python testing tool*
* **`coverage`** *a tool for measuring code coverage of Python programs*
* **`pytest-cov`** *plugin produces coverage reports*

###### use pytest with coverage
```bash
> pytest --cov=sources test_*.py

Name                          Stmts   Miss  Cover
-------------------------------------------------
sources/__init__.py               0      0   100%
sources/revercegeocoding.py      19      1    95%
sources/stop.py                  16      0   100%
sources/trackpoints.py           62     15    76%
-------------------------------------------------
TOTAL                            97     16    84%
```