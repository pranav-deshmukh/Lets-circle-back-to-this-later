import CompareProductSearch from "@/components/CompareProductSearch";
import Comparision from "@/components/Comparison";
import Footer from "@/components/Footer";
import ReviewPageNavigation from "@/components/ReviewPageNav";


function Compare() {
    return ( 
        <div className="bg-[#ffffff]">
            <ReviewPageNavigation/>
            <CompareProductSearch/>
            <Comparision/>
            <Footer/>
        </div>
     );
}

export default Compare;