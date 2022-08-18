from typing import TextIO

from structural.facade.complexLibrary.VideoFile import VideoFile


class AudioMixer:
    @staticmethod
    def fix(result: VideoFile) -> str:
        print("AudioMixer: fixing audio...")
        path = 'audio_mixer.txt'
        with open(path, 'w') as fp:
            pass
            # To write data to new file uncomment
            # this fp.write("New file created")
        return path
