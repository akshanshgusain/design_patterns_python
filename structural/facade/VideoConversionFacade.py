"""
Facade is a structural design pattern that provides a simplified (but limited) interface to a complex system of classes,
 library or framework.
"""
from structural.facade.complexLibrary.AudioMixer import AudioMixer
from structural.facade.complexLibrary.BitrateReader import BitrateReader
from structural.facade.complexLibrary.CodecFactory import CodecFactory
from structural.facade.complexLibrary.MPEG4CompressionCodec import MPEG4CompressionCodec
from structural.facade.complexLibrary.OggCompressionCodec import OggCompressionCodec
from structural.facade.complexLibrary.VideoFile import VideoFile
from structural.facade.complexLibrary.iCodec import Codec


class VideoConversionFacade:

    def __init__(self):
        pass

    @staticmethod
    def convert_video(file_name: str, format: str) -> str:
        print("VideoConversionFacade: conversion started.")
        file: VideoFile = VideoFile(file_name)
        source_codec: Codec = CodecFactory.extract(file)
        destination_codec: Codec

        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer: VideoFile = BitrateReader.read(file, source_codec)
        intermediate_result: VideoFile = BitrateReader.converts(buffer, destination_codec)
        result: str = AudioMixer.fix(intermediate_result)
        print("VideoConversionFacade: conversion completed, returning the file path")
        return result