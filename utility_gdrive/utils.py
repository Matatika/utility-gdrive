import io

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


def download_file(real_file_id, creds):
    """Downloads a file
    Args:
        real_file_id: ID of the file to download
    Returns : IO object with location.

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    returned_files = {}

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_id = real_file_id

        folders = service.files().list(q="mimeType='application/vnd.google-apps.folder'").execute()

        for folder in folders["files"]:
            if folder["id"] == file_id:
                files_in_folder = service.files().list(q=f"'{file_id}' in parents").execute()
                for file in files_in_folder["files"]:
                    file, file_name = download_file_data(service, file["id"])
                    returned_files[file_name] = file

        if returned_files == {}:
            file, file_name = download_file_data(service, file_id)
            returned_files[file_name] = file

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return returned_files



def download_file_data(service, file_id):
    file_name = service.files().get(fileId=file_id).execute()

    request = service.files().get_media(fileId=file_id)

    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(F'Downloading {file_name} {int(status.progress() * 100)}.')

    return file.getvalue(), file_name["name"]