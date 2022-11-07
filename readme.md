# full authenticator service
โปรเเกรมนี้ถูกสร้างด้วย python ทั้งหมด
โดยโปรเเกรมจะสร้าง sql database ออกมาเพื่อ save  username เเละ password เเล้วก็มีการ implement id เป็น integer ให้ user เเต่ละคนโดยอัตโนมัติ

<br>

function การทำงานพื้นฐานจะมีดังนี้
 - สร้าง account
 - ลบ account
 - authenticate acount

<br>

# วิธืการใช้งาน มีดังนี้
run file ที่ชื่อ api.py เพื่อเปิด server บริการ api 

server นี้ใช้ method get ทั้งหมด

## ถ้า สร้างสำเร็จ มันจะส่ง json {complete : True } หมายเหตุ username ห้ามซ้ำกัน

> https:blablabla.com/create_account?username=spa&?password=mypassword

## ถ้า authenticate ผ่าน json ที่มัน return กลับมาจะ มี {complete : True} เเละ username password ที่ได้รับกลับมาสำหรับ chack

> https:blablabla.com/auth?username=spa&?password=mypassword

## ถ้าสำเร็จจะ return complete เป็น true

> https:blablabla.com/delete_account?username=spa&?password=mypassword

# สิ่งที่ต้องมีคือ flask & sqlite3

> pip install Flask

> pip install Flask-RESTful

> pip install pysqlite3