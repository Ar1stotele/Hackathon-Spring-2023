import { useContext } from "react";

import UserInfoContext from "../../Store/userInformationContext";

function GuestPage() {
  const userInfo = useContext(UserInfoContext);
  return (
    <div>
      <p className="text-center pt-4">Welcome to the GeoRecycler</p>
      {userInfo.username == "" ? (
        <button
          className="text-center bg-blue-100 mx-10 rounded-md mt-10 w-[80%]"
          onClick={() => {
            userInfo.setUsername("Giorgi");
          }}
        >
          Authenticate With Google
        </button>
      ) : (
        <p className="text-center mt-20">Welcome dear {userInfo.username}</p>
      )}
    </div>
  );
}

export default GuestPage;
