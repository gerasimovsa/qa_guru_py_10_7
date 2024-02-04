import os.path
import shutil
from zipfile import ZipFile
import pytest
from utils.paths import *


@pytest.fixture(autouse=True)
def archive_files():
    if not os.path.exists(RESOURCES):
        os.mkdir(RESOURCES)

    with ZipFile(os.path.join(RESOURCES, "sample_zip.zip"), "w") as archiver:
        for filename in DATA_FILES:
            archiver.write(os.path.join(DATA, filename), arcname=filename)

    yield

    shutil.rmtree(RESOURCES)
