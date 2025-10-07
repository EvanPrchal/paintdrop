import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Auth0Provider } from "@auth0/auth0-react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css";
import App from "./App.tsx";
import Signup from "./Signup.tsx";
import Login from "./Login.tsx";
import Profile from "./Profile.tsx";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Auth0Provider
      domain="dev-v0mmlcufmyjsq8l7.us.auth0.com"
      clientId="xjhVNghS5CAYZauR7wN29od0KRF1rNAi"
      authorizationParams={{
        redirect_uri: window.location.origin,
      }}
    >
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </BrowserRouter>
    </Auth0Provider>
  </StrictMode>
);
