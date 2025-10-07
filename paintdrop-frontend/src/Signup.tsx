import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

type createUserRequest = {
  username: string;
  email: string;
  password: string;
};

const Signup = () => {
  const [user, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (e: any) => {
    const payload: createUserRequest = {
      username: user,
      email: email,
      password: password,
    };

    fetch("http://localhost:8000/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
      mode: "cors",
    });
    console.log(payload);

    // navigates to login page after account creation
    e.preventDefault();
    alert(`Account Created! Username is: ${user}`);
    navigate(`/login`);
  };
  return (
    <div className="flex flex-col items-center bg-paint-white p-[5%]">
      <h1 className="text-header text-paint-blue">Welcome to Paintdrop</h1>
      <h2 className="text-subheader text-paint-blue mb-[2%]">Please Sign Up</h2>
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
          className="border-2 border-[#e1e1e1] rounded-full p-[3.5%] px-[7.5%] w-2xl"
          required
          type="text"
          name="email"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
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
          Sign Up
        </button>
      </form>
      <Link to="/login" className="underline text-[#b8b9b8] font-body text-[30px] text-center">
        Already signed up?
      </Link>
    </div>
  );
};

export default Signup;
