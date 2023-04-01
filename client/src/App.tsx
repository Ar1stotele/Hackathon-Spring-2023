import { Toaster } from "react-hot-toast";
import { Route, useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import Header from "./Components/UI/Header";
import { Navigation } from "./Navigation/Navigation";
import { useContext, useEffect } from "react";
import { ROUTES } from "./constants";
import UserInfoContext from "./Store/userInformationContext";
import { fetchAccountStatistics } from "./API/fetchAccountStatistics";

function App() {
  const location = useLocation();
  const navigate = useNavigate();
  const userInfo = useContext(UserInfoContext);

  useEffect(() => {
    (async () => {
      const data = await fetchAccountStatistics();
      userInfo.setCarbonEmission(data.totalCarbon);
      userInfo.setCansRecycled(data.cans);
      userInfo.setTotalItems(data.totalItems);
      userInfo.setPlasticBottlesRecycled(data.plasticBottles);
    })();
    if (location.pathname !== ROUTES.guest && userInfo.username == "") {
      navigate(ROUTES.guest);
    }
  }, [location.pathname]);
  return (
    <div className="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 h-[100vh]">
      <Toaster />
      <Header />
      <div className="text-white">
        <Navigation />
      </div>
    </div>
  );
}

export default App;
