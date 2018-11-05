from flask import Flask,render_template
from flask import jsonify,request
from heba import Model
clf = Model()

app = Flask(__name__)

@app.route("/train",methods=['GET','POST'])
def train():
	clf.read_df("C:\\Users\\hebaa\\Desktop\\NTI\\Ass #3\\DatafinitiElectronicsProductData.csv")
	#return clf.df.head().to_json()
	clf.split_df()
	clf.train_test(0.25)
	model_name = request.args.get('moddel')
	m= clf.train(model_name)
	clf.pretty_ev()
	return 'The Model Is '+(str(m))


@app.route("/train_page")
def train_page():
    return "<form method = 'GET' action ='http://127.0.0.1:9090/train'>\
    <h2>Algorizm:</h2>\
    </br>\
    <select name='moddel'>\
		<option value='LogisticRegression'>LogisticRegression</option>\
		<option value='KNeighborsClassifier'>KNeighborsClassifier</option>\
		<option value='GaussianNB'>GaussianNB</option>\
		<option value='SVC'>SVC</option>\
		<option value='DecisionTreeClassifier'>DecisionTreeClassifier</option>\
		<option value='RandomForestClassifier'>RandomForestClassifier</option>\
    </select>\
  </br></br>\
  <input type='submit' value='train'>\
  </form>"

@app.route("/predict_page",methods=['GET','POST'])
def predict_page():
	return "<form method='GET' action='http://127.0.0.1:9090/predict'>\
            <h1> data input: </h1>\
            <p>brand</p>\
            </tr><select name='brand'>\
            <option>Logitech</option>\
            <option>Microsoft</option>\
            <option>JBL</option>\
            <option>Sling Media</option>\
            <option>Sony</option>\
            <option>Sdi Technologies, Inc.</option>\
            <option>Lowepro</option>\
            <option>Glengery</option>\
            <option>Yamaha</option>\
            <option>Definitive Technology</option>\
            <option>Siriusxm</option>\
            <option>Samsung</option>\
            <option>Boytone</option>\
            <option>Midland</option>\
            <option>Motorola</option>\
            <option>CLARITY-TELECOM</option>\
            <option>House of Marley</option>\
            </select>\
            </br>\
            <p>colors</p>\
            <select name='colors: '>\
            <option>Black</option>\
            <option>Black,White</option>\
            <option>Red,Pink,Yellow,Blue,Bordeaux Pink,Cinnabar Red,Black,Viridian Blue,Charcoal Black</option>\
            <option>Multicolor,Black,Grey</option>\
            <option>Multicolor</option>\
            <option>Grey</option>\
            <option>White</option>\
            <option>Siriusxm Sxezr1h1 Xm,Siriusxm Sxezr1v1 Xm</option>\
            <option>Gray,Color</option>\
            <option>Navy,Black,Gray,Blue</option>\
            </select>\
            </br>\
            <p>manufacturer</p>\
			<select name='manufacturer: '>\
            <option>Logitech</option>\
            <option>Microsoft</option>\
            <option>JBL</option>\
            <option>Slingbox</option>\
            <option>Sony</option>\
            <option>iHome</option>\
            <option>Lowepro</option>\
            <option>Glengery</option>\
            <option>5 Years</option>\
            <option>Siriusxm</option>\
            <option>YAMAHA</option>\
            <option>SAMSUNG</option>\
            <option>Boytone</option>\
            <option>Midland</option>\
            <option>Motorola</option>\
            <option>Midland</option>\
            <option>Yamaha</option>\
            <option>Allround Software</option>\
            <option>House of Marley</option>\
            </select>\
            </br>\
            <br><input type='submit' value='predict'></br>\
            </form>\
    "

@app.route("/predict",methods=['GET','POST'])
def predict():
    brand = request.args.get('brand')
    colors = request.args.get('colors')
    manufacturer = request.args.get('manufacturer')
    rat = clf.predict(brand=brand,colors=colors,manufacturer=manufacturer)
    return "<h1> The Prediction :- </h1>\
            <h2> reviews.rating = "+str(rat)+" $</h2>"



if __name__ == '__main__':
	try:
		app.run(port='9090',host='0.0.0.0')
	except Exception as e:
		print("Error")