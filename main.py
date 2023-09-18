import polars as pl
import matplotlib.pyplot as plt
import os
from polars.errors import EmptyDataFrame, PolarsError

# Function to calculate statistics for specific columns
def calculate_statistics(file_path):
    try:
        # Reading the dataset from the CSV file
        data = pl.read_csv(file_path)

        # Selecting specific columns of interest
        selected_columns = ['danceability', 'energy', 'artist_popularity', 'loudness']
        data = data.select(selected_columns)

        if data.is_empty():
            raise EmptyDataFrame("The DataFrame is empty")

        # Calculating mean, median
        mean = data.mean()
        median = data.median()

        mean = mean.round(1)
        median = median.round(1)

        return {'mean': mean, 'median': median}
    except EmptyDataFrame as e:
        return str(e)
    except PolarsError as e:
        return str(e)

# Function to visualize specific columns as histograms
def visualize_data(file_path, save_path=None):
    try:
        # Reading the dataset from the CSV file
        data = pl.read_csv(file_path)

        # Selecting specific columns of interest
        selected_columns = ['danceability', 'energy', 'artist_popularity', 'loudness']
        data = data.select(selected_columns)

        if data.is_empty():
            raise EmptyDataFrame("The DataFrame is empty")

        # Create a directory to store the plots if save_path is provided
        if save_path:
            os.makedirs(save_path, exist_ok=True)

        # Iterate over each numeric column and create a histogram
        histogram_paths = []
        for col in data.columns:
            plt.figure(figsize=(8, 6))
            plt.hist(data[col].to_list(), bins=20, edgecolor='k', alpha=0.7)
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title(f"Histogram of {col}")
            plt.grid(True)

            if save_path:
                histogram_path = os.path.join(save_path, f"{col}_histogram.png")
                plt.savefig(histogram_path)
                plt.close()
                histogram_paths.append(histogram_path)
            else:
                plt.show()

        if save_path:
            return histogram_paths
    except EmptyDataFrame as e:
        return str(e)
    except PolarsError as e:
        return str(e)

# Function to calculate the correlation of artist_popularity with other columns
def calculate_correlation(file_path):
    try:
        # Reading the dataset from the CSV file
        data = pl.read_csv(file_path)

        # Selecting specific columns of interest
        selected_columns = ['danceability', 'energy', 'artist_popularity', 'loudness']
        data = data.select(selected_columns)

        if data.is_empty():
            raise EmptyDataFrame("The DataFrame is empty")

        # Calculating the correlation matrix
        correlation_matrix = data.corr()

        # Extracting the correlation of 'artist_popularity' with other columns
        artist_popularity_correlation = correlation_matrix['artist_popularity']

        return artist_popularity_correlation
    except EmptyDataFrame as e:
        return str(e)
    except PolarsError as e:
        return str(e)