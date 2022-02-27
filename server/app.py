from flask import Flask, request, jsonify, after_this_request
import random

app = Flask(__name__)

@app.route("/rand", methods=['GET'])
def hello():
    @ after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    return str(random.randint(0, 100))




@app.route("/sales/by-sku", methods=['GET'])
def SalesBySku():
    @ after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    
    import dummy
    
    return jsonify(dummy.sales_by_sku_list)


if __name__ == "__main__":
    app.run(host="localhost",debug=True, port=5555)