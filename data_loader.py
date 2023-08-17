import pypyodbc as odbc # pip install pypyodbc
import pandas as pd # pip install pandas

"""
Step 1. Importing dataset from CSV
"""
datafile = pd.read_csv('Incident_Reports.csv')

"""
Step 2.1 Data clean up
"""
datafile['Published Date'] = pd.to_datetime(datafile['Published Date']).dt.strftime('%Y-%m-%d %H:%M:%S')
datafile['Status Date'] = pd.to_datetime(datafile['Published Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

datafile.drop(datafile.query('Location.isnull() | Status.isnull()').index, inplace=True)


"""
Step 2.2 Specify columns we want to import
"""
columns = ['Incident ID', 'Published Date', 'Issue Reported', 'Location', 
            'Address', 'Status', 'Status Date']

df_data = datafile[columns]
records = df_data.values.tolist()


"""
Step 3.1 Create SQL Servre Connection String
"""
DRIVER = 'SQL Server'
SERVER_NAME = '<Server Name>'
DATABASE_NAME = '<Database Name>'

def connection_string(driver, server_name, database_name):
    conn_string = f"""
        DRIVER={{{driver}}};
        SERVER={server_name};
        DATABASE={database_name};
        Trust_Connection=yes;        
    """
    return conn_string

"""
Step 3.2 Create database connection instance
"""
try:
    conn = odbc.connect(connection_string(DRIVER, SERVER_NAME, DATABASE_NAME))
except odbc.DatabaseError as e:
    print('Database Error:')    
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))


"""
Step 3.3 Create a cursor connection and insert records
"""

sql_insert = '''
    INSERT INTO incidents 
    VALUES (?, ?, ?, ?, ?, ?, ?, GETDATE())
'''

try:
    cursor = conn.cursor()
    cursor.executemany(sql_insert, records)
    cursor.commit();    
except Exception as e:
    cursor.rollback()
    print(str(e[1]))
finally:
    print('Task is complete.')
    cursor.close()
    conn.close()
