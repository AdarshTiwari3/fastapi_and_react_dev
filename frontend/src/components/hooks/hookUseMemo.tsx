import { useMemo, useState, type ChangeEvent } from "react";

const UseMemoHook = () => {
  const [input, setInput] = useState<string>("");
  const [count, setCount] = useState<number>(0);
  const inputHandler = (e: ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
  };

  const calculateExpensive = useMemo(() => {
    let result = 0;
    for (let index = 0; index < 1000000; index++) {
      result += index; // heavy work
    }
    console.log("expensive completed");
    return result;
  }, []);

  const handleClick = () => {
    setCount((prev) => prev + 1);
  };

  return (
    <div className="bg-gray-500 h-full p-4 ">
      <div>
        <p className="text-center">UseMemo Hook Practice</p>
      </div>
      <div className="pt-2 flex justify-center">
        <input
          value={input}
          type="search"
          className="bg-amber-50 rounded-l-lg"
          onChange={inputHandler}
        />
        <button className="bg-green-400 px-2 rounded-r-lg">Search</button>
      </div>
      <div className="mt-2 ">
        <p className="text-center">count: {count}</p>
        <p className="text-center">expensive result: {calculateExpensive}</p>
        <div className="flex justify-center pt-2">
          <button
            className="bg-green-400 p-2 rounded-md text-xs cursor-pointer"
            onClick={handleClick}
          >
            Click Me
          </button>
        </div>
      </div>
    </div>
  );
};

export default UseMemoHook;
