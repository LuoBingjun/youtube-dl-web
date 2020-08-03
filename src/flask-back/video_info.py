from flask_restful import Resource, reqparse
from flask_restful import fields, marshal

import youtube_dl

parser = reqparse.RequestParser()
parser.add_argument('url', type=str, required=True, help='URL to the video')

resource_fields = {'title': fields.String, 'description': fields.String, 'uploader': fields.String, 'thumbnail': fields.String, 'duration': fields.Float}

class VideoInfo(Resource):
    def get(self):
        args = parser.parse_args()
        video_url = args["url"]
        with youtube_dl.YoutubeDL() as ydl:
            result = ydl.extract_info(video_url, download=False)
            return marshal(result, resource_fields)