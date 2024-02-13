# 3 Levels Of Calculator Homework

## Key Commands:

1. **Installation:**
    ```sh
    pip3 install virtualenv
    ```

2. **Activating Virtual Environment:**
    ```sh
    source venv/bin/activate
    ```

3. **Installing Dependencies:**
    ```sh
    pip3 install -r requirements.txt
    ```

4. **Updating Requirements File:**
    ```sh
    pip3 freeze > requirements.txt
    ```

## Testing Commands:

- Run tests without pylint or coverage:
    ```sh
    pytest
    ```

- Run tests with pylint static code analysis:
    ```sh
    pytest --pylint
    ```

- Run tests, pylint, and coverage to ensure all code is tested:
    ```sh
    pytest --pylint --cov
    ```

- Run tests with a specified number of records (e.g., 10):
    ```sh
    pytest --num_records=10
    ```

