from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="utility-gdrive",
    version="0.1.0",
    description="A Python CLI for downloading Google Drive files.",
    author="DanielPDWalker",
    url="https://www.matatika.com/",
    entry_points="""
        [console_scripts]
        gdrive=utility_gdrive.cli.commands.root:root
    """,
    license="AGPL-3.0",
    install_requires=required,
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
