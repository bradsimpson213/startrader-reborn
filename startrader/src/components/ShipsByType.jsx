import React, { useEffect, useState } from "react";
import ShipResults from "./ShipResults";

const UniqueShips = ({type}) => {
  const [ships, setShips] = useState(null);
  useEffect(() => {
    (async () => {
      const res = await fetch(`/ships/class/${type}`);
      const data = await res.json();
      setShips(data.star_ships);
    })();
  }, [type]);
  return <ShipResults title={`${type}s`} ships={ships} />;
};

export default UniqueShips;
