import { useState } from "react";
import UseCallbackHook from "./hookUseCallback";
import UseContextHook from "./hookUseContext";
import UseEffectHook from "./hookUseEffect";
import UseMemoHook from "./hookUseMemo";
import UseReducerHook from "./hookUseReducer";
import UseRefHook from "./hookUseRef";
import UseStateHook from "./hookUseState";

type hooksArr = {
  id: number;
  value: string;
};

const hooksArray: hooksArr[] = [
  { id: 1, value: "useState" },
  { id: 2, value: "useEffect" },
  { id: 3, value: "useContext" },
  { id: 4, value: "useReducer" },
  { id: 5, value: "useMemo" },
  { id: 6, value: "useCallback" },
  { id: 7, value: "useRef" },
];
const Hooks = () => {
  const [tab, setTab] = useState<number>(0);
  const handleTab = (tabNumber: number) => {
    setTab(tabNumber);
  };

  const renderTabContent = () => {
    switch (tab) {
      case 0:
        return <UseStateHook />;
      case 1:
        return <UseEffectHook />;
      case 2:
        return <UseContextHook />;
      case 3:
        return <UseReducerHook />;
      case 4:
        return <UseMemoHook />;
      case 5:
        return <UseCallbackHook />;
      case 6:
        return <UseRefHook />;
      default:
        return <div className="p-4">Select a hook</div>;
    }
  };

  return (
    <div>
      <h4 className="bg-slate-700 text-white font-semibold p-1 text-center">
        Hooks Practice
      </h4>
      <div className="flex gap-2 bg-gray-600 justify-center overflow-auto">
        {hooksArray.map((hooks, index) => {
          return (
            <p
              key={hooks.id}
              className={`cursor-pointer p-2 text-black
                ${
                  tab === index
                    ? "border-b-3 border-amber-500 text-gray-400"
                    : ""
                }
                `}
              onClick={() => handleTab(index)}
            >
              {hooks.value}
            </p>
          );
        })}
      </div>
      <div className="h-full">{renderTabContent()}</div>
    </div>
  );
};
export default Hooks;
