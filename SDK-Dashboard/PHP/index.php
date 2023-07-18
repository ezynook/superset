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