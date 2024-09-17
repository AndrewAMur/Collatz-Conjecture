# Collatz Conjecture

## Overview

The Collatz Conjecture is a mathematical sequence that starts with any positive integer \( n \). The sequence is defined as follows:
- If \( n \) is even, divide it by 2.
- If \( n \) is odd, multiply it by 3 and add 1.
- Repeat the process with the new value of \( n \) until \( n \) becomes 1.

Despite its simple rules, the Collatz Conjecture remains unsolved in mathematics, with no proof yet that every positive integer eventually reaches 1.

This project consists of two Python scripts:
1. `generate_sequence.py` - Computes and prints the Collatz sequence for a given starting number.
2. `generate_visualization.py` - Generates a plot of the lengths of Collatz sequences for integers from 1 to 1000.

## Getting Started

To get started with this project, follow these instructions to set up your environment and run the scripts on your local machine.

### Prerequisites

Ensure you have Python 3.x installed on your system. You will also need the Python packages listed in `requirements.txt`.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AndrewAMur/Collatz-Conjecture.git
   cd Collatz-Conjecture
   ```

2. **Create a Virtual Environment (Optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Scripts

1. **Generate Collatz Sequence**

   To compute and display the Collatz sequence for a specific starting number, run:

   ```bash
   python generate_sequence.py
   ```

   Follow the prompt to enter a positive integer. The script will output the Collatz sequence for the provided number.

2. **Generate Visualization**

   To generate and view a plot of Collatz sequence lengths for integers from 1 to 1000, run:

   ```bash
   python generate_visualization.py
   ```

   This script will produce a plot showing how the length of the Collatz sequence varies with the starting number.

### Example Output

- **Collatz Sequence Output:**

  ```
  Enter a positive integer to start the Collatz sequence: 6
  The Collatz sequence is:
  [6, 3, 10, 5, 16, 8, 4, 2, 1]
  ```

- **Visualization:**

  A plot will be displayed showing the sequence lengths for numbers from 1 to 1000.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements. Please ensure any changes are well-tested and documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Collatz Conjecture on Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)

For any questions or support, please open an issue on [GitHub](https://github.com/AndrewAMur/Collatz-Conjecture).
