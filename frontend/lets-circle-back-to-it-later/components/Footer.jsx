import { IoLocation } from "react-icons/io5";
import { IoCall } from "react-icons/io5";
import { IoMail } from "react-icons/io5";
import { FaInstagram } from "react-icons/fa";
import { FaLinkedin } from "react-icons/fa";
import { FaSquareXTwitter } from "react-icons/fa6";
import { FaTelegramPlane } from "react-icons/fa";
import { IoLogoWhatsapp } from "react-icons/io";

function Footer() {
  return (
    <div className="w-full h-[100px] bg-[#F5F5DC] min-h-[100px] flex flex-col justify-between text-black px-1">
        <section className="md:text-lg font-bold h-[20px] pt-1 px-2">
          Contact Information
        </section>
      <div className="flex items-center justify-between">
        <section className="h-[80px] flex items-center md:text-[12px] text-[8px] md:gap-14 font-semibold ml-2">
          <span className="flex justify-center items-center gap-1">
            <IoLocation className="md:text-lg text-sm" />
            360 king Street
            <br />
            Feastervile Trevose, PA 19053
          </span>
          <span className="flex justify-center items-center gap-1">
            <IoCall className="md:text-lg text-sm" />
            +234 8152 586 5869
            <br />
            +234 8185 958 6359
          </span>
          <span className="flex justify-center items-center gap-1">
            <IoMail className="md:text-lg text-sm" />
            support.reviews.com@gmail.com
          </span>
        </section>
      <div className="flex md:text-xl text-[10px] md:gap-4 gap-1">
        <span><FaInstagram/></span>
        <span><FaLinkedin/></span>
        <span><FaSquareXTwitter/></span>
        <span><FaTelegramPlane/></span>
        <span><IoLogoWhatsapp/></span>
      </div>
      </div>
    </div>
  );
}

export default Footer;
