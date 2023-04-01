import axios from "axios";
import { API } from "../constants";

// to send verification code on email through server
export async function fetchAccountStatistics() {
  //   requestBody: {
  //     carbonEmission: string;
  //     plasticBottlesRecycled: string;
  //     glassBottlesRecycled: string;
  //     cansRecycled: string;
  //   },
  return (await axios.get(`${API.address}${API.routes.data}`)).data;
}
