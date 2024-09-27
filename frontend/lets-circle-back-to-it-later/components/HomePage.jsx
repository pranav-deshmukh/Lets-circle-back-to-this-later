import { Input } from "./ui/input";
import { FaPlus } from "react-icons/fa";

function HomePage() {
    return ( 
        <div className="w-full h-[800px] min-h-[300px] flex items-center justify-center flex-col gap-10 ">
            <section className="text-4xl text-center p-4">
                <span>Complete product<br/> review analysis,<br/> simplified</span>
            </section>
            <section className="flex items-center w-[800px] min-w-[200px] justify-center">
                <Input className="bg-white text-black w-[400px] h-[43px] rounded-xl" placeholder="Enter Url"/>
                <span className="bg-[#F5F5DC] ml-4 p-3 rounded-full">

                <FaPlus className=" text-black"/>
                </span>
            </section>
        </div>
     );
}

export default HomePage;