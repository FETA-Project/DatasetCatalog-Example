import requests
from zipfile import ZipFile
import tarfile
import shutil
import os
import gzip

def sample_csv_rows(input_csv_path: str):
    """
    Loads a CSV file, takes the first 2000 and last 2000 rows,
    and saves them to 'miner22-sampled.csv'.

    If the file has fewer than 4000 rows, all rows will be included.

    Args:
        input_csv_path (str): The path to the input CSV file.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(input_csv_path)

        # Get the total number of rows
        total_rows = len(df)

        if total_rows <= 4000:
            sampled_df = df
        else:
            first_2000_rows = df.head(2000)
            last_2000_rows = df.tail(2000)
            sampled_df = pd.concat([first_2000_rows, last_2000_rows])

        # Save the sampled data to a new CSV file
        output_csv_path = 'miner22-sampled.csv'
        sampled_df.to_csv(output_csv_path, index=False)

        print(f"Successfully sampled {len(sampled_df)} rows and saved to '{output_csv_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_csv_path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{input_csv_path}' is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def clean_directory(base_dir):
    shutil.rmtree(base_dir)
    shutil.rmtree("decrypto_dataset_design.csv")

def get_dataset_csv(base_dir):
    """
    Get sample dataset csv for analysis
    """
    uncompressed_file = os.path.join(base_dir,"DeCryptoDatasets","decrypto_dataset_design.csv")
    shutil.copy(uncompressed_file,".")
    #uncompressed_file = os.path.join(base_dir,"DeCryptoDatasets","decrypto_dataset_evaluation.csv")
    #shutil.copy(uncompressed_file,".")
    #print(f"Uncompressed file saved to: ",os.path.abspath("."))

def download_and_extract_tar_gz(url, extract_to='.'):
    """
    Downloads a .tar.gz file from a URL, saves it to disk, and
    extracts all its contents to the specified directory.

    Args:
        url: The URL of the .tar.gz file.
        extract_to: The directory to extract the files to (defaults to current directory).
    """
    try:
        tar_gz_filename = "downloaded.tar.gz"

        # Download with streaming to handle large files
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(tar_gz_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Extract the contents
        with tarfile.open(tar_gz_filename, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_to)
        print(f"Files extracted to: {extract_to}")

        # Remove the tar.gz file after extraction
        os.remove(tar_gz_filename)
        print(f"Tar.gz file removed: {tar_gz_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
    except Exception as e:
        print(f"Error processing the file: {e}")

def download_and_unzip(url, extract_to='.'):
  """
  Downloads a large zip file from a URL, saves it to disk, and 
  extracts all its contents to the specified directory.

  Args:
    url: The URL of the zip file.
    extract_to: The directory to extract the files to (defaults to current directory).
  """
  try:
    zip_filename = "downloaded.zip"  # Choose a filename

    # Download with streaming to handle large files
    with requests.get(url, stream=True) as response:
      response.raise_for_status()
      with open(zip_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192): 
          f.write(chunk)

    # Extract the contents
    with ZipFile(zip_filename, 'r') as zip_ref:
      zip_ref.extractall(extract_to)
    print(f"Files extracted to: {extract_to}")

    # Remove the zip file after extraction
    os.remove(zip_filename)
    print(f"Zip file removed: {zip_filename}")

  except requests.exceptions.RequestException as e:
    print(f"Error downloading the file: {e}")
  except Exception as e:
    print(f"Error processing the file: {e}")

# Run action
zenodo_url = "https://zenodo.org/records/7189293/files/DeCryptoDatasets.tar.gz?download=1"
base_directory = 'extracted_data'
download_and_extract_tar_gz(zenodo_url, base_directory)
get_dataset_csv(base_directory)
sample_csv_rows(decrypto_dataset_design.csv)
clean_directory(base_directory)
