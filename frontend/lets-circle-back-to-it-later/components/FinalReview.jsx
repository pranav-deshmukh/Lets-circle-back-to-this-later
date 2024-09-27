import ReviewParams from "./ReviewParams";
import { data } from "@/sample/sampledata";

const {pros, cons, ...filteredData} = data

function FinalReview() {
  return (
    <div className="w-full h-full min-h-[300px] md:grid items-center justify-center grid-cols-2 place-items-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
      {Object.entries(filteredData).map(([key,value],idx) => {
        return <ReviewParams key={idx} title={key} value={value}/>;
      })}
    </div>
  );
}

export default FinalReview;
