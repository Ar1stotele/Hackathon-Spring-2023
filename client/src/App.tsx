import { Toaster } from "react-hot-toast";
import { Route, useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import Header from "./Components/UI/Header";
import { Navigation } from "./Navigation/Navigation";
import { useContext, useEffect } from "react";
import { ROUTES } from "./constants";
import UserInfoContext from "./Store/userInformationContext";

function App() {
  const location = useLocation();
  const navigate = useNavigate();
  const userInfoCtx = useContext(UserInfoContext);

  useEffect(() => {
    if (location.pathname !== ROUTES.guest && userInfoCtx.username == "") {
      navigate(ROUTES.guest);
    }
  }, [location.pathname]);
  return (
    <div className="App">
      <Toaster />
      <Header />
      <Navigation />
    </div>
  );
}

export default App;
