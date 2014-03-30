from flask import *
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', page_title='First Page')

app.debug = True
if __name__ == '__main__' :
	app.run()

			

