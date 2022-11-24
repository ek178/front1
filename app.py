from flask import Flask
import jinja_partials
from views import home

api = Flask(__name__)
api.register_blueprint(home.blueprint)
jinja_partials.register_extensions(api)



#@api.route('/')
#def index():
#    return render_template ("templates/index.html")
 
#@api.route('/data1')
#def name():
#    return render_template ("data1.html")

#@api.route('/data2')
#def age():
#    return render_template ("data2.html")


if __name__ == '__main__':
    api.run(debug=True,port=5000)

