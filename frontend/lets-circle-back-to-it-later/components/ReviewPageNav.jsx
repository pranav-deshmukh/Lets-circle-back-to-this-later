import { Roboto } from "next/font/google";
import { Input } from "./ui/input";

const Robo = Roboto({
  weight: "700",
  subsets: ["latin"],
});

function ReviewPageNavigation() {
  return (
    <div className={`w-full h-[60px] bg-[#F5F5DC] flex items-center text-lg font-semibold text-black fixed ${Robo.className} text-lg text-[#090330]`}>
      <div className="w-[10%] ml-4">
        <span className="md:flex hidden">Reviews.com</span>
      </div>
      <div className="w-[60%] flex justify-center gap-20">
        <span>Home</span>
        <span>About</span>
        <span>Contact</span>
      </div>
      <div className="w-[30%] flex justify-center items-center">

        <Input className="max-w-[300px] h-[40px] bg-white border-2 border-black rounded-full" placeholder="Search Product..."/>
      </div>
    </div>
  );
}

export default ReviewPageNavigation;
