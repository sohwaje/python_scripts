"""
$ python3.7 mysql_repl_mon.py
IP: 10.1.0.29, seconds: 1, slave_io_running: normal, slave_sql_running: normal
IP: 10.1.0.39, seconds: 1, slave_io_running: normal, slave_sql_running: normal
IP: 10.1.0.40, seconds: 0, slave_io_running: normal, slave_sql_running: normal
IP: 10.1.0.41, seconds: 1, slave_io_running: normal, slave_sql_running: normal
IP: 10.1.0.42, seconds: 0, slave_io_running: normal, slave_sql_running: normal
IP: 10.1.0.43, seconds: 1, slave_io_running: normal, slave_sql_running: normal
IP: 10.1.0.44, seconds: 0, slave_io_running: normal, slave_sql_running: normal
"""
import MySQLdb as mdb

SERVER = ['10.1.0.29', '10.1.0.39','10.1.0.40','10.1.0.41','10.1.0.42','10.1.0.43','10.1.0.44']

def main():
    for server in SERVER:
        host = server
        user = 'root'
        password = '!#SI0aleldj*)'
        con = mdb.connect(host, user, password)
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute('show slave status')
        slave_status = cur.fetchone()  # slave status 딕셔너리 형태로 담김
        second = slave_status["Seconds_Behind_Master"]

        if slave_status["Slave_SQL_Running"] == "Yes":
            slave_sql_running = "normal"
        else:
            slave_sql_running = "abnormal"
        if slave_status["Slave_IO_Running"] == "Yes":
            slave_io_running = "normal"
        else:
            slave_io_running = "abnormal"
        print("IP: %s, seconds: %s, slave_io_running: %s, slave_sql_running: %s" % (host, second, slave_io_running, slave_sql_running))

if __name__ == '__main__':
    main()
