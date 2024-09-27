import { Input } from "./ui/input";

function HomePage() {
    return ( 
        <div className="w-full max-h-[600px] min-h-[600px] flex items-center justify-center flex-col gap-10">
            <section className="text-4xl text-center p-4">
                <span>Complete product<br/> review analysis,<br/> simplified</span>
            </section>
            <section>
                <Input className="bg-white text-black w-[400px] h-[43px] rounded-xl" placeholder="Enter Url"/>
            </section>
        </div>
     );
}

export default HomePage;