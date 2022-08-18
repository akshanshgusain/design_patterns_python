from structural.facade.complexLibrary.iCodec import Codec


class MPEG4CompressionCodec(Codec):
    def __init__(self):
        self.type: str = "mp4"
