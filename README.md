# Integer Sequence Filter

This Python program accepts a sequence of integers, filters the list based on certain criteria, and prints the result.

## Files

1. **main.py:** Contains the main program logic.
2. **tests.py:** Includes test functions for the utility functions.
3. **utils.py:** Provides utility functions, such as `filter_list`, for processing integer sequences.

## How to Run

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Run the main program:

    ```bash
    python main.py
    ```

3. Enter a sequence of integers separated by space when prompted.

## File Descriptions

### main.py

The main program file that takes user input, processes it, and prints the filtered list. It uses the `filter_list` function from `utils.py`.

### tests.py

Includes test functions for ensuring the correctness of the utility functions in `utils.py`.

### utils.py

Contains utility functions, such as `filter_list`, which processes a list of integers by removing items at positions that are multiples of 2 or 3.

## Usage

1. Run the main program and enter a sequence of integers.
2. The program will process the input and print the filtered list.

## Example

```bash
python main.py
Enter a sequence of integers separated by space: 1 2 3 4 5 6 7 8 9 10

[1,5,7]
