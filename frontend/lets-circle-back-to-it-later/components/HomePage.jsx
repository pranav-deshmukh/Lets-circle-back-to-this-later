import { Playfair_Display_SC } from "next/font/google";

import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { FaPlus } from "react-icons/fa";
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
        <Input
          className="bg-white text-black min-w-[400px] h-[43px] rounded-xl"
          placeholder="Enter Url"
        />
        <section className="flex gap-2">
          <TooltipProvider>
            <Tooltip>
              <TooltipTrigger>
                <p className="bg-[#F5F5DC] p-3 rounded-full">
                  <FaPlus className=" text-black" />
                </p>
              </TooltipTrigger>
              <TooltipContent>
                <p>Add another product</p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>

          <span className="">
            <Button className="bg-[#F5F5DC] text-black font-bold text-[14px] hover:bg-[#cacac9] rounded-2xl">
              Search
            </Button>
          </span>
        </section>
      </section>
    </div>
  );
}

export default HomePage;
