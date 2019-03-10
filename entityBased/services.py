# some other imports

from abc import ABC, abstractmethod # Standard library
from enums import StorageType, ArtifactType


class Service(object):
    pass

class StorageService(Service, ABC):
    
    # Methods every child service should implement
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass
    
    @staticmethod
    def __get(type):
        return {
            StorageType.S3.value: S3Service,
            StorageType.DB.value: DBService
        }.get(type)
    
    # Factory for services
    @classmethod
    def get_storage(cls, type):
        storage_class = cls.__get(type) # Get storage type
        storage_instance = storage_class()
        if not issubclass(storage_class, cls):
            raise Exception(cls, " ", "interface is not satisfied")
        return storage_instance
  
class S3Service(StorageService):
    def read(self):
        print("reading the file from S3")
    
    def write(self):
        print("writing the file into S3")
    
class DBService(StorageService):
    def read(self):
        print("query the rows from DB")
    
    def write(self):
        print("inserting rows into DB")
    
    
class ArtifactService(Service, ABC):
    # Methods every child service should implement
    @abstractmethod
    def decode(self):
        pass
  
    @abstractmethod
    def encode(self):
        pass
  
    @staticmethod
    def __get(type):
        return {
            ArtifactType.AUDIO.value: AudioArtifactService,
            ArtifactType.TEXT.value: TextArtifactService
        }.get(type)

    # Factory for services
    @classmethod
    def get_artifact(cls, type):
        artifact_class = cls.__get(type) # Get storage type
        artifact_instance = artifact_class()
    
        if not issubclass(artifact_class, cls):
            raise Exception(cls, " ", "interface is not satisfied")
        return artifact_instance

class AudioArtifactService(ArtifactService):
  def decode(self):
    print("decoding the audio file")
  
  def encode(self):
    print("encoding the audio file")

class TextArtifactService(ArtifactService):
  def decode(self):
    print("decoding the text file")
  
  def encode(self):
    print("encoding the text file")
