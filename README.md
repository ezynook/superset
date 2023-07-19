<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Superset_logo.svg/2560px-Superset_logo.svg.png" width="200">

---
<img src="snapshot/img.png">

# Apache Superset

### 👉 วิธีการติดตั้ง
ก่อนการติดตั้งต้องมี Docker engine ก่อน โดยสามารถดาวน์โหลดได้ที่ 
* [Windows](https://docs.docker.com/desktop/install/windows-install/)
* [Linux and macOS](https://docs.docker.com/desktop/install/linux-install/)

### 👉 ดาวน์โหลดและการใช้งาน
```bash
cd /path/to/superset
git clone https://github.com/ezynook/superset.git
```
```bash
docker-compose up -d --build
```
__เช็คสถานะการทำงานด้วยคำสั่ง ```docker ps``` จากนั้นดูสถานะดังนี้__

```sh
+-----------------------------------------------------------------------------------------------------------------+
CONTAINER ID   IMAGE                COMMAND        CREATED         STATUS         PORTS                    NAMES
+-----------------------------------------------------------------------------------------------------------------+
2e25b96b399a   ghcr.io/ezynook...   "softnix.sh"   3 seconds ago   Up 2 seconds   0.0.0.0:8088->8088/tcp   superset 
-------------------------------------------------------------------------------------------------------------------
```
---

### 👉 SDK Embedded Dashboard
[วิธีการใช้งาน SDK](https://github.com/ezynook/superset/blob/main/SDK-Dashboard/README.md)

__เลือกใช้งานได้ 2 ภาษา__
* PHP
* Python (Flask Framework)

PHP ให้ Copy file ```index.php``` ไปยัง path document web เช่น ```/var/www/html```
```bash
cd SDK-Dashboard/PHP/
```
Python Flask
```bash
cd SDK-Dashboard/Python/
python app.py
```
Run On Detach
```bash
yum install -y nodejs npm
npm install -g pm2
```
Running
```bash
pm2 start --name "Superset SDK" python app.py
```

---

> Author: __Pasit.y__