import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import DrawerLeft from './components/DrawerLeft'
import Dashboard from "./components/Dashboard";
import { createTheme, ThemeProvider } from '@mui/material/styles';


export default function App() {
  const theme = createTheme({
    palette: {
      primary: {
        main: '#4caf50',
      },
      secondary: {
        main: '#00e676',
      },
    },
  });

  return (
    <>
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <DrawerLeft />
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/home" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
      </ThemeProvider>
    </>
  )
}

