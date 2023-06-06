import json
import logging
from base64 import b64decode
import requests
import mitmproxy.http
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from google.protobuf.json_format import MessageToDict
import liqi
from proto import liqi_pb2 as pb

# 导入配置
SETTINGS = json.load(open('settings.json', 'r'))
SEND_METHOD = SETTINGS['SEND_METHOD']  # 需要发送给小助手的method
SEND_ACTION = SETTINGS['SEND_ACTION']  # '.lq.ActionPrototype'中，需要发送给小助手的action
API_URL = SETTINGS['API_URL']  # 小助手的地址
logging.info(
    f'''已载入配置：\n
    SEND_METHOD: {SEND_METHOD}\n
    SEND_ACTION: {SEND_ACTION}\n
    API_URL: {API_URL}''')

liqi_proto = liqi.LiqiProto()
# 禁用urllib3安全警告
disable_warnings(InsecureRequestWarning)


class WebSocketAddon:
    def websocket_message(self, flow: mitmproxy.http.HTTPFlow):
        # 在捕获到WebSocket消息时触发
        assert flow.websocket is not None  # make type checker happy
        message = flow.websocket.messages[-1]
        # 解析proto消息
        result = liqi_proto.parse(message)
        if message.from_client is False:
            logging.info(f'接收到：{result}')
        if result['method'] in SEND_METHOD and message.from_client is False:
            if result['method'] == '.lq.ActionPrototype':
                if result['data']['name'] in SEND_ACTION:
                    data = result['data']['data']
                    if result['data']['name'] == 'ActionNewRound':
                        # 雀魂弃用了md5改用sha256，但没有该字段会导致小助手无法解析牌局，也不能留空
                        # 所以干脆发一个假的，反正也用不到
                        data['md5'] = data['sha256'][:32]
                else:
                    return
            elif result['method'] == '.lq.FastTest.syncGame':  # 重新进入对局时
                actions = []
                for item in result['data']['game_restore']['actions']:
                    if item['data'] == '':
                        actions.append({'name': item['name'], 'data': {}})
                    else:
                        b64 = b64decode(item['data'])
                        action_proto_obj = getattr(
                            pb, item['name']).FromString(b64)
                        action_dict_obj = MessageToDict(
                            action_proto_obj, preserving_proto_field_name=True, including_default_value_fields=True)
                        if item['name'] == 'ActionNewRound':
                            # 这里也是假md5，理由同上
                            action_dict_obj['md5'] = action_dict_obj['sha256'][:32]
                        actions.append(
                            {'name': item['name'], 'data': action_dict_obj})
                data = {'sync_game_actions': actions}
            else:
                data = result['data']
            logging.warn(f'已发送：{data}')
            requests.post(API_URL, json=data, verify=False)
            if 'liqi' in data.keys():  # 补发立直消息
                logging.warn(f'已发送：{data["liqi"]}')
                requests.post(API_URL,
                              json=data['liqi'], verify=False)


addons = [
    WebSocketAddon()
]
