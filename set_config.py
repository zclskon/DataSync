import json


def set_config():
    server_list = ['nanhua', 'zhongxin', 'luzheng']
    fw = open('config.ini', 'w+')
    fw.write('%s=%s\n' % ('server_list', json.dumps(server_list)))
    fw.close()


if __name__ == '__main__':
    set_config()
