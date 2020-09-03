import pymysql
from prettytable import PrettyTable
from contextlib import closing
from pymysql.cursors import DictCursor
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO, filemode='w')
SQL_QUERIES = 'sql.txt'
HOST = 'localhost'
USER = 'root'
PASS = '12799721'
DB = 'union_reporting'


def create_table(table_from_bd):
    t_heads = []
    t_data = []
    for row in table_from_bd:
        for head, content in row.items():
            if head not in t_heads:
                t_heads.append(head)
            t_data.append(content)
    table = PrettyTable(t_heads)
    columns = len(t_heads)
    while t_data:
        table.add_row(t_data[:columns])
        t_data = t_data[columns:]
    return table


def read_sql_queries(queries_file):
    with open(queries_file, 'r') as queries:
        queries = queries.read().rstrip().split(';')
        return [query for query in queries if query]


with closing(pymysql.connect(
        host=HOST,
        user=USER,
        password=PASS,
        db=DB,
        charset='utf8mb4',
        cursorclass=DictCursor)) as conn:
    for query in read_sql_queries(SQL_QUERIES):
        with conn.cursor() as cursor:
            cursor.execute(query)
            logging.info(create_table(cursor))
