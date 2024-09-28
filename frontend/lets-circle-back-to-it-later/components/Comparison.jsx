"use client";
import { data } from "@/sample/sampledata";
import { useState, useEffect } from "react";
import ReviewParams from "./ReviewParams";
import { usePathname } from "next/navigation";
import ProsAndCons from "./ProsAndCons";

const { pros, cons, ...filteredData } = data;

function Comparision() {
  const [selectedCard, setSelectedCard] = useState(null);
  const [isSmallScreen, setIsSmallScreen] = useState(false);
  const pathname = usePathname();
  const arr = pathname.split("/");

  // Check if the screen is smaller than md (768px)
  useEffect(() => {
    const handleResize = () => {
      setIsSmallScreen(window.innerWidth < 768); // Tailwind's md breakpoint is 768px
    };

    handleResize(); // Check on component mount
    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  const handleCardClick = (title) => {
    setSelectedCard(selectedCard === title ? null : title);
  };

  return (
    <div className="flex flex-col justify-center">
      <div className="flex md:flex-row flex-col justify-center">
        <div className="md:w-[40%]">
          <p className=" mt-4 text-lg font-bold">Product 1:{arr[2]}</p>
          <div className="items-center justify-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
            {Object.entries(filteredData).map(([key, value]) => (
              <div
                key={key}
                onClick={() => handleCardClick(key)}
                className={`p-4 bg-[#F5F5DC] overflow-y-auto rounded-xl ${
                  selectedCard === key ? "border-2 border-[#090330] " : ""
                }${value == "None" ? "hidden" : "flex"}`}
              >
                {/* Conditionally pass the title if the screen is smaller than md */}
                <ReviewParams
                  value={value}
                  title={isSmallScreen ? key : undefined}
                />
              </div>
            ))}
          </div>
        </div>

        {/* For medium and larger screens (md breakpoint) */}
        <div className=" md:flex hidden flex-col justify-evenly">
          {Object.entries(filteredData).map(([key, value]) => (
            <div
              key={key}
              onClick={() => handleCardClick(key)}
              className={`p-4 bg-[#8492eb] text-white text-center overflow-y-auto rounded-xl ${
                selectedCard === key ? "border-2 border-[#090330] " : ""
              }${value == "None" ? "hidden" : "flex"}`}
            >
              {key}
            </div>
          ))}
        </div>

        <div className="md:w-[40%]">
          <p className=" mt-4 text-lg font-bold">Product 2:{arr[3]}</p>
          <div className="items-center justify-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
            {Object.entries(filteredData).map(([key, value]) => (
              <div
                key={key}
                onClick={() => handleCardClick(key)}
                className={`p-4 bg-[#F5F5DC] overflow-y-auto rounded-xl ${
                  selectedCard === key ? "border-2 border-[#090330] " : ""
                }${value == "None" ? "hidden" : "flex"}`}
              >
                {/* Conditionally pass the title if the screen is smaller than md */}
                <ReviewParams
                  value={value}
                  title={isSmallScreen ? key : undefined}
                />
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="flex md:flex-row flex-col justify-center items-center mt-6  mb-10">
        <div className="w-[400px] bg-[#F5F5DC] p-2">
          <p className="text-2xl font-semibold">Pros</p>
          {pros.map((pro, idx) => (
            <ProsAndCons key={idx} title={`Pro ${idx + 1}`} value={pro} />
          ))}
        </div>

        <div className="flex md:border-l-[2px] border-b-[2px] border-black md:h-[300px]"></div>

        <div className="w-[400px] p-2 bg-[#F5F5DC] md:ml-4">
          <p className="text-2xl font-semibold">Cons</p>
          {cons.map((con, idx) => (
            <ProsAndCons key={idx} title={`Con ${idx + 1}`} value={con} />
          ))}
        </div>
      </div>
      <div className="flex md:flex-row flex-col justify-center items-center mt-6  mb-10">
        <div className="w-[400px] bg-[#F5F5DC] p-2">
          <p className="text-2xl font-semibold">Pros</p>
          {pros.map((pro, idx) => (
            <ProsAndCons key={idx} title={`Pro ${idx + 1}`} value={pro} />
          ))}
        </div>

        <div className="flex md:border-l-[2px] border-b-[2px] border-black md:h-[300px]"></div>

        <div className="w-[400px] p-2 bg-[#F5F5DC] md:ml-4">
          <p className="text-2xl font-semibold">Cons</p>
          {cons.map((con, idx) => (
            <ProsAndCons key={idx} title={`Con ${idx + 1}`} value={con} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Comparision;
