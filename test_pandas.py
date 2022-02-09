### CSV 파일 저장
'''conn=pymysql.connect(host='localhost',port=3310,user='root',password='test123',db='testdb')
sql="select * from index_test"

result = pandas.read_sql_query(sql,conn)
result.to_csv(r'pandas_output.csv',index=False)

import pymysql
import pandas as pd
# import numpy as np
# 1. pymysql 연결 2. 쿼리 pandas에 날리고 table format 읽음 3. csv로 화면출력
'''
from sqlalchemy import create_engine
import pymysql
import pandas

# pymysql.connect.cursor(pymysql.cursors.DictCursor).execute(query)
# pymysql.connect.cursor.fetchall())

def main():
    db = pymysql.connect(
        user='root', 
        passwd='aaaa', 
        host='127.0.0.1', 
        db='db20193439',  # 내 db
        charset = 'utf8'
    )

    cursor = db.cursor(pymysql.cursors.DictCursor)

    sql = "select * from customer"
    # 저장 : df.to_sql(name=table, con=engine, if_exists='append')
    cursor.execute(sql)

    result = cursor.fetchall() # cursor는 fetchall(), fetchone(), fetchmany() 등 관리
    print(result[0])
    for row in result:
        i=row['customer_id']
        n=row['customer_name']
        s=row['customer_street']
        c=row['customer_city']
        print(i, n, s, c)
                  
    #df = pandas.DataFrame(result)



    raw_data = {'col0': [1, 2, 3, 4], 'col1': [10, 20, 30, 40], 'col2':[100, 200, 300, 400]}


if __name__ == '__main__':
    main()

'''

# 전체 보기
    print(df)
# 인덱스 보기
#print(df.columns)

# 0~2열 보기
#print(df.iloc[:, 0:3])

# 1, 4, 6행 보기
#print(df.iloc[[1, 4, 6]])
#print(df.iloc[[1, 4, 6], :])

# 0~2행 / 1, 4, 6열 보기
#print(df.iloc[0:3, [1, 4, 6]])

# 인덱스 명으로 특정 열 보기
#print(df.loc[:, ['id', 'name', 'birthday']])

### DB에 SQL query Insert (안됨)
url = 'mysql+mysqldb://root:aaaa@127.0.0.1:3306/db20193439'
engine = create_engine(url)
df_1 = pandas.DataFrame(raw_data)
df_1.to_sql('customer', con=engine, if_exists='append', index=False)
'''
