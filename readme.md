# Python Homeworks

## Description

This repository contains homeworks you shoud take. It will help you for the imcoming python assessment.

# Assignments
Find the list of the assignment to do bellow:
- [Umbrella](/umbrella/)

## Setup
Install the required packages to be able to run the evaluation locally.

You need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: > ...`  follow the steps below:

- Windows:
        
        python3 -m venv venv; venv\Scripts\activate; python -m pip install --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol **;** but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

## Evaluation
This evaluation will be automatically grade, so please follow the instructions carefully. 

You can run this command bellow being at the root of the repository to be sure your solutions are the good ones before to push your solutions.

Be sure the virtual environment `venv` is activated then thype the command bellow: 

```command
python -m pytest -v
```

```command
python -m pytest -v tests/<exercise_name>
```
