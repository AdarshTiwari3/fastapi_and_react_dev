import { useEffect, useState } from "react";

const UseEffectHook = () => {
  const [count, setCount] = useState<number>(0);

  const handleClick = () => {
    setCount((prev: number) => prev + 1);
  };

  useEffect(() => {
    const timer = setTimeout(() => {
      console.log("I am inside useeffect");
    }, 10);
    return () => {
      console.log("clearing the useEffect");
      clearTimeout(timer);
    };
  }, []);
  return (
    <div className="bg-gray-500 p-2">
      <div>
        <p className="text-center">UseEffect Hook Practice</p>
      </div>
      <div>
        <p>Count: {count}</p>
        <button
          onClick={handleClick}
          className="bg-green-400 p-2 rounded-md text-xs cursor-pointer"
        >
          Increment
        </button>
      </div>
    </div>
  );
};

export default UseEffectHook;
