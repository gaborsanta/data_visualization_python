import csv
from datetime import datetime
from matplotlib import pyplot as plt

#file = 'death_valley_2014.csv'
# Get dates, high, and low temperatures from file.

def weatherChart(files):
    # Put fig outside to plot both graphs on the same chart
    fig = plt.figure(dpi=128, figsize=(10, 6))
    for file in files:

        filename = '/Users/gabor/Desktop/workspace/python_work/python_crashcourse_book/data_visualization/resources/' + file
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            #for index, column_header in enumerate(header_row):
                #print(index, column_header)

            dates, highs, lows = [], [], []
            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    high = int(row[1])
                    low = int(row[3])
                except ValueError:
                    print(current_date, 'missing data')
                else:
                    dates.append(current_date)
                    #convert to int for matplotlib to read
                    highs.append(high)
                    lows.append(low)

            # Plot data
            #fig = plt.figure(dpi=128, figsize=(10, 6))
            plt.plot(dates, highs, c='red', alpha=0.5)
            plt.plot(dates, lows, c='blue', alpha=0.5)
            plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

            # Format plot.
            plt.title("Daily high and low temperatures - " + file, fontsize=24)
            plt.xlabel("", fontsize=10)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=12)

    plt.show()

files = ['death_valley_2014.csv', 'sitka_weather_2014.csv']
weatherChart(files)