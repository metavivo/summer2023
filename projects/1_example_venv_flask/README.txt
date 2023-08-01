mkdir test-project
cd test-project

python -version
python --version
whereis python3
ls -as /usr/bin/python*
python3.8

python3.8 -m venv venv

bash
source venv/bin/activate
deactivate
exit

bash
source venv/bin/activate
pip list

python3.8
import numpy
print(numpy.__version__) 

File tests/imports-test.py:
#!/usr/bin/env python3
import numpy as np
print(np.__version__) 


tests/imports-test.py

pip freeze

pip freeze > requirements.txt


mkdir duplicate-project
cp -r test-project/* duplicate-project
cd duplicate-project
\rm -fr venv


cd duplicate-project
python3.8 -m venv venv
bash
source venv/bin/activate
pip install -r requirements.txt

tests/imports-test.py
