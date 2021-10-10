from datetime import datetime
import os
from pathlib import Path, PosixPath
from zipfile import ZipFile

TMP = Path(os.getenv("TMP", "/tmp"))
LOG_DIR = TMP / "logs"
ZIP_FILE = "logs.zip"


def _file_stamp(file):
    ts = file.stat().st_ctime
    dt = datetime.fromtimestamp(ts)
    date_str = dt.strftime("%Y-%m-%d")
    return f"{file.name.split('.')[0]}_{date_str}.log", ts


def zip_last_n_files(
    directory: PosixPath = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3
):
    files = sorted(
        [(file, _file_stamp(file)) for file in directory.iterdir()],
        key=lambda x: x[1][1],
        reverse=True,
    )
    with ZipFile(zip_file, "w") as zf:
        for file, stamp in files[:n]:
            file_name, _ = stamp
            zf.writestr(file_name, file.read_text())
