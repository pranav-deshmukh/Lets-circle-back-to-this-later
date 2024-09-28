"use client";

import { useState, useEffect } from "react";
import ProsAndCons from "./ProsAndCons";
import ReviewParams from "./ReviewParams";
import { data } from "@/sample/sampledata";
import axios from "axios";

const { pros, cons, ...filteredData } = data;

function FinalReview() {
  const [selectedCard, setSelectedCard] = useState(null);

  const handleCardClick = (title) => {
    setSelectedCard(selectedCard === title ? null : title);
  };

  useEffect(() => {
    // Retrieve url1 and url2 from localStorage
    const url1 = localStorage.getItem("url1");
    const url2 = localStorage.getItem("url2");

    // Post request with url1 and url2 from localStorage
    if (url1 && url2) {
      axios
        .post('/api/your-endpoint', {
          url1: url1,
          url2: url2,
        })
        .then((response) => {
          console.log(response.data); // Handle the response data
        })
        .catch((error) => {
          console.error(error); // Handle the error
        });
    }
  }, []); // Empty dependency array ensures this effect runs once on component mount

  return (
    <div className="w-full h-full flex flex-col">
      <div className="md:grid items-center justify-center grid-cols-2 place-items-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
        {Object.entries(filteredData).map(([key, value]) => (
          <div
            key={key}
            onClick={() => handleCardClick(key)}
            className={`p-4 bg-[#F5F5DC] overflow-y-auto rounded-xl ${
              selectedCard === key ? "border-2 border-[#090330]" : ""
            } ${value === "None" ? "hidden" : "flex"}`}
          >
            <ReviewParams title={key} value={value} />
          </div>
        ))}
      </div>

      <div className="flex md:flex-row flex-col justify-center items-center mt-6 mb-10">
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
