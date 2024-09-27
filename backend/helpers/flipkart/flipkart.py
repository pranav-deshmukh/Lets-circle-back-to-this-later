import requests
from bs4 import BeautifulSoup

url = r"https://www.flipkart.com/boat-wave-fury-1-83-hd-display-bluetooth-calling-functional-crown-smartwatch/p/itma0f5091a1aa94?pid=SMWGQHN4RWUTXYMY&lid=LSTSMWGQHN4RWUTXYMYK9SSX1&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_7&otracker=browse&fm=organic&iid=cb054fd7-ca04-4d49-b080-f830ce0b1d27.SMWGQHN4RWUTXYMY.SEARCH&ppt=browse&ppn=browse&ssid=h6hzf9trds0000001727430890688"

def get_flipkart_info(url):
    """
    output: object{id:string, title:string, body:string, verified:bool} 
    id->[initial name of website][review no.] eg r1, r2, r3
    """
    custom_header = {
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
        'Accept-Language' : 'en-US,en;q=0.9'
    }
    print("request sent")
    response = requests.get(url, headers=custom_header)
    print("status: ", response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.select_one("div#container")
    print(container)
    # all_reviews = container.contains[0].contains[2].contains[0].contains[1].contains[7].contains[5].contains[0].contains[3]
    # print(all_reviews.text)
    # final_output = []
    # for i in range(len(all_reviews)):
    #     review = all_reviews[i]
    #     review_body = review.contents[0].contents
    #     verified = None
    #     if "Certified" in review_body[0].text:
    #         verified = True
    #     else:
    #         verified = False
    #     output = {"id":f"r{i+1}", "title":review_body[1].text, "body":review_body[3].text, "verified":verified}
    #     final_output.append(output)
    # return final_output
    


if __name__ == '__main__':
    print(get_flipkart_info(url))