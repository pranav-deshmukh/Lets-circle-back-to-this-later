import Image from "next/image";

function ReviewParams({ title, value }) {
  return (
    <div
      className={`w-full max-w-[650px] md:h-[250px] p-4 bg-[#F5F5DC] overflow-y-auto ${
        value == "None" ? "hidden" : "flex flex-col"
      }`}
    >
      <div className="flex justify-end">
        <Image src={"/SampleImg.png"} height={150} width={150} alt="sample" />
      </div>
      <span className="font-bold text-lg mb-2">{title}</span>
      <span>{value}</span>
    </div>
  );
}

export default ReviewParams;
