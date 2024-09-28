
import CompareProductSearch from "@/components/CompareProductSearch";
import FinalReview from "@/components/FinalReview";
import Footer from "@/components/Footer";
import ReviewPageNavigation from "@/components/ReviewPageNav";

function ReviewPage() {
  
  return (
    <div className="bg-[#ffffff]">
      <ReviewPageNavigation />
      <CompareProductSearch/>
      <FinalReview/>
      <Footer/>
    </div>
  );
}

export default ReviewPage;
