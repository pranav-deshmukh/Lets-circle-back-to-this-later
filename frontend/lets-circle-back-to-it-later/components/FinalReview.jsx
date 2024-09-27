import Footer from "./Footer";
import ProsAndCons from "./ProsAndCons";
import ReviewParams from "./ReviewParams";
import { data } from "@/sample/sampledata";

const { pros, cons, ...filteredData } = data;

function FinalReview() {
  return (
    <div className="w-full h-full flex flex-col">
      <div className="md:grid items-center justify-center grid-cols-2 place-items-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
        {Object.entries(filteredData).map(([key, value], idx) => {
          return <ReviewParams key={idx} title={key} value={value} />;
        })}
      </div>
      <div className="flex justify-evenly items-center">
        <div className="">
            <p>Pros</p>
          {Object.entries(pros).map(([key, value], idx) => {
            return <ProsAndCons key={idx} title={key} value={value} />;
          })}
        </div>
        <div className="border-l-[2px] border-black h-[300px]"></div>
        <div className="pb-10">
            <p>Cons</p>
          {Object.entries(cons).map(([key, value], idx) => {
            return <ProsAndCons key={idx} title={key} value={value} />;
          })}
        </div>
      </div>
      <Footer/>
    </div>
  );
}

export default FinalReview;
