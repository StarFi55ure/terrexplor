from flask import Flask
from flask_restful import Resource, Api

from TXTileServer.api.tasks import raster_process_hillshade

app = Flask(__name__)
api = Api(app)


@api.resource('/process')
class StartProcessing(Resource):
    """
    Just to kick off processing
    """

    def get(self):
        res = raster_process_hillshade.delay()

        return {
            'status': 'done',
            'message': 'start processing'
        }


def build_wsgi_application():
    '''
    Return the app wsgi object

    :return:
    '''

    return app
