<img src="https://repository-images.githubusercontent.com/39464018/58649580-eca4-11ea-844d-c2ddca24b226" width="200">

---

# Step Embedded Apache Superset

### สร้างไฟล์ ```superset_config.py```
ตั้งค่าให้เหมือน Code นี้
```py
import os

ROW_LIMIT = 5000
WEBSERVER_THREADS = 8
SUPERSET_WEBSERVER_PORT = 8088
SUPERSET_WEBSERVER_TIMEOUT = 300
SECRET_KEY=os.environ.get('SECRET_KEY')
WTF_CSRF_ENABLED = False
WTF_CSRF_EXEMPT_LIST = []
MAPBOX_API_KEY = ''
SESSION_COOKIE_SAMESITE = None
ENABLE_PROXY_FIX = True
PUBLIC_ROLE_LIKE = "Gamma"
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/superset'

CORS_OPTIONS = {
  'supports_credentials': True,
  'allow_headers': ['*'],
  'resources':['*'],
  'origins': ['*']
}
```
---

### แก้ไขสิทธิ Role ```Gamma```
> Menu: settings > List Roles

__เปิดสิทธิตาม Ketword ดังนี้__
* all_*
* can grant guest token
* เปิดทุกสิทธิที่เกี่ยวกับ ```Datasource``` ```menu access``` ```dashboard``` ```embed```
---
### สร้าง User สำหรับ Public Dashboard
> Menu: settings > List Users

__กรอกข้อมูลดังนี้__
```py
[
    "First Name": "test"
    "Last Name": "test"
    "Is Active ?" [/]
    "Email": "something@mail.com"
    "Role": "Gamma"
    "Password": "*****"
    "Confirm Password": "*****"
]
```
---
### ไปสร้าง Dashboard และ Charts ภายใต้ Username ที่สร้างสำหรับ Public dashboard
* สร้าง Charts
* นำ Charts ไปผูกกับ Dashboard
---
### สร้าง Embed Dashboard ID
> Menu: Dashboard > ... > Embed dashboard
* ช่อง Allows Domains ปล่อยว่างๆ  = ```Allow All Domains```
* กด Save Changes
* 📋 __Copy SDK id มา__
---
### สร้าง Token ในการ Access Dashboard
__สร้าง Token Login__ | Route: ```/api/v1/security/login```
```json
//JSON Body
{
  "password": "test",
  "provider": "db",
  "refresh": true,
  "username": "test"
}
```
> หลังจากนั้นจะได้ ```access_token``` มาให้ทำการ Copy ไว้

__สร้าง Guest Token__ | Route: ```/api/v1/security/guest_token/```

> นำ ```access_token``` ที่ได้มาใส่ที่ Header -> Bearear Key
```json
//JSON Body
{
  "resources": [
    {
      "id": "6e96c9aa-95f9-47f8-8046-fa764f94faaf", //Dashboard Embed id 
      "type": "dashboard"
    }
  ],
  "rls": [
  ],
  "user": {
    "first_name": "test",
    "last_name": "test",
    "username": "test"
  }
}
```
---

---
__Author:__ ```Pasit Y.```