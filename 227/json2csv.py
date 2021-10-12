import os
from pathlib import Path
import csv
import json

EXCEPTION = "exception caught"
TMP = Path(os.getenv("TMP", "/tmp"))


def convert_to_csv(json_file):
    """Read/load the json_file (local file downloaded to /tmp) and
    convert/write it to defined csv_file.
    The data is in mounts > collected

    Catch bad JSON (JSONDecodeError) file content, in that case print the defined
    EXCEPTION string ('exception caught') to stdout reraising the exception.
    This is to make sure you actually caught this exception.

    Example csv output:
    creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
    32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
    63502,ability_mount_hordescorpionamber,True,...
    ...
    """  # noqa E501
    try:
        csv_file = TMP / json_file.name.replace(".json", ".csv")
        with open(json_file, "r") as fp:
            data = json.load(fp)
        mounts = data["mounts"]["collected"]
        headers = mounts[0].keys()
        with open(csv_file, "w") as fp:
            w = csv.DictWriter(fp, fieldnames=headers)
            w.writeheader()
            for mount in mounts:
                w.writerow(mount)
    except Exception as e:
        print(EXCEPTION)
        raise e
