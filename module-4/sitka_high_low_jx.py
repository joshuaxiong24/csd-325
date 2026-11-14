# sitka_high_low_jx.py
# Modified from sitka_highs.py
#
# CHANGE LOG
# 1. Added "import sys" so the program can exit cleanly.
# 2. Wrapped the CSV reading in a function (read_data) so it can be reused.
# 3. Read the lows (TMIN) as well as the highs (TMAX), using the header row
#    to find the column positions instead of hard-coding them.
# 4. Added a welcome message that explains how to use the menu.
# 5. Added a menu loop: Highs, Lows, or Exit.
# 6. Highs plot in red, lows plot in blue.
# 7. Added input validation for bad menu choices.
# 8. Added an exit message shown when the user quits.

import csv
import sys
from datetime import datetime

import matplotlib.pyplot as plt

FILENAME = 'sitka_weather_2018_simple.csv'


def read_data(filename):
    """Read dates, highs, and lows from the Sitka CSV file."""
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Find column positions from the header (safer than hard-coding)
        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')

        for row in reader:
            try:
                current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
                high = int(row[high_index])
                low = int(row[low_index])
            except (ValueError, IndexError):
                # Skip rows with missing or bad data
                continue
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows


def plot_temps(dates, temps, color, title):
    """Draw a line graph of the temperatures in the given color."""
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, temps, c=color)

    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def show_instructions():
    """Print the welcome message and menu instructions."""
    print('=' * 50)
    print('  Sitka, Alaska 2018 Temperature Viewer')
    print('=' * 50)
    print('How to use this program:')
    print("  Type 'highs' to see a graph of the daily high temperatures.")
    print("  Type 'lows'  to see a graph of the daily low temperatures.")
    print("  Type 'exit'  to quit the program.")
    print()


def main():
    dates, highs, lows = read_data(FILENAME)
    show_instructions()

    while True:
        choice = input(
            "Enter your choice (highs, lows, exit): ").strip().lower()

        if choice == 'highs':
            plot_temps(dates, highs, 'red', 'Daily High Temperatures - 2018')
        elif choice == 'lows':
            plot_temps(dates, lows, 'blue', 'Daily Low Temperatures - 2018')
        elif choice == 'exit':
            print('Thanks for using the Sitka Temperature Viewer. Goodbye!')
            sys.exit()
        else:
            print("Sorry, that wasn't a valid choice. Please type highs, lows, or exit.")
        print()


if __name__ == '__main__':
    main()
