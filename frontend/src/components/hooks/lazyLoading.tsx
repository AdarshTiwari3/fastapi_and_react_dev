import { useMemo, useState } from "react";

const LazyLoading = () => {
  const [data, setData] = useState(false);

  const expensiveComputation = useMemo(() => {
    // this will only recompute when `data` changes
    for (let i = 0; i < 1000000; i++) {}
    return "Computation done!";
  }, [data]);

  const handleClick = () => {
    setData(true); // update state
  };

  return (
    <div>
      <p onClick={handleClick}>
        Lazy Loading Example - {data ? expensiveComputation : "Not done"}
      </p>
    </div>
  );
};

export default LazyLoading;
