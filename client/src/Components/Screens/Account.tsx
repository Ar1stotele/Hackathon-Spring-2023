import { useContext, useEffect } from "react";

import UserInfoContext from "../../Store/userInformationContext";
import { fetchAccountStatistics } from "../../API/fetchAccountStatistics";

function Account() {
  const userInfo = useContext(UserInfoContext);
  useEffect(() => {
    (async () => {
      const data = await fetchAccountStatistics();
      console.log({ data });
      console.log(typeof data.cans);
      userInfo.setCarbonEmission(data.Carbon)
      userInfo.setCansRecycled(data.cans)
      userInfo.setGlassBottlesRecycled(data.glass)
      userInfo.setPlasticBottlesRecycled(data.plastic)
      
      
    })();
  }, []);
  return (
    <div>
      <p className="text-center pt-4">
        Welcome to the Account {userInfo.username}
      </p>

      <div className="mx-[15%] mt-[10%]">
        <p>Carbon Emission Preserved: {userInfo.carbonEmission} KG</p>
        <p>Cans recycled: {userInfo.cansRecycled}</p>
        <p>Plastic bottles recycled: {userInfo.plasticBottlesRecycled}</p>
        <p>Glass bottles recycled: {userInfo.glassBottlesRecycled}</p>
      </div>
    </div>
  );
}

export default Account;
