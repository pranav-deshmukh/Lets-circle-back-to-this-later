"use client"
import { Playfair_Display_SC } from "next/font/google";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { FaPlus } from "react-icons/fa";
import { useRouter } from "next/navigation";
import { useState } from "react";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";

const Playfair = Playfair_Display_SC({
  weight: "400",
  subsets: ["latin"],
});

function HomePage() {
  const router = useRouter();
  const [url1, setUrl1] = useState(""); 
  const [url2, setUrl2] = useState(""); 
  const [compare, setCompare] = useState(false); 

  function handleClickReview() {
    if (url1) {
      localStorage.setItem("url1",url1);
      router.push(`review/prod1`); 
    }
  }
  function handleCkickCompare() {
    if (url1&&url2) {
      localStorage.setItem("url1",url1);
      localStorage.setItem("url2",url2);
      router.push(`compare/prod1/prod2`); 
    }
  }

  return (
    <div className="w-full h-[800px] min-h-[300px] flex items-center justify-center flex-col gap-10 ">
      <section
        className={`md:text-6xl text-4xl text-center p-4 ${Playfair.className}`}
      >
        <span>
          Complete product
          <br /> review analysis,
          <br /> simplified
        </span>
      </section>
      <section className="flex md:flex-row flex-col items-center max-w-[800px] min-w-[200px] justify-center gap-3">
        <section>

        <Input
          className="bg-white text-black min-w-[350px] h-[43px] rounded-xl"
          placeholder="Enter Url"
          value={url1}
          onChange={(e) => setUrl1(e.target.value)}
          />
          {
            compare&&(
  
              <Input
                className="bg-white text-black min-w-[350px] h-[43px] rounded-xl mt-2"
                placeholder="Enter Url"
                value={url2}
                onChange={(e) => setUrl2(e.target.value)}
              />
            )
          }
          
        </section>
        <section className="flex gap-2">
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger>
                <p className="bg-[#F5F5DC] p-3 rounded-full" onClick={()=>setCompare((prev)=>!prev)}>
                  <FaPlus className=" text-black" />
                </p>
              </TooltipTrigger>
              <TooltipContent>
                <p>Add another product</p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>

          <span className="">
            <Button
              onClick={compare?handleCkickCompare:handleClickReview} 
              className="bg-[#F5F5DC] text-black font-bold text-[14px] hover:bg-[#cacac9] rounded-2xl"
            >
              {compare?"Compare":"Search"}
            </Button>
          </span>
        </section>
      </section>
    </div>
  );
}

export default HomePage;
