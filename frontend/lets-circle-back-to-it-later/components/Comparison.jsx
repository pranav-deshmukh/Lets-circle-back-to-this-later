"use client";
import { data } from "@/sample/sampledata";
import { useState, useEffect } from "react";
import ReviewParams from "./ReviewParams";

const { pros, cons, ...filteredData } = data;

function Comparision() {
  const [selectedCard, setSelectedCard] = useState(null);
  const [isSmallScreen, setIsSmallScreen] = useState(false);

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
    <div className="flex md:flex-row flex-col justify-center">
      <div className="md:w-[40%]">
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
              <ReviewParams value={value} title={isSmallScreen ? key : undefined} />
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
              <ReviewParams value={value} title={isSmallScreen ? key : undefined} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Comparision;
