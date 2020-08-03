from flask import Flask
from flask_restful import Api

from video_info import VideoInfo

URL_PATH = '/ytb'

app = Flask(__name__)
api = Api(app)

api.add_resource(VideoInfo, URL_PATH + '/api/video_info')

if __name__ == '__main__':
    app.run(debug=True)