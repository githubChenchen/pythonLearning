import sqlite3
conn = sqlite3.connect('school.db')
cursor = conn.cursor()
print('数据库已打开')
cursor.execute("drop table student1")
cursor.execute('''create table student1(ID int primary key not null,Name text not null,Age int not null,Score real,Address char(50))''')
print('创建表成功')
cursor.execute("insert into student1 values(1001,'张小山',20,581,'辽宁沈阳')")
cursor.execute("insert into student1 values(1002,'张小四',21,582,'辽宁大连')")
cursor.execute("insert into student1 values(1003,'张小无',22,583,'江苏南京')")
cursor.execute("insert into student1 values(1004,'张小六',23,585,'江苏镇江')")
cursor.execute("insert into student1 values(1005,'张小其',22,589,'江苏无锡')")
cursor.execute("insert into student1 values(1006,'张小吧',21,589,'江苏苏州')")
cursor.execute("insert into student1 values(1007,'张小就',26,589,'江苏徐州')")
conn.commit()
for row in cursor.execute('select * from student where ID = 1002'):
    print(row)
conn.close
