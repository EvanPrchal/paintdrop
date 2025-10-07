import { Link } from "react-router";
import Logo from "./components/Logo";
import { useAuth0 } from "@auth0/auth0-react";

function App() {
  const { loginWithRedirect } = useAuth0();
  const { logout } = useAuth0();

  return (
    <div className="flex flex-col text-center items-center bg-paint-grey justify-around h-screen">
      <section className="text-paint-black">
        <h2 className="text-header font-logotype -mb-[5%] text-paint-white">Welcome to</h2>
        <Logo />
        <h3 className="mt-[7.5%] text-subheader font-body text-paint-white underline">Get Started</h3>
      </section>
      <section className="text-body w-full flex justify-around">
        <button
          onClick={() => loginWithRedirect()}
          className={`rounded-full px-4 w-3xs border-4 text-body border-paint-grey text-paint-grey 
             bg-paint-white hover:bg-paint-grey active:bg-paint-black hover:border-paint-white hover:text-paint-white`}
        >
          Log In
        </button>
        <button
          onClick={() => logout({ logoutParams: { returnTo: window.location.origin } })}
          className={`rounded-full px-4 w-3xs border-4 text-body border-paint-grey text-paint-grey 
             bg-paint-white hover:bg-paint-grey active:bg-paint-black hover:border-paint-white hover:text-paint-white`}
        >
          Log Out
        </button>
      </section>
    </div>
  );
}

export default App;
