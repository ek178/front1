from flask import Flask,render_template


api = Flask(__name__)
 
@api.route('/')
def hello():
    return render_template ("index.html")

@api.route('/data1.html')
def name():
    return render_template ("data1.html")

@api.route('/data2.html')
def age():
    return render_template ("data2.html")


if __name__ == '__main__':
    api.run(debug=True,port=5000)

