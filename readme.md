To create and use the virtual environment 
python3 -m venv env

source env/bin/activate


use linter
pytest --pylinte



Make from scratch

python3 -m venv env
source env/bin/activate
pip install pytest pytest-pylint
pip freeze > requirements.txt



use python-faker-library to test
from faker import Faker
