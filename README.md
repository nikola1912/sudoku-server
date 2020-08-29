# sudoku-server

### Virtual Environment

- Activate virtual environment by running `venv/Scripts/activate`
- On VS Code you can just open a new terminal, the venv will be activated automatically
- Deactivate virtual environment by running `deactivate`

### Environment Variables

- Change environment variables in `.flaskenv` and `.env` files
- `.flaskenv` should be used for public variables, such as `FLASK_APP`, while `.env` should be used for private variables, such as API keys
- `.env` should never be commited

### Packages

- Install new packages by running `pip install <package_name>`
- When a new package is installed, run `pip freeze` and copy the output to the `requirements.txt` file
- Install all the packages from the `requirements.txt` file by running `pip install -r requirements.txt`

### Setup

- Activate virtual environment
- Install required packages
- Start the server by running `flask run`
- Stop the server by doing `CTRL+C` in the terminal
