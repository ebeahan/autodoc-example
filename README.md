Autodoc Example
===============

Basic repo demostrating how to generate documentation using the sphinx
package with a simple Python project.

#### Requires:
Sphinx 1.5a1

#### Usage
Use the following instructions to automatically build HTML documentation
from the repo.

```py
pip install sphinx
cd docs
make html
cd _build/html
python -m SimpleHTTPServer
```
