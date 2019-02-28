# creation du venv
python3 -m venv venv

# installation de pex et de flask
venv/bin/pip install pex flask

# creation du pex (python executable)
venv/bin/pex . flask -c server.py -o server.pex
