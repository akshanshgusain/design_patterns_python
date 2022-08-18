class VideoFile:
    def __init__(self, name: str):
        self.name = name
        self.codec_type = name.split(".")[1]

    def get_codec_type(self) -> str:
        return self.codec_type

    def get_name(self) -> str:
        return self.name
