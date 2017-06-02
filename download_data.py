import errno
import os

import requests


def create_data_subdirectory():
    try:
        os.makedirs('data')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def download_file(url):
    local_filename = os.path.join('data', url.split('/')[-1])
    response = requests.get(url)
    with open(local_filename, 'wb') as outfile:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                outfile.write(chunk)
    return None


def main():

    url_base = 'https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/download/'

    filenames = [
        'train_v2.csv.zip',
        'train-tif-v2.tar.7z',
        'train-jpg.tar.7z',
        'test-tif-v2.tar.7z',
        'test-jpg.tar.7z',
        'test-jpg-additional.tar.7z',
        'sample_submission_v2.csv.zip',
        'Kaggle-planet-train-tif.torrent',
        'Kaggle-planet-test-tif.torrent']

    create_data_subdirectory()

    for filename in filenames:
        print('Downloading {}'.format(filename))
        download_file(url_base + filename)
    

if __name__ == '__main__':

    main()
