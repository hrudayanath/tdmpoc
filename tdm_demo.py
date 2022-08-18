import sys
import pandas as pd
from pandas.io import sql
import pymysql
from sqlalchemy import create_engine


if len(sys.argv) < 2:
    print("Required arguments missing")
    sys.exit(1)

input_file = sys.argv[1]


engine = create_engine('mysql+pymysql://springuser:ThePassword@localhost/testDb')


df = pd.read_csv(input_file)


df.to_sql("customer",con=engine)