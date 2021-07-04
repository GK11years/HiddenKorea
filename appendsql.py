import MySQLdb
import pymysql
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()


engine = create_engine(
    "mysql+mysqldb://{uresname}:{passwd}@{localhost}:{port}/{dbname}", encoding='utf-8')
conn = engine.connect()
df.to_sql(name='{new_table_name}', con=engine, if_exists='append', index=False)
conn.close()
