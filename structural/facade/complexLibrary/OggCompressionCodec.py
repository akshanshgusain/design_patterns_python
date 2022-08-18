from structural.facade.complexLibrary.iCodec import Codec


class OggCompressionCodec(Codec):
    def __init__(self):
        self.type: str = "ogg"
