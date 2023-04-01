import { useState } from "react";
import { QrReader } from "react-qr-reader";

export const QrCodeReader = () => {
  const [data, setData] = useState("");

  return (
    <>
      {data === "" ? (
        <QrReader
          onResult={(result: any, error: any) => {
            if (!!result) {
              setData(result?.text);
            }

            if (!!error) {
              console.info(error);
            }
          }}
          constraints={{ facingMode: "user" }}
        />
      ) : (
        <p>{data}</p>
      )}
    </>
  );
};
