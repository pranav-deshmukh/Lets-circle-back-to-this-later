import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { FaPlus } from "react-icons/fa";

function HomePage() {
  return (
    <div className="w-full h-[800px] min-h-[300px] flex items-center justify-center flex-col gap-10 ">
      <section className="text-4xl text-center p-4">
        <span>
          Complete product
          <br /> review analysis,
          <br /> simplified
        </span>
      </section>
      <section className="flex md:flex-row flex-col items-center max-w-[800px] min-w-[200px] justify-center gap-3">
        <Input
          className="bg-white text-black min-w-[300px] h-[43px] rounded-xl"
          placeholder="Enter Url"
        />
        <section className="flex gap-2">
          <span className="bg-[#F5F5DC] p-3 rounded-full">
            <FaPlus className=" text-black" />
          </span>
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
