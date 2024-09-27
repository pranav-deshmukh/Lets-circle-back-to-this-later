import ReviewParams from "./ReviewParams";

const arr = ["", "", "", "", "", "", "", "", "", "", ""];

function FinalReview() {
  return (
    <div className="w-full h-full min-h-[300px] md:grid items-center justify-center grid-cols-2 place-items-center gap-y-10 gap-x-4 md:p-10 flex flex-col">
      {arr.map((idx) => {
        return <ReviewParams key={idx} />;
      })}
    </div>
  );
}

export default FinalReview;
