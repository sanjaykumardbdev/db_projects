# https://developer.oracle.com/dsl/prez-python-queries.html
from pprint import pprint
from tkinter import *
import cx_Oracle


 # '1 ..........................'
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
cur = conn.cursor()
cur1 = conn.cursor()

print(conn.version)
print(conn.dsn)

 # '3 ..........................'
db = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/XE')
db_cur = db.cursor()

print(db.version)
print(db.dsn)

# -- '4 ..........................'
db1 = cx_Oracle.connect('scott/tiger@localhost:1521/XE')
db1_cur = db1.cursor()

print(db1.version)
print(db1.dsn)
versioning = db1.version.split('.')
print(versioning)

# print(type(versioning[0]))

if versioning[0] == '11':
    print('using 11g')
else:
    print('other version')




stmt = 'select sysdate from dual'

output = cur.execute(stmt).fetchone()
print(output[0])
output = db_cur.execute(stmt).fetchone()
print(output[0])
output = db1_cur.execute(stmt).fetchone()
print(output[0])


stmt = 'select * from emp'

output = cur.execute(stmt).fetchone()
print(output[0])
output = db_cur.execute(stmt).fetchone()
print(output[0])
output = db1_cur.execute(stmt).fetchone()
print(output[0])



# execute :
print('------------------------- execute create insert delete---------------------')

stmt1 = 'drop table py_test'
cur.execute(stmt1)

stmt = 'create table py_test(id number(9), name varchar2(9), address varchar2(9))'
cur.execute(stmt)


stmt = 'delete from py_test'
cur.execute(stmt)
conn.commit()


stmt = "insert into py_test(id,name,address) values (1,'san', 'blr')"
cur.execute(stmt)
conn.commit()

stmt = "insert into py_test(id,name,address) values (1,'sanjay', 'blr1')"
cur.execute(stmt)
conn.commit()


stmt = "insert into py_test(id,name,address) values (:a, :b, :c)"

# cur.bindarraysize = 1
# cur.setinputsizes(int, 40)
# ----------------------------------------- values
id = 1
name = 'r_sanjay'
address = 'brl11'

id1 = 11
name1 = 'r_jay'
address1 = 'brl11'
# ----------------------------------------- qry

row = (id, name, address)
cur.execute(stmt, row)
conn.commit()


row = [(id, name, address), (id1+2, name1, address1), (id1+1, name1, address1) ]
cur.executemany(stmt, row)
conn.commit()
# -----------------------------------------

# -----------------------------------------fetch(optional)
print('------------------------- execute fetch ---------------------')

stmt = 'select * from py_test order by 1'

py_list11 = cur.execute(stmt)
cnt = 0
for i in py_list11:
    print(str(cnt+1) + ' ' + str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))
    # print(str(i[0]) + ' \t' + str(i[1]) + ' \t\t' + str(i[2]))
    cnt += 1


print('------------------------- execute one ---------------------')
py_list1 = cur.execute(stmt).fetchone()
print(str(py_list1[0]) + '  '+ str(py_list1[1]) + '   '+ str(py_list1[2]))

print('id is : {}'.format(py_list1[0]))
print('name is : {}'.format(py_list1[1]))
print('Address is : {}'.format(py_list1[2]))

print('id is : {} name is : {} Address is : {}'.format(py_list1[0], py_list1[1], py_list1[2]))

print('------------------------- execute one end ---------------------')
print('-----------------------------------------fetchall start')


cur.execute('select * from py_test order by 1')
pprint(cur.fetchall())

print('-----------------------------------------fetchall end')


print('-----------------------------------------fetchmany(4) start')
cur.execute('select * from py_test order by 1')
pprint(cur.fetchmany(4))
print('-----------------------------------------fetchmany(4) end')

print('------------------------------------------')
cur.execute('select * from py_test order by 1')
print(cur.fetchmany(2))
print('------------------------------------------')

lst1 = cur.fetchmany(2)
for i in lst1:
    print(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))
print('done')

print('------------------Description ------------------------')
cur.fetchall()
pprint(cur.description)

print('------------------Data Types ------------------------')
dt = cur.execute('select * from py_test')
print(dt)

print('------------------Bind Variable Patterns ------------------------')

cur.execute('select empno, ename, sal from emp where deptno = 10')
# pprint(cur.fetchall())

cur.execute('select empno, ename, sal from emp where deptno = 20 and sal >= 2800')
# pprint(cur.fetchall())

#  Bind variable by name:

param1 = {'deptno': 20, 'sal': 2800}
cur.execute('select empno, ename, sal from emp where deptno = :deptno and sal >= :sal', param1)
print(cur.bindnames())

cur1.execute('select empno, ename, sal from emp where deptno = :deptno1 and sal >= :sal1', deptno1=20, sal1=2800)
pprint(cur1.fetchall())
print(cur1.bindnames())

print('------------------Bind Variable Patterns with exception------------------------by position')

r1 = cur.execute('select empno, ename, sal from emp where deptno = :1 and sal >= :2', (20, 2800))
r1 = cur.execute('select empno, ename, sal from emp where deptno = :9 and sal >= :4', (20, 2800))
r1 = cur.execute('select empno, ename, sal from emp where deptno = :0 and sal >= :m', (20, 2800))


cur.prepare('select empno, ename, sal from emp where deptno = :deptno and sal >= :sal')
cur.execute(None, {'deptno': 20, 'sal': 2800})
print(len(cur.fetchall()))
