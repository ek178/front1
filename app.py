from flask import Flask,render_template
from flask import current_app as api
#import jinja_partials

api = Flask(__name__)
#api.register_blueprint(home.blueprint)
#jinja_partials.register_extensions(api)



@api.route('/')
def index():
    return render_template (
        "index.html")
 
@api.route('/data1')
def name():
    return render_template ("data1.html")

@api.route('/data2')
def age():
    return render_template ("data2.html")


if __name__ == '__main__':
    api.run(debug=True,port=5000)

