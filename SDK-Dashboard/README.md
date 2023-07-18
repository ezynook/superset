<img src="https://repository-images.githubusercontent.com/39464018/58649580-eca4-11ea-844d-c2ddca24b226" width="200">

---

# Step Embedded Apache Superset

### สร้างไฟล์ ```superset_config.py```
ตั้งค่าให้เป๊ะๆตาม Code นี้
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
  'origins': ['http://localhost:8088', 'http://localhost:8888']
}
```
---

### แก้ไขสิทธิ Role ```Gamma```
> Menu: settings > List Roles

__เปิดสิทธิตาม Ketword ดังนี้__
* all_*
* can grant guest token
* เปิดทุดสิธิที่เกี่ยวกับ ```Datasource``` ```menu access``` ```dashboard```
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
* ช่อง Allows Domains ปล่อยว่างๆไว้
* กด Save Changes
* __Copy SDK id มา__
---
### สร้าง Token ในการ Access Dashboard
__สร้าง Token Login__
Route: ```/api/v1/security/login```
```json
//JSON Values
{
  "password": "test",
  "provider": "db",
  "refresh": true,
  "username": "test"
}
```
__สร้าง Guest Token__
Route: ```/api/v1/security/guest_token/```
```json
//JSON Values
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
### สร้างไฟล์ ```index.php```
```php
<?php
date_default_timezone_set("Asia/Bangkok");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");

class Superset_API {

	private $SUPERSET_HOST = "http://192.168.10.47:8088";
	private $USERNAME = "test";
	private $PASSWORD = "test";
	private $DASHBOARD = "6e96c9aa-95f9-47f8-8046-fa764f94faaf";

	public function get_token() {
		$curl = curl_init();

		curl_setopt_array($curl, array(
			CURLOPT_URL => $this->SUPERSET_HOST . "/api/v1/security/login",
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_ENCODING => '',
			CURLOPT_MAXREDIRS => 10,
			CURLOPT_TIMEOUT => 0,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
			CURLOPT_CUSTOMREQUEST => 'POST',
			CURLOPT_POSTFIELDS => '{
                "password": "' . $this->PASSWORD . '",
                "provider": "db",
                "refresh": true,
                "username": "' . $this->USERNAME . '"
            }',
			CURLOPT_HTTPHEADER => array(
				'Content-Type: application/json',
			),
		));

		$response = curl_exec($curl);

		curl_close($curl);
		$arr = json_decode($response, 1);
		$result = $arr['access_token'];
		$res = $this->guest_token($result);
		return $res;
	}
	public function guest_token($b_key) {
		$curl = curl_init();
		curl_setopt_array($curl, array(
			CURLOPT_URL => $this->SUPERSET_HOST . '/api/v1/security/guest_token/',
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_ENCODING => '',
			CURLOPT_MAXREDIRS => 10,
			CURLOPT_TIMEOUT => 0,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
			CURLOPT_CUSTOMREQUEST => 'POST',
			CURLOPT_POSTFIELDS => '{
                "resources": [
                    {
                      "id": "' . $this->DASHBOARD . '",
                      "type": "dashboard"
                    }
                  ],
                  "rls": [
                  ],
                  "user": {
                    "first_name": "' . $this->USERNAME . '",
                    "last_name": "' . $this->USERNAME . '",
                    "username": "' . $this->USERNAME . '"
                  }
            }',
			CURLOPT_HTTPHEADER => array(
				'Content-Type: application/json',
				'Authorization: Bearer ' . $b_key,
			),
		));

		$response = curl_exec($curl);
		curl_close($curl);
		$arr = json_decode($response, 1);
		return $arr['token'];

	}
}

$obj = new Superset_API();
echo "
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset='utf-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1'>
            <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css'>
            <title>Test</title>
            <style type='text/css'>
                    iframe {
                            width: 100%;
                            height: 800px;
                            border: none;
                            border-width: 0;
                    }
            </style>
        </head>
        <body>
            <nav class='navbar navbar-light bg-light justify-content-between'>
                    <a class='navbar-brand'>
                            <img src='https://repository-images.githubusercontent.com/39464018/58649580-eca4-11ea-844d-c2ddca24b226'
                                    width='90'>
                            <span class='badge rounded-pill bg-secondary text-white'>Apache Superset Public Dashboard</span>
                    </a>
            </nav>
            <div id='myDiv' class='container-fluid mt-5'></div>
            <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.1/jquery.min.js'></script>
            <script src='https://unpkg.com/@superset-ui/embedded-sdk'></script>
            <script>
                    const mydata = supersetEmbeddedSdk.embedDashboard({
                        id: '6e96c9aa-95f9-47f8-8046-fa764f94faaf',
                        supersetDomain: 'http://192.168.10.47:8088',
                        mountPoint: document.getElementById('myDiv'),
                        fetchGuestToken: () => '{$obj->get_token()}',
                        dashboardUiConfig: { hideTitle: true }
                    });
            </script>
        </body>
        </html>
";
?>
```
---
__Author:__ ```Pasit Y.```