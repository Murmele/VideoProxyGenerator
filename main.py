from pathlib import Path
import os
import ffmpeg

"""
Resizes a video to 720p, using as proxy
"""


def convert720p(original_name, proxy_name):
    width = 1280
    height = 720
    input_video = ffmpeg.input(original_name)
    #important that they get separated and then concatenated at the end, otherwise no sound can be heared
    a1 = input_video.audio
    v1 = input_video.video.filter('scale', width, height)

    output_video = ffmpeg.output(v1, a1, proxy_name, video_bitrate=2e6, audio_bitrate=100e3)

    try:
        (out, err) = ffmpeg.run(output_video)
    except ffmpeg.Error:
        print("An error occured during resizing. Skip video")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    proxy_suffix = "_proxy720p.MP4"
    searchFolder = "../FOTOS/2020/GoPro" # folder in which should be searched

    for path in Path(searchFolder).rglob('*.MP4'):
        print(f"Check Proxy for file: {path}")
        [root, extension] = os.path.splitext(path)

        proxy_video_name = root + proxy_suffix

        if not os.path.isfile(proxy_video_name) and proxy_suffix not in f"{path}":
            print("Create proxy file.")
            convert720p(path, proxy_video_name)
        else:
            print("Proxy file exists already")
