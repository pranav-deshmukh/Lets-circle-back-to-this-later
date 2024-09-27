import About from "@/components/About";
import HomePage from "@/components/HomePage";
import Navigation from "@/components/Navigation";

export default function Home() {
  return (
    <div className="text-white h-screen w-screen  overflow-y-auto">
      <Navigation />
      <HomePage />
      <About />
    </div>
  );
}
