import { QrCodeReader } from "../QrCodeReader/QrCodeReader";

function Recycle() {
  return (
    <div>
      <p className="text-center pt-4">Welcome to the Recycle</p>
      <QrCodeReader />
    </div>
  );
}

export default Recycle;
