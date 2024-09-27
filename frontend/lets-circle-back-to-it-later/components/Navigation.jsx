function Navigation() {
  return (
    <div className="w-full h-[60px] bg-[#F5F5DC] flex items-center text-lg font-semibold text-black fixed">
      <div className="w-[10%] ml-4">
        <span className="md:flex hidden">Reviews.com</span>
      </div>
      <div className="w-[70%] flex justify-center gap-20">
        <span>Home</span>
        <span>About</span>
        <span>Contact</span>
      </div>
    </div>
  );
}

export default Navigation;
