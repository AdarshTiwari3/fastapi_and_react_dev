import { useState } from "react";

const UseStateHook = () => {
  const [count, setCount] = useState<number>(0);
  const handleClick = () => {
    setCount((prev) => prev + 1);
  };
  return (
    <div className="bg-gray-500 p-2">
      <div>
        <p className="text-center">UseState Hook Practice</p>
      </div>
      <div>
        <p>Count: {count}</p>
        <button
          onClick={handleClick}
          className="bg-green-400 p-2 rounded-md text-xs cursor-pointer"
        >
          Click me
        </button>
      </div>
    </div>
  );
};

export default UseStateHook;
