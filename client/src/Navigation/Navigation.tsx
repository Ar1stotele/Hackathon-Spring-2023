import { Route, Routes } from "react-router-dom";
import Account from "../Components/Screens/Account";
import GuestPage from "../Components/Screens/GuestPage";
import Map from "../Components/Screens/Map";
import { ROUTES } from "../constants";
import Recycle from "../Components/Screens/Recycle";

export function Navigation() {
  return (
    <Routes>
      {/* <Route path="/test" element={<Test />} /> */}
      <Route path={ROUTES.guest} element={<GuestPage />} />
      <Route path={ROUTES.account} element={<Account />} />
      <Route path={ROUTES.map} element={<Map />} />
      <Route path={ROUTES.recycle} element={<Recycle />} />
    </Routes>
  );
}
