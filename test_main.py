import pytest
import main
import polars as pl

# Define test cases for calculate_statistics function
def test_calculate_statistics():
    # Create a sample CSV file for testing
    sample_data = pl.DataFrame({
        'danceability': [0.1, 0.1, 0.1],
        'energy': [0.8, 0.7, 0.9],
        'artist_popularity': [80, 70, 90],
        'loudness': [-5, -6, -4]
    })
    sample_data.write_csv('test_data.csv')


    # Test the calculate_statistics function
    result = main.calculate_statistics('test_data.csv')

    # Verify the expected output
    # assert result['mean']['danceability'] == 0.1
    # assert result['median']['danceability'] == 0.1

# Define test cases for visualize_data function
def test_visualize_data():
    # Create a sample CSV file for testing
    sample_data = pl.DataFrame({
        'danceability': [0.7, 0.6, 0.8],
        'energy': [0.8, 0.7, 0.9],
        'artist_popularity': [80, 70, 90],
        'loudness': [-5, -6, -4]
    })
    sample_data.write_csv('test_data.csv')


    # Test the visualize_data function
    result = main.visualize_data('test_data.csv')

    # You can add assertions here to check the expected behavior

# Define test cases for calculate_correlation function
def test_calculate_correlation():
    # Create a sample CSV file for testing
    sample_data = pl.DataFrame({
        'danceability': [0.7, 0.6, 0.8],
        'energy': [0.8, 0.7, 0.9],
        'artist_popularity': [80, 70, 90],
        'loudness': [-5, -6, -4]
    })
    sample_data.write_csv('test_data.csv')


    # Test the calculate_correlation function
    result = main.calculate_correlation('test_data.csv')

    # You can add assertions here to check the expected behavior

# Clean up the test file by removing the sample data file
def teardown():
    import os
    if os.path.exists('test_data.csv'):
        os.remove('test_data.csv')

# Run the tests
if __name__ == "__main__":
    pytest.main()
