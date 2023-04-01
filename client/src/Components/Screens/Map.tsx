import { useContext, useEffect, useState } from "react";
//AIzaSyC6z3oBXWg8eTlMucUaeSJDbAMcTy3ivxM
import UserInfoContext from "../../Store/userInformationContext";

function Map() {
  const userInfo = useContext(UserInfoContext);
  const [cords, setCords] = useState({ lat: 59.95, lng: 30.33 });
  useEffect(() => {
    // navigator.geolocation.watchPosition(function (position) {
    //   console.log("Latitude is :", position.coords.latitude);
    //   console.log("Longitude is :", position.coords.longitude);
    //   // setCords({
    //   //   lat: position.coords.latitude,
    //   //   lng: position.coords.longitude,
    //   // });
    // });
  }, []);
  return (
    <div>
      <p className="text-center pt-4">Welcome to the Map</p>
    </div>
  );
}

export default Map;
