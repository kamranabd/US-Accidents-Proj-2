# import dependencies
from flask import Flask, jsonify, render_template, redirect, request
from accidentsdata import read_accidents, read_accidents_severity,\
read_accidents_severity,read_accidents_state, read_accidents_zipcode,read_accidents_all


app = Flask(__name__)

#Define flask routes 

@app.route('/')  ##route to render index.html in heroku
def index():
    # return "<h3>Welcome to Team 8 Project 2 Server!!</h3>"
    return render_template("index.html")
 

@app.route('/api/info')  #all available APIs
def available_apis():
    return render_template("api_page.html")
 
@app.route('/barchart')
def get_barchart():
    # if request.method == "POST":
    #     return redirect("/", code=302)
    # return redirect("state-chart.html")
    # return redirect("/state-chart.html")
    return render_template("bar.html")

@app.route('/piechart')
def get_pie():
    return render_template("pie.html")

@app.route('/data')
def get_data():
    return render_template("table.html")

@app.route('/api/allaccidents') #not a good idea to call the all accidents api, 540K documents 
def get_all_ccidents():
    accidents = read_accidents_all()
    return jsonify(accidents)

@app.route('/api/accidents') # return all accidents, but limited to 5000k documents 
def get_accidents():
    accidents = read_accidents()
    return jsonify(accidents)


@app.route('/api/accidents/<min_severity>') #return accidents severity on a scale of 1-4
def get_accidents_severity(min_severity):
    accidents = read_accidents_severity(min_severity)
    return jsonify(accidents)


@app.route('/api/states/<state>') #filter to specific state 
def get_accidents_state(state):
    accidents = read_accidents_state(state)
    return jsonify(accidents)


@app.route('/api/zipcode/<zipcode>') #filter to specific zipcode 
def get_accidents_zipcode(zipcode):
    accidents = read_accidents_zipcode(zipcode)
    return jsonify(accidents)


if __name__ == '__main__':
    app.run(debug=True)
    # print(read_accidents())
    # print(read_accidents_severity(2))
