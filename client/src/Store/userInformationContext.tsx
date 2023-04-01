import { createContext, FC, ReactNode, SetStateAction, useState } from "react";

// Calendar Info Context - Stores information related to the Pages: Intro and Form;
export interface UserInfoContextInterface {
  balance: string;
  username: string;
  carbonEmission: number;
  plasticBottlesRecycled: number;
  glassBottlesRecycled: number;
  cansRecycled: number;

  setBalance: (arg: SetStateAction<string>) => void;
  setUsername: (arg: SetStateAction<string>) => void;
  setCarbonEmission: (arg: SetStateAction<number>) => void;
  setPlasticBottlesRecycled: (arg: SetStateAction<number>) => void;
  setGlassBottlesRecycled: (arg: SetStateAction<number>) => void;
  setCansRecycled: (arg: SetStateAction<number>) => void;
}

const UserInfoContext = createContext<UserInfoContextInterface>({
  balance: "0.0",
  username: "",
  carbonEmission: 0,
  plasticBottlesRecycled: 0,
  glassBottlesRecycled: 0,
  cansRecycled: 0,

  setBalance: (arg: SetStateAction<string>) => {},
  setUsername: (arg: SetStateAction<string>) => {},
  setCarbonEmission: (arg: SetStateAction<number>) => {},
  setPlasticBottlesRecycled: (arg: SetStateAction<number>) => {},
  setGlassBottlesRecycled: (arg: SetStateAction<number>) => {},
  setCansRecycled: (arg: SetStateAction<number>) => {},
});

type Props = {
  children?: ReactNode;
};

export const UserInfoContextProvider: FC<Props> = ({ children }: Props) => {
  const [balance, setBalance] = useState("0.0");
  const [username, setUsername] = useState("");
  const [plasticBottlesRecycled, setPlasticBottlesRecycled] = useState(0);
  const [glassBottlesRecycled, setGlassBottlesRecycled] = useState(0);
  const [cansRecycled, setCansRecycled] = useState(0);
  const [carbonEmission, setCarbonEmission] = useState(0);

  return (
    <UserInfoContext.Provider
      value={{
        balance,
        username,
        carbonEmission,
        plasticBottlesRecycled,
        glassBottlesRecycled,
        cansRecycled,

        setBalance,
        setUsername,
        setCarbonEmission,
        setPlasticBottlesRecycled,
        setGlassBottlesRecycled,
        setCansRecycled,
      }}
    >
      {children}
    </UserInfoContext.Provider>
  );
};

export default UserInfoContext;
