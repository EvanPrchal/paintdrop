import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

type LoginResponse = {
  disabled: boolean | null;
  username: string;
  hashed_password: string;
  email: string;
  access_token: string | null;
};

const Login = () => {
  const { loginWithRedirect } = useAuth0();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();
  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const formData = new URLSearchParams();
    formData.append("grant_type", "password");
    formData.append("username", username);
    formData.append("password", password);

    const response = await fetch("http://localhost:8000/auth/token", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formData.toString(),
    });
    if (response.ok) {
      const data: LoginResponse = await response.json();
      if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        alert("Succesfully logged in!");
        navigate(`/profile/${username}`, { state: { username: username } });
      }
    } else {
      alert("Incorrect username or password");
    }
  };

  return (
    <div className="flex flex-col items-center bg-paint-white p-[5%]">
      <h1 className="text-header text-paint-blue">Welcome to Paintdrop</h1>
      <h2 className="text-subheader text-paint-blue mb-[2%]">Please Log In</h2>
      <form className="flex flex-col justify-around gap-7 text-body items-center" onSubmit={handleSubmit}>
        <input
          className="border-2 border-[#e1e1e1] rounded-full p-[3.5%] px-[7.5%] w-2xl"
          required
          type="text"
          name="username"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          className="border-2 border-[#e1e1e1] rounded-full p-[3.5%] px-[7.5%] mb-[7.5%] w-2xl"
          required
          type="password"
          name="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          className={`rounded-full px-4 w-3xs border-4 text-body mb-[10%] 
             bg-paint-blue hover:bg-paint-white hover:text-paint-blue active:bg-paint-black border-paint-blue text-paint-white`}
        >
          Log In
        </button>
      </form>
      <Link to="/signup" className="underline text-[#b8b9b8] font-body text-[30px] text-center">
        Not signed up?
      </Link>
    </div>
  );
};

export default Login;
