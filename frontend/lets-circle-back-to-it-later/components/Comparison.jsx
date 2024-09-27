"use client";
import { data } from "@/sample/sampledata";
import { useState } from "react";
import ReviewParams from "./ReviewParams";

const { pros, cons, ...filteredData } = data;

function Comparision() {
  const [selectedCard, setSelectedCard] = useState(null);

  const handleCardClick = (title) => {
    setSelectedCard(selectedCard === title ? null : title);
  };
  return (
    <div className="flex justify-center">
      <div className="w-[40%]">
        <div className="items-center justify-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
          {Object.entries(filteredData).map(([key, value]) => (
            <div
              key={key}
              onClick={() => handleCardClick(key)}
              className={`p-4 bg-[#F5F5DC] overflow-y-auto rounded-xl ${
                selectedCard === key ? "border-2 border-[#090330] " : ""
              }${value == "None" ? "hidden" : "flex"}`}
            >
              <ReviewParams value={value} />
            </div>
          ))}
        </div>
      </div>
      <div className="flex flex-col justify-evenly">
        {Object.entries(filteredData).map(([key, value]) => (
            <div
              key={key}
              onClick={() => handleCardClick(key)}
              className={`p-4 bg-[#9086ea] text-white text-center overflow-y-auto rounded-xl ${
                selectedCard === key ? "border-2 border-[#090330] " : ""
              }${value == "None" ? "hidden" : "flex"}`}
            >
              {key}
            </div>
          ))}
      </div>
      <div className="w-[40%]">
        <div className="items-center justify-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
          {Object.entries(filteredData).map(([key, value]) => (
            <div
              key={key}
              onClick={() => handleCardClick(key)}
              className={`p-4 bg-[#F5F5DC] overflow-y-auto rounded-xl ${
                selectedCard === key ? "border-2 border-[#090330] " : ""
              }${value == "None" ? "hidden" : "flex"}`}
            >
              <ReviewParams value={value} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Comparision;
