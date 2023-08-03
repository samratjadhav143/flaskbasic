from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/mathwithpostman',methods=['POST'])
def calculateofpostman():
    # print(str(request.json))
    ops = request.json["operation"]
    num1 = int(request.json["num1"])
    num2 = int(request.json["num2"])
    if ops == "add":
        result = num1 + num2
        responce=f"sum of {num1} + {num2} is {result}"
    

    elif ops == "subtract":
        result = num1 - num2
        responce=f"subtraction of {num1} + {num2} is {result}"
    

    elif ops == "multiply":
        result = num1 * num2
        responce=f"multiplication of {num1} * {num2} is {result}"
    

    elif ops == "divide":
        result = num1 / num2
        responce=f"dividetion of {num1} / {num2} is {result}"
    
    else:
        responce =f"{ops} is either not arithmetic or its not supported" 
    return jsonify(responce)

if __name__=="__main__":
    app.run(host="0.0.0.0")

# @app.route('/math',methods=['POST'])
# def math_ops():
#     if(request.method == 'POST'):
#         ops = request.form['operation']
#         num1 = int(request.form['num1'])
#         num2 = int(request.form['num2'])
#         if ops == 'add':
#             r = num1+num2
#             result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'subtract':
#             r = num1-num2
#             result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'multiply':
#             r = num1*num2
#             result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'divide':
#             r = num1/num2
#             result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
#         return render_template('results.html' , result = result)




# @app.route('/postman_action',methods=['POST'])
# def math_ops1():
#     if(request.method == 'POST'):
#         ops = request.json['operation']
#         num1 = int(request.json['num1'])
#         num2 = int(request.json['num2'])
#         if ops == 'add':
#             r = num1+num2
#             result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'subtract':
#             r = num1-num2
#             result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'multiply':
#             r = num1*num2
#             result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
#         if ops == 'divide':
#             r = num1/num2
#             result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
#         return jsonify(result)

#  if __name__=="__main__":
#      app.run(host="0.0.0.0")
