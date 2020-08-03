from flask import Flask
from flask_restful import Api

from video_info import VideoInfo

app = Flask(__name__)
api = Api(app)

api.add_resource(VideoInfo, '/api/video_info')

if __name__ == '__main__':
    app.run(debug=True)