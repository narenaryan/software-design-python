from enum import Enum # Standard library

class StorageType(Enum):
    S3 = "s3"
    DB = "db"


class ArtifactType(Enum):
    AUDIO = "audio"
    TEXT = "text"
