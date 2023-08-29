sudo apt update -y

sudo apt install python3-pip

sudo apt install python3-venv

cd qb-oauth-python

python -m venv quickbooksVenv

source quickbooksVenv/bin/activate

pip install -r requirements.txt

echo "--------------Environment ready--------------"

