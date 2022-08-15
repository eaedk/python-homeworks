# Python Homeworks

## Description

This repository contains homeworks you shoud take. It will help you for the imcoming python assessment.

## Setup
Install the required packages to be able to run the evaluation locally.

You need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: > ...`  follow the steps below:

- Windows:
        
        python3 -m venv venv; venv\Scripts\activate; python -m pip install --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install --upgrade pip; python -m pip install -qr requirements.txt  

## Evaluation
This evaluation will be automatically grade, so please follow the instructions carefully. 

You can run this command bellow being at the root of the repository to be sure your solutions are the good ones before to push your solutions.
```command
python -m pytest -v
```

```command
python -m pytest -v <exercise_name>/tests
```
