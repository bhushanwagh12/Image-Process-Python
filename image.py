import sqlite3 as s
import pytesseract
from PIL import Image

conn=s.connect("motor6.db")
print(conn)
curs=conn.cursor()
id=int(input("IDno :"))
if(id!=102):

    print("IDNo is existed ")
else:
    print("Invalid IDNo")
try:
    curs.execute("insert into vehicle6 values (101,'MH-12DE1433')")
    curs.execute("select name from vehicle6")
    res=curs.fetchone()

    sre=curs.execute("select * from vehicle6 where idno=101")
    print(curs.fetchone())



    curs.execute("create table vehicle6(idno number,name text)")
except s.OperationalError:
    print("Database table already exist")
print("table is created")

conn.commit()
print("data inserted ..")
conn.close()
print("database connection closed ...")



img=Image.open('vehicle.jpg')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
text=pytesseract.image_to_string(img)
print(text)