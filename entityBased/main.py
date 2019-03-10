# some other imports

import os

from services import StorageService, ArtifactService


def main(key):
    s3_service = StorageService.get_storage("s3") # or "db"
    audio_service = ArtifactService.get_artifact("audio")
    # Use methods on those objects as per program logic
    s3_service.read()
    audio_service.encode()
  

if __name__ == '__main__':
    main(os.environ.get("key"))
