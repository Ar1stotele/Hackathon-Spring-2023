import { useContext } from "react";
import { useLocation } from "react-router-dom";
import { toast } from "react-hot-toast";

import UserInfoContext from "../../Store/userInformationContext";
import { Link } from "react-router-dom";
import { ROUTES } from "../../constants";

function Header() {
  const location = useLocation();
  const userInfoCtx = useContext(UserInfoContext);
  return (
    <div
      onClick={() => {
        if (userInfoCtx.username === "") {
          toast.error("Please sign in before using application :)");
        }
      }}
      className="flex justify-content items-center p-4 rounded-b-lg bg-[#F4EDEC] text-[20px] "
    >
      {userInfoCtx.username !== "" ? (
        <>
          <Link
            to={ROUTES.map}
            className={`flex-1 text-center ${
              location.pathname === ROUTES.map ? "text-blue-700 underline" : ""
            } `}
          >
            Map
          </Link>
          <Link
            to={ROUTES.recycle}
            className={`flex-1 text-center ${
              location.pathname === ROUTES.recycle
                ? "text-blue-700 underline"
                : ""
            } `}
          >
            Recycle
          </Link>
          <Link
            to={ROUTES.account}
            className={`flex-1 text-center ${
              location.pathname === ROUTES.account
                ? "text-blue-700 underline"
                : ""
            } `}
          >
            Account
          </Link>
        </>
      ) : (
        <>
          <p className="flex-1 text-center">Map</p>
          <p className="flex-1 text-center">Recycle</p>
          <p className="flex-1 text-center">Account</p>
        </>
      )}
    </div>
  );
}

export default Header;
