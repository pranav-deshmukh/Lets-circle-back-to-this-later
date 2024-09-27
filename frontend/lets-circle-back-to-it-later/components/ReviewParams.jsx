function ReviewParams({ title, value }) {
  return (
    <div className="w-full max-w-[650px] md:h-[300px] p-4 bg-[#F5F5DC] overflow-y-auto">
      <div className="font-bold text-lg mb-2">{title}</div>
      <div>{value!="None"?value:"No data available"}</div>
    </div>
  );
}

export default ReviewParams;
