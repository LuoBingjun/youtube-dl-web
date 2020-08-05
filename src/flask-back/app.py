from flask import Flask
from flask_restful import Api

from video_info import VideoInfo
from download import Download
import config


app = Flask(__name__,)

app.config['JSON_AS_ASCII'] = False

api = Api(app)
api.add_resource(VideoInfo, config.URL_PATH + '/api/video_info')
api.add_resource(Download, config.URL_PATH + '/api/download')

if __name__ == '__main__':
    app.run(debug=True)