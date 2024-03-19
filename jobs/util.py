import zipfile as zip


def extract_csv(file_path, extract_path):
    with zip.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
