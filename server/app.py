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
    
    """
    # Return a list of Order Items, within date range, merged Alias onto SKU
    expected_result = {
        [ 
            {"sku": "636836014104",
            "name": "REAL SIC Hop Flower Enamel Pin - Premium Craft Brewery, Beer Lover Lapel Pin for Jackets, Backpacks, Bags, Hats & Tops",
            "sales": 386.2,
            "qty": 22,
            "img": 'https://m.media-amazon.com/images/I/416tSWX3TsL.jpg',
            },
            {"next":"item"},

        ]
    }
    """

    import dummy
    return jsonify(dummy.sales_by_sku_list)


@app.route("/sales/by-order", methods=['GET'])
def SalesByOrder():
    @ after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    """
        # Return a list of Orders, within date range, including days in-between
        # Sum sales, shipping 
        # Discounts handled (concatinated, made negative) on ingest
        # Qty_in_order handled on ingest
        # Transfer to FBA (boolean) handled on ingest
        # Function should return defaults, but also be able to request specific data
        # burn = total_qty/days

    
    expected_result = {
        "total_sales":50897,
        "shipping":2356,
        "discounts": -924,
        "total_qty": 1146,
        "burn": 38.2,
        "days_in_range" [ "Nov 01", "Nov 02","Nov 03","Nov 04"],
        "sales_by_day": [1046.68,1391.59,1541.81,1400.66],
        "qty_by_day": [list],
        "transfer_by_day": [list],
    }

    """


    import dummy

    result = {
        "total_sales":sum(dummy.sales_by_day),
        "shipping":2356,
        "discounts": -924,
        "total_qty": sum(dummy.qty_by_day),
        "burn": 38.2,
        "days_in_range": dummy.days_in_range,
        "sales_by_day": dummy.sales_by_day,
        "qty_by_day": dummy.qty_by_day,
        "transfer_by_day": dummy.transfer_by_day,
    }    
    
    return jsonify(result)


@app.route("/orders", methods=['GET'])
def GetOrders():
    @ after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    """
        # Return a list of Orders, within date range
        # Also provide method to Get a single order by id
    """
    import dummy

    return jsonify(dummy.orders)

@app.route("/orders/by-day", methods=['GET'])
def GetOrdersByDay():
    @ after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    """
        # Return chart data - list of days in range as labels
        # and count of orders per day
    """

    import dummy

    result = {
        'labels': dummy.orders_lables,
        'data': dummy.orders_by_day
    }

    return jsonify(result)



@app.route("/customers", methods=['GET'])
def GetCustomers():
    @ after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    """
        # Return table data - list of customers and summed order value
        # Number of orders and "customer value"
    """

    import dummy

if __name__ == "__main__":
    app.run(host="localhost",debug=True, port=5555)