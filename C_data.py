import pandas 
import sqlite3

# First Query
df = pandas.read_csv("New_File.csv")
table_name = "MY_table"
f = open("real.db", "w")
conn = sqlite3.connect('real.db')
df.to_sql(table_name, conn, if_exists='append', index=False)

crsr = conn.cursor()
# SQL command to create a table in the database
# execute the statement
crsr.execute('''SELECT ((CLOSE-OPEN)/(OPEN)) AS Gain FROM MY_table ORDER BY (Gain) DESC limit 25''')
data = crsr.fetchall()
print("TOP 25 QUERIES ARE AS FOLLOWS :")
for d in data:
    print(d[0],end="\n")
# close the connection
conn.close()


# Second QUery
# Get datewise top 25 gainers for last 30 days as per point 4 above.
# for i in range(30):
#     df = pandas.read_csv("bahvcopies"+"f{i}"+".csv")
#     table_name = "MY_table"
#     f = open("real"+"f{i}"+".db", "w")
#     conn = sqlite3.connect("real"+"f{i}"+".db")
#     df.to_sql(table_name, conn, if_exists='append', index=False)

#     crsr = conn.cursor()
#     crsr.execute('''SELECT ((CLOSE-OPEN)/(OPEN)) AS Gain FROM MY_table ORDER BY (Gain) DESC limit 25''')
#     data = crsr.fetchall()
#     print("TOP 25 QUERIES ARE AS FOLLOWS :")
#     for d in data:
#         print(d[0],end="\n")


# #3rd Query
# # 3. Alternatively, you can also get a single list of the top 25 gainers based on open of the oldest day and close of latest day of those 30 days as per point 4.
# df = pandas.read_csv("bahvcopies0.csv")
# table_name = "MY_table0"
# f = open("real0.db", "w")
# conn = sqlite3.connect("real0.db")
# df.to_sql(table_name, conn, if_exists='append', index=False)
# crsr = conn.cursor()
# crsr.execute('''SELECT ((CLOSE-OPEN)/(OPEN)) AS Gain FROM MY_table ORDER BY (Gain) DESC limit 25''')
# data = crsr.fetchall()
# print("TOP 25 QUERIES ARE AS FOLLOWS :")
# for d in data:
#     print(d[0],end="\n")