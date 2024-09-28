import About from "@/components/About";
import Footer from "@/components/Footer";
import HomePage from "@/components/HomePage";
import Navigation from "@/components/Navigation";

export default function Home() {
  return (
    <div className="text-white h-screen w-screen overflow-y-auto">
      <Navigation />
      <section id="home">
        <HomePage />
      </section>
      <section id="about">
        <About />
      </section>
      <section id="contact">
        <Footer />
      </section>
    </div>
  );
}
