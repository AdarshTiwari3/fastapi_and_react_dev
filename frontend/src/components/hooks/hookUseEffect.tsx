import { useEffect, useState, lazy, Suspense } from "react";

const LazyComponent = lazy(() => import("./lazyLoading"));
const baseURL = import.meta.env.VITE_APP_URL;
const UseEffectHook = () => {
  const [count, setCount] = useState<number>(0);

  //   const mypromise = new Promise<number>((resolve, reject) => {
  //     const num = 9;
  //     if (num > 8) {
  //       resolve(num);
  //     } else {
  //       reject("Number is small");
  //     }
  //   });

  //   mypromise
  //     .then((res) => {
  //       console.log("success=", res);
  //     })
  //     .catch((err) => {
  //       console.log("failed", err);
  //     });
  //   console.log("Start");

  //   setTimeout(() => {
  //     console.log("Step 1");

  //     setTimeout(() => {
  //       console.log("Step 2");

  //       setTimeout(() => {
  //         console.log("Step 3");

  //         setTimeout(() => {
  //           console.log("Step 4: Done!");
  //         }, 1000);
  //       }, 1000);
  //     }, 1000);
  //   }, 1000);

  const handleClick = () => {
    setCount((prev) => prev + 1);
  };
  //   useEffect(() => {
  //     const timer = setTimeout(() => {
  //       console.log("Effect runs");
  //     }, 1000);
  //     return () => {
  //       clearTimeout(timer);
  //       console.log("clearing timeout");
  //     };
  //   }, []);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${baseURL}/auth/update_profile`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: "smith@gmail.com",
            city: "Gurgaon",
            contact: "9766238229",
            state: "Delhi",
          }),
        });
        const data = await response.json();
        console.log("res=", data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
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

      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
    </div>
  );
};

export default UseEffectHook;
