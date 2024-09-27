"use client";

import { useState } from "react";
import ProsAndCons from "./ProsAndCons";
import ReviewParams from "./ReviewParams";
import { data } from "@/sample/sampledata";

const { pros, cons, ...filteredData } = data;

function FinalReview() {
  const [selectedCard, setSelectedCard] = useState(null);

  const handleCardClick = (title) => {
    setSelectedCard(selectedCard === title ? null : title);
  };

  return (
    <div className="w-full h-full flex flex-col">
      <div className="md:grid items-center justify-center grid-cols-2 place-items-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
        {Object.entries(filteredData).map(([key, value]) => (
          <div
            key={key}
            onClick={() => handleCardClick(key)}
            className={`p-4 bg-[#F5F5DC] overflow-y-auto rounded-xl ${
              selectedCard === key ? "border-2 border-[#090330] " : ""
            }${value == "None" ? "hidden" : "flex"}`}
          >
            <ReviewParams title={key} value={value} />
          </div>
        ))}
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

export default FinalReview;
