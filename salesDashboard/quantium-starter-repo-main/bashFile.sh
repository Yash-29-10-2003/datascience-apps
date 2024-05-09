##!/bin/bash

. ./venv/Scripts/activate

python -m dashTest.py

# exit code is 0 if all tests pass
PYTEST_EXIT_CODE=$?

# return exit code 0 if all tests pass or 1 otherwise
if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi