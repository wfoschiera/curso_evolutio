from youtube_dl import YoutubeDL
import sys
import time


def convert_duration(segundos):
    return time.strftime('%H:%M:%S', time.gmtime(segundos))


def get_youtube_video_info(vid):
    video = "http://www.youtube.com/watch?v=%s" %vid
    youtube_dl_opts = {}
    with YoutubeDL(youtube_dl_opts) as ydl:
        info_dict = ydl.extract_info(video, download=True)
        # video_url = info_dict.get("url", None)
        return {
            'title': info_dict.get('title', None),
            'duration':  convert_duration(info_dict.get("duration"))
        }

if __name__ == '__main__':
    print("Aguarde... em breve as informações serão apresentada na tela")
    video_id = (sys.argv[1])
    info = get_youtube_video_info(video_id)
    print(f"Titulo: {info['title'].capitalize()}")
    print(f"Duração: {info['duration']}")
