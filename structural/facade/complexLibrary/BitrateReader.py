from structural.facade.complexLibrary.VideoFile import VideoFile
from structural.facade.complexLibrary.iCodec import Codec


class BitrateReader:
    @staticmethod
    def read(file: VideoFile, codec: Codec) -> VideoFile:
        print("BitrateReader: reading file...")
        return file

    @staticmethod
    def converts(buffer: VideoFile, codec: Codec) -> VideoFile:
        print("BitrateReader: writing file...")
        return buffer
