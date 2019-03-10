# some imports
import os

from get import read_from_s3
from delete import delete_from_s3
from put import encode_audio_file

def main(key):
    read_from_s3()
    # some logic
    delete_from_s3()
    # some logic
    encode_audio_file()

if __name__ == '__main__':
    main(os.environ.get("key"))
