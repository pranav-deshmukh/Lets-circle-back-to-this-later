from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


app.route('/info',method = ['get'])
def scrape(url):
    #get the product name from the url
    
    print('hi')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)