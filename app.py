from flask import Flask,render_template


api = Flask(__name__)
 
@api.route('/')
def hello():
    return render_template ("index.html")

@api.route('/data1.html')
def names():
    return render_template ("data1.html")



if __name__ == '__main__':
    api.run(debug=True,port=5000)

