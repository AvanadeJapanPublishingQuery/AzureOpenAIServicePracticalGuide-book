import os
import yaml
from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

# レスポンスのスキーマをインポート
from schemas import (
    GetEventResponse
)

#マニフェストファイルを読み込み、その内容をJSON形式で返す関数
@app.route("/.well-known/ai-plugin.json")
def plugin_manifest():
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return Response(text, content_type="application/json")

# OpenAPIのYAMLファイルを読み込み、その内容をJSON形式で返す関数
@app.route('/openapi.yaml')
def serve_openapi_yaml():
    with open(os.path.join(os.path.dirname(__file__), 'openapi.yaml'), 'r') as f:
        yaml_data = f.read()
        yaml_data = yaml.load(yaml_data, Loader=yaml.FullLoader)
        return jsonify(yaml_data)

#イベントのリストを取得するクラス
class Events(Resource):
    def get(self):
        events = ['Pool Event', 'Park Event', 'Car Event', 'Food Event']
        # GetEventResponseを使ってイベントのリストを整形し、その結果を返す
        return GetEventResponse(events=events).dict()

# '/events'のエンドポイントにEventsリソースを追加 
api.add_resource(Events, '/events')

if __name__ == '__main__': 
    app.run(debug=True, port=8080)