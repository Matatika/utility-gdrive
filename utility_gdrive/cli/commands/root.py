"""CLI entrypoint 'utility-gdrive' command"""

import click
import os

from pathlib import Path
from utility_gdrive.auth import proxy_refresh_handler
from utility_gdrive.utils import download_file
from google.oauth2.credentials import Credentials


@click.command()
@click.argument(
    "file_id",
    type=click.STRING,
    default=os.getenv("GDRIVE_FILE_ID")
)
@click.option(
    "-output_path",
    type=click.STRING,
    default=os.getenv("GDRIVE_OUTPUT_PATH"),
    help="Output path for files, default is utility-gdrive is being invoked. Environment variable: GDRIVE_OUTPUT_PATH"
)
@click.option(
    "-client_id",
    type=click.STRING,
    default=os.getenv("GDRIVE_CLIENT_ID"),
    help="Google client id. Environment variable: GDRIVE_CLIENT_ID"
)
@click.option(
    "-client_secret",
    type=click.STRING,
    default=os.getenv("GDRIVE_CLIENT_SECRET"),
    help="Google client secret. Environment variable: GDRIVE_CLIENT_SECRET"
)
@click.option(
    "-access_token",
    type=click.STRING,
    default=os.getenv("GDRIVE_ACCESS_TOKEN"),
    help="Google access token. Environment variable: GDRIVE_ACCESS_TOKEN"
)
@click.option(
    "-refresh_token",
    type=click.STRING,
    default=os.getenv("GDRIVE_REFRESH_TOKEN"),
    help="Google refresh token. Environment variable: GDRIVE_REFRESH_TOKEN"
)
def root(file_id, output_path, client_id, client_secret, access_token, refresh_token):
    """This command takes a G-Drive file or folder id.
    
    Environment variable: GDRIVE_FILE_ID"""

    if not client_id or not client_secret or not access_token or not refresh_token:
        if not client_id:
            click.secho("Missing google client id.", fg="yellow")
        if not client_secret:
            click.secho("Missing google client secret.", fg="yellow")
        if not access_token:
            click.secho("Missing google access token.", fg="red")
        if not refresh_token:
            click.secho("Missing google refresh token.", fg="red")


    if os.getenv("GDRIVE_OAUTH_CREDENTIALS_REFRESH_PROXY_URL") and \
        os.getenv("GDRIVE_OAUTH_CREDENTIALS_REFRESH_PROXY_URL_AUTH") and \
        os.getenv("GDRIVE_OAUTH_CREDENTIALS_REFRESH_TOKEN") and \
        os.getenv("GDRIVE_OAUTH_CREDENTIALS_ACCESS_TOKEN"):
        creds = Credentials(
            access_token,
            refresh_handler=proxy_refresh_handler
        )
    else:
        creds = Credentials(
            access_token or '',
            refresh_token=refresh_token,
            token_uri='https://oauth2.googleapis.com/token',
            client_id=client_id,
            client_secret=client_secret
        )

    files = download_file(file_id, creds)
    file_name = None
    
    for k, v in files.items():
        if output_path:
            if output_path[-1] != "/":
                output_path = output_path + "/"
            file_name = Path(output_path + k)
        with open(file_name or k, "wb") as f:
            f.write(v)
