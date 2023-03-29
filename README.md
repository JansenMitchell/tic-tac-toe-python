# Tic-Tac-Toe Python

Implementation of Tic-Tac-Toe in Python.

## How to run
1. Clone the repository
```bash
$ git clone git@github.com:JansenMitchell/tic-tac-toe-python.git
```
2. In the root directory, run the following command
```bash
$ python tic_tac_toe.py
```

## How to test
1. Comment out the following line in `tic_tac_toe.py`
```python
game_loop()
```
2. In the root directory, run the following command
```bash
$ python -m pytest -s test_tic_tac_toe.py
```
3. Enter a number from 0 to 8 to simulate a move.