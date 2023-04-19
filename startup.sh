

sudo apt update
sudo apt -y install python3-pip
sudo apt -y install python3-venv

cd qb-oauth-python
python3 -m venv quickbooksVenv
source quickbooksVenv/bin/activate
pip install -r requirements.txt

python3 main.py

