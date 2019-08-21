import psycopg2
import os
import sys
import warnings
from psycopg2 import extras
warnings.filterwarnings("ignore")

params = {'host': 'server',
          'database': 'database_name',
          'user': 'user_name',
          'password': 'password'}


if __name__ == '__main__':
    try:
        conn = psycopg2.connect(**params)

    finally:
        if conn is not None:
            conn.close()
