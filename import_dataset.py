import os
import pandas as pd
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_extract_kaggle_dataset(dataset_name, desired_file,
                                        target_dir, summary=False):
    """
    Download and extract a Kaggle dataset.
    
    Parameters:
    - dataset_name: str, the name of the Kaggle dataset
    - target_dir: str, the directory to save the downloaded files
    """
    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Authenticate and download the dataset from Kaggle
    api = KaggleApi()
    api.authenticate()
    
    # Download dataset
    api.dataset_download_files(dataset_name, path=target_dir, unzip=False)
    
    # Path to the downloaded zip file
    zip_path = os.path.join(target_dir, f"{dataset_name.split('/')[-1]}.zip")
    
    # Unzip the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extract(desired_file, path=target_dir)

    # Load datasets
    file_path = os.path.join(target_dir, desired_file)
    df = pd.read_csv(file_path)

    if summary is True:
        # Print dataset shapes
        print("Movies dataset shape:", df.shape)

        # Preview data
        print("\nMovies preview:")
        print(df.head())

        # Info about datasets
        print("\nMovies dataset info:")
        df.info()

        # Print describe dataset
        print("\nMovies dataset describe:")
        print(df.describe())

    return df
