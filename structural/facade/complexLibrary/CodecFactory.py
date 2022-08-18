from structural.facade.complexLibrary.MPEG4CompressionCodec import MPEG4CompressionCodec
from structural.facade.complexLibrary.OggCompressionCodec import OggCompressionCodec
from structural.facade.complexLibrary.VideoFile import VideoFile
from structural.facade.complexLibrary.iCodec import Codec


class CodecFactory:

    @staticmethod
    def extract(file: VideoFile) -> Codec:
        codec_type: str = file.codec_type

        if codec_type == "mp4":
            print(f"CodecFactory: extracting mpeg audio...")
            return MPEG4CompressionCodec()
        else:
            print(f"CodecFactory: extracting ogg audio...")
            return OggCompressionCodec()