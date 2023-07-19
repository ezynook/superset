import React, { useState, useEffect } from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import { embedDashboard } from "@superset-ui/embedded-sdk";
import "./Dashboard.css";
import axios from 'axios';

export default function Dashboard() {

  const [getToken, setGetToken] = useState<string>("");

  const dashboard = "2f0c57a1-d9e1-449a-ac6e-b5792f89372d";
  const url = "http://192.168.10.47:3000/get_token";

  // const login = async () => {
  //   const url = "http://192.168.10.47:8088/api/v1/security/login";

  //   const payload = {
  //     password: "tang",
  //     provider: "db",
  //     refresh: true,
  //     username: "tang"
  //   };

  //   const headers = {
  //     'Content-Type': 'application/json',
  //     "Access-Control-Allow-Origin": "*"
  //   };

  //   try {
  //     const response = await axios.post(url, payload, { headers });
  //     console.log(response); // Response data will be in response.data
  //     console.log("55555555555555555555555")
  //   } catch (error) {
  //     console.error(error);
  //     console.log("6666666666666666666666666")
  //   }

  // }

  const fetchToken = async () => {
    const response = await axios.get(url + "?dashboard_id=" + dashboard);

    if (response.status === 200) {
      setGetToken(String(response.data))
    }
  }

  useEffect(() => {
    void fetchToken();
  }, []);

  useEffect(() => {
    if (getToken) {
      embedSupersetDashboard();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [getToken]);


  const embedSupersetDashboard = () => {
    const token: string = getToken
    // const token = await fetchGuestTokenFromBackend();
    void embedDashboard({
      id: dashboard, // Given by the Superset embedding UI
      supersetDomain: "http://192.168.10.47:8088",
      mountPoint: document.getElementById("superset-container")!, // HTML element in which the iframe will render
      // eslint-disable-next-line @typescript-eslint/require-await
      fetchGuestToken: async () => token,
      dashboardUiConfig: {
        hideTitle: true,
      },
    });
  };

  return (
    <React.Fragment>
      <CssBaseline />
      <Container
        maxWidth={false}
        sx={{
          // bgcolor: "#cfe8fc",
          // maxWidth:'80%',
          height: "90vh",
          marginTop: "80px",
        }}
      >
        <div id="superset-container"></div>
      </Container>
    </React.Fragment>
  );
}
