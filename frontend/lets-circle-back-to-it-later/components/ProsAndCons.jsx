function ProsAndCons({ title, value }) {
  return (
    <div
      className={`w-full max-w-[650px] p-4 items-baseline bg-[#F5F5DC] overflow-y-auto ${
        value == "None" ? "hidden" : "flex"
      }`}
    >
      <p className="font-bold text-lg mb-2">{title}. </p>
      <p>{value}</p>
    </div>
  );
}

export default ProsAndCons;
