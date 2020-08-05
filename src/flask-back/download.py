from flask_restful import Resource, reqparse
from flask_restful import fields, marshal

import youtube_dl
import os

from youtube_dl.utils import YoutubeDLError

import config
parser = reqparse.RequestParser()
parser.add_argument('url', type=str, required=True, help='URL to the video')
parser.add_argument('format_id', type=str, required=True, help='Format id')


class Download(Resource):
    def post(self):
        args = parser.parse_args()
        url = args["url"]
        format_id = args['format_id']
        ydl_opts = {
            'format': format_id,
            # 'progress_hooks': [self.rename_hook],
            'outtmpl': os.path.join(config.DOWNLOAD_FOLDER, '%(id)s.%(ext)s'),
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                result = ydl.download([url])
            return result
        except YoutubeDLError as e:
            return {
                "error": str(e)
            }


