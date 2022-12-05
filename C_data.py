import pandas 
import sqlite3
import time
# from datetime import timedeltas_date2

# First Query
df = pandas.read_csv("New_File.csv")
table_name = "MY_table"
f = open("real.db", "w")
conn = sqlite3.connect('real.db')
df.to_sql(table_name, conn, if_exists='append', index=False)

crsr = conn.cursor()
# SQL command to create a table in the database
# execute the statement
crsr.execute('''SELECT `NAME OF COMPANY`, ((CLOSE-OPEN)/(OPEN)) AS Gain FROM MY_table ORDER BY (Gain) DESC limit 25''')
data = crsr.fetchall()
print("TOP 25 QUERIES ARE AS FOLLOWS :")
for d in data:
    print(d,end="\n")
# close the connection
conn.close()


# Second QUery
# Get datewise top 25 gainers for last 30 days as per point 4 above.
count =1
for i in range(30):
    df = pandas.read_csv('bhavcopies'+f"{count}"+'.csv')
    column = df["TIMESTAMP"]
    print(column[0])
    merged = pandas.read_csv('bhavcopies'+f"{count}"+'.csv')
    merged.to_csv('New_File'+f"{count}"+'.csv')
    df = pandas.read_csv('D:/program/INTERN_ASSIGNMENT'+'/New_File'+f"{count}"+'.csv')
    table_name = "MY_table"
    f = open('real'+f"{count}"+'.db', "w")
    conn = sqlite3.connect('real'+f"{count}"+'.db')
    df.to_sql(table_name, conn, if_exists='append', index=False)

    crsr = conn.cursor()
    crsr.execute('''SELECT SYMBOL, ((CLOSE-OPEN)/(OPEN)) AS Gain FROM MY_table ORDER BY (Gain) DESC limit 25''')
    data = crsr.fetchall()
    print("TOP 25 QUERIES ARE AS FOLLOWS :")
    for d in data:
        print(d,end="\n")
    count+=1
    print()
    time.sleep(1)
    # print(count)


#3rd Query
# 3. Alternatively, you can also get a single list of the top 25 gainers based on open of the oldest day and close of latest day of those 30 days as per point 4.
# df = pandas.read_csv("bahvcopies1.csv")
# df.to_csv('New_File'+f"{count}"+'.csv')
table_name1 = "MY_table1"
table_name2 = "MY_table2"

df1 = pandas.read_csv('bhavcopies1.csv')
df2 = pandas.read_csv('bhavcopies1.csv')
f = open("real_new.db", "w")
conn = sqlite3.connect("real_new.db")
df1.to_sql(table_name1, conn, if_exists='append', index=False)
crsr = conn.cursor()
df2.to_sql(table_name2, conn, if_exists='append', index=False)
crsr.execute('''SELECT MY_table1.SYMBOL, ((MY_table1.CLOSE-MY_table2.OPEN)/(MY_table2.OPEN)) AS Gain FROM MY_table1 FULL OUTER JOIN MY_table2 on MY_table1.OPEN = MY_table2.CLOSE ORDER BY (Gain) DESC limit 25''')
data = crsr.fetchall()
print("TOP 25 QUERIES ARE AS FOLLOWS Based on open of the oldest day and close of the latest day:")
for d in data:
    print(d,end="\n")