# setup virtual environment
python3 -m venv venv
. venv/bin/activate #or run: source  venv/bin/activate

#install boto3
pip install boto3

save dependecies in requirements.txt
pip freeze > requirements.txt

to install dependencies:
pip install -r requirements.txt