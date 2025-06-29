# MLOps Week 4

This repository implements a basic ML workflow using the Iris dataset as part of MLOps Week 4 homework.

## Features

- Data validation to check input schema
- Model evaluation metrics
- Unit tests using `pytest`
- GitHub Actions integration for CI
- CML (Continuous Machine Learning) to comment test results on PRs

## Structure

```
├── data/
│ └── iris.csv
├── src/
│ ├── data_validation.py
│ └── model_evaluation.py
│ └── predict.py
│ └── train_model.py
├── tests/
│ ├── test_data_validation.py
│ └── test_model_evaluation.py
├── .github/
│ └── workflows/
│ └── sanity.yml
├── requirements.txt
├── README.md
└── main.py
```


## Steps

1. Install requirements:

```pyhton
pip install -r requirements.txt
```

2. Run unit tests:

```python
pytest tests/
```

3. Push to GitHub and create a PR to see GitHub Actions + CML in action.

```yml
name: Sanity Check

on: [pull_request]

permissions:
  contents: write
  pull-requests: write

jobs:
  run-tests:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Install CML
      run: |
        sudo apt-get update
        sudo apt-get install -y nodejs npm
        npm install -g @dvcorg/cml

    - name: Run tests
      run: |
        pytest tests/ > result.txt || true
        echo "## Test Results" > report.md
        echo "\`\`\`" >> report.md
        cat result.txt >> report.md
        echo "\`\`\`" >> report.md

    - name: Configure Git
      run: |
        git config --global user.email "action@github.com"
        git config --global user.name "GitHub Actions"

    - name: Comment results
      env:
        REPO_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        cml comment create --publish report.md
```

## Sample Test cases

- Validates IRIS CSV columns
- Checks accuracy metric for a dummy prediction

## Git push to dev branch

- Push all the files and code to `dev` branch
- Create a pull request to `main` branch to run github actions

## Output 

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.0, pluggy-1.6.0
rootdir: /home/runner/work/mlops-week4/mlops-week4
collected 2 items

tests/test_data_validation.py .                                          [ 50%]
tests/test_model_evaluation.py .                                         [100%]

============================== 2 passed in 0.81s ===============================
```