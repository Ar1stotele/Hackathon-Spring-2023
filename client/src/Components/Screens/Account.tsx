import { useContext, useEffect } from "react";

import UserInfoContext from "../../Store/userInformationContext";

function Account() {
  const userInfo = useContext(UserInfoContext);
  return (
    <div>
      <p className="text-center pt-4">
        Welcome to the Account {userInfo.username}
      </p>

      <div className="mx-[15%] mt-[10%]">
        <p>Carbon Emission Preserved: {userInfo.carbonEmission} KG</p>
        <p>Cans recycled: {userInfo.cansRecycled}</p>
        <p>Plastic bottles recycled: {userInfo.plasticBottlesRecycled}</p>
        <p>Total items recycled: {userInfo.totalItems}</p>
      </div>
    </div>
  );
}

export default Account;
