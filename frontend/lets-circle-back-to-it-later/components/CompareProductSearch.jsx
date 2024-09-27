import { Input } from "./ui/input";

function CompareProductSearch() {
  return (
    <div className="w-full md:h-[200px] h-[430px] flex md:flex-row flex-col md:items-end items-center justify-evenly gap-10 border-b-[1px] border-black">
      <div className="md:pb-3">
        <label htmlFor="Search Product" className="text-2xl">Search a New Product</label>
        <Input
          className="w-[320px] h-[40px] bg-white border-2 border-black rounded-full mt-4"
          placeholder="Search Product..."
        />
      </div>
      <div className="h-full hidden md:flex border-black border-l-[1px]"></div>
      <div className="md:pb-3">
        <label htmlFor="Search Product" className="text-2xl">Add a product to compare</label>
        <Input
          className="w-[300px] h-[40px] bg-white border-2 border-black rounded-full mt-4"
          placeholder="Compare Product..."
        />
      </div>
    </div>
  );
}

export default CompareProductSearch;
