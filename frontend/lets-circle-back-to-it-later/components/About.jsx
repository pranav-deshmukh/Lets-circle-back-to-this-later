import { Kay_Pho_Du } from "next/font/google";

const Kay = Kay_Pho_Du({
  weight: "400",
  subsets: ["latin"],
});
function About() {
    return ( 
        <div className={`w-full h-[800px] min-h-[300px] flex items-center justify-center flex-col gap-10 ${Kay.className}`}>
            <div className="md:text-6xl text-4xl font-semibold">
                <span>About Us</span>
            </div>
            <div className="max-w-[800px] min-w-[100px] p-4 md:text-xl">
                <span>Discover the ultimate solution for streamlined product review analysis. Our platform scours the web to gather comprehensive feedback, ensuring you get a clear, unbiased overview of any product. With a focus on delivering accurate insights, we help you make informed decisions quickly and easily, saving you the hassle of sifting through countless reviews.</span>
            </div>
            <div className="max-w-[800px] min-w-[300px] p-4 md:text-xl">
                Designed for convenience and efficiency, our service brings together reviews from trusted sources in one place. Whether you're shopping for gadgets, appliances, or anything in between, we simplify the process so you can focus on finding the best product for your needs.
            </div>
        </div>
     );
}

export default About;