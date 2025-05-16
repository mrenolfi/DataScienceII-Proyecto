# This script downloads and extracts a dataset from Kaggle.
# It also provides a summary of the dataset if requested.
from import_dataset import download_and_extract_kaggle_dataset

dataset_name = "tmdb/tmdb-movie-metadata"
desired_file = "tmdb_5000_movies.csv"
target_dir = "data_raw"
df = download_and_extract_kaggle_dataset(dataset_name,
                                         desired_file,
                                         target_dir, summary=True)

