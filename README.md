# Currency Exchange Rate Script

This script retrieves currency exchange rates from the PrivatBank API and displays the sale and purchase rates for EUR and USD currencies.

# Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/currency-exchange-script.git
   ```

2. Navigate to the project directory:

   ```
   cd currency-exchange-script
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

# Usage

1.  Run the script by providing the number of days to retrieve exchange rates for as a command-line argument:

    ```
    python exchange_rate_script.py <num_days>
    ```

    Replace <num_days> with an integer value representing the number of recent days to retrieve exchange rates for. Note that the maximum number of days is 10.

    # Example

        python exchange_rate_script.py 5

2.  The script will fetch the exchange rates for the specified number of recent days and display the sale and purchase rates for EUR and USD currencies.
