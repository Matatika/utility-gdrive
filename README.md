<a href="https://github.com/Matatika/utility-gdrive/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Matatika/utility-gdrive"></a>

## gdrive
Current Status: In development

Python package for downloading Google Drive files.

With gdrive you can download a file or a folder of files (currently only the top level files, no sub-folders) with google authentication. Currently google own file types are not supported, support for this is on the roadmap.


### Settings

Valid settings to run the gdrive package:
- A valid `access_token` with the correct scope : `https://www.googleapis.com/auth/drive.readonly` granted. NOTE: Once the `access_token` expires you will be required to get another yourself.

- A valid `refresh_token` with the correct scope: `https://www.googleapis.com/auth/drive.readonly` granted, `client_id` and `client_secret`. With these settings provided the package will refresh your `access_token` for you whenever it expires.


| **Setting** | **Required** | **Providing Settings Inline or Environment Variable** |
| ----------- | ------------ | --------------------- |
`access_token` | true | Inline: `-access_token=` or Environment Variable: `GDRIVE_ACCESS_TOKEN`
`path` | true | When calling the package: `gdrive path/to/file_or_folder` or Environment Variable: `GDRIVE_FILE_ID`
`client_id` | false | Inline: `-client_id=` or Environment Variable: `GDRIVE_CLIENT_ID`
`client_secret` | false | Inline: `-client_secret=` or Environment Variable: `GDRIVE_CLIENT_SECRET`
`refresh_token` | false | Inline: `-refresh_token=` or Environment Variable: `GDRIVE_REFRESH_TOKEN`
`output_path` | false | Inline: `-output_path=` or Environment Variable: `GDRIVE_OUTPUT_PATH`


### Command Examples

Example CLI usage (If you set the environment variables these will get picked up automatically on run so no need to pass them): `gdrive path/to/file -output_path=path/to/dir -client_id=12345 -client_secret= 12345 -refresh_token=12345 -access_token=12345`


### Roadmap
- Add support for google native files.
    - Need to `get_export` and do better mimeType filtering.
- Add support for downloading files from a folder and all its sub folders.
- Add support for `nextPageToken` (current limit of 100 files)
