#!/bin/bash
echo "Hello World"
pip install -r requirements.txt
echo "Installation complete"
echo "Running test.py"
python test.py
echo "Running the jupyter notebook"
runipy test.ipynb