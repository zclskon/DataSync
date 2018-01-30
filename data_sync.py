# encoding:utf-8
import tools
import pandas as pd
import multiprocessing
from sqlalchemy import create_engine

config = tools.load_ini('config.ini')
db_dict = tools.load_ini('db.ini')


def sync_table(server, name):
    db_server = tools.Db(**db_dict.get(server))
    df = pd.read_sql('select * from %s' % name, db_server.conn)
    db_server.close()
    db_188 = tools.Db(**db_dict.get('db_188'))
    db_188.execute('delete from %s.%s' % (server, name.split('.')[1]))
    engine = create_engine(
        'mysql+pymysql://%s:%s@%s:%s/%s' % (db_188.user, db_188.passwd, db_188.host, db_188.port, server))
    df.to_sql(name.split('.')[1], engine, if_exists='append', index=False)
    db_188.close()


def data_sync(server):
    sync_table(server, 'om.order_history')
    sync_table(server, 'portfolio.pf_account')
    sync_table(server, 'portfolio.pf_position')
    sync_table(server, 'strategy.strategy_parameter')
    sync_table(server, 'strategy.strategy_state')
    sync_table(server, 'om.trade2_history')


def mul_data_sync():
    proc_list = [multiprocessing.Process(target=data_sync, args=(server,)) for server in
                 config.get('server_list') + ['guoxin']]
    for proc in proc_list:
        proc.start()
    for proc in proc_list:
        proc.join()


if __name__ == '__main__':
    mul_data_sync()
