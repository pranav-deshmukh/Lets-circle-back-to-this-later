"use client"

import { useState } from "react"; 
import { usePathname, useRouter } from "next/navigation"; 
import { Input } from "./ui/input"; 
import { Button } from "./ui/button";

function CompareProductSearch({ setUrl }) {  
  const [url1, setUrl1] = useState(""); 
  const [url2, setUrl2] = useState(""); 
  const pathname = usePathname();
  const router = useRouter(); 

  
  
  function handleClickReview() {
    if (url1) {
      localStorage.setItem("url1",url1);
      setUrl(url1);

      router.push(`/review/prod1`); 
    }
  }

  function handleClickCompare() {
    if (url2) {
      localStorage.setItem("url2",url2)
      router.push(`/compare/prod1/prod2`); 
    }
  }

  return (
    <div className="w-full md:h-[250px] h-[500px] flex md:flex-row flex-col md:items-end items-center justify-evenly gap-10 border-b-[2px] border-black bg-[#cfd6e9]">
      <div className="md:pb-6">
        <label htmlFor="Search Product" className="md:text-2xl">
          Search a New Product
        </label>
        <Input
          className="w-[280px] h-[40px] bg-white border-2 border-black rounded-full mt-4"
          placeholder="Search Product..."
          value={url1} 
          onChange={(e) => setUrl1(e.target.value)} 
        />
        <div className="flex justify-center">
          <Button 
            onClick={handleClickReview} 
            className="mt-4 bg-black text-white px-4 py-2 rounded-full"
          >
            Search
          </Button>
        </div>
      </div>

      <div className="h-full hidden md:flex border-black border-l-[2px]"></div>

      <div className="md:pb-6">
        <label htmlFor="Search Product" className="md:text-2xl">
          Add a product to compare
        </label>
        <Input
          className="w-[280px] h-[40px] bg-white border-2 border-black rounded-full mt-4"
          placeholder="Compare Product..."
          value={url2} 
          onChange={(e) => setUrl2(e.target.value)} 
        />
        <div className="flex justify-center">
          <Button 
            onClick={handleClickCompare} 
            className="mt-4 bg-black text-white px-4 py-2 rounded-full"
          >
            Compare
          </Button>
        </div>
      </div>
    </div>
  );
}

export default CompareProductSearch;
