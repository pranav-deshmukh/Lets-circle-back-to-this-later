import CompareProductSearch from "@/components/CompareProductSearch";
import FinalReview from "@/components/FinalReview";
import ReviewPageNavigation from "@/components/ReviewPageNav";

function ReviewPage() {
  return (
    <div className="bg-[#efeded]">
      <ReviewPageNavigation />
      <CompareProductSearch/>
      <FinalReview/>
    </div>
  );
}

export default ReviewPage;
