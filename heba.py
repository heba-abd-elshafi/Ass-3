
# coding: utf-8
import pandas as pd
import webbrowser
from sklearn.preprocessing import LabelEncoder,StandardScaler,Imputer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

class Model():
	def __init__(self):
		self.brand_enc = LabelEncoder()
		self.cat_enc = LabelEncoder()
		self.col_enc = LabelEncoder()
		self.man_enc = LabelEncoder()
		

	def read_df(self,path):
		self.df=pd.read_csv(path)
		self.df=self.df[['brand','categories','colors','manufacturer','reviews.rating']]
		self.df=self.df[(self.df['colors'].notnull())&(self.df['manufacturer'].notnull())&(self.df['reviews.rating'].notnull())]
		self.df['brand'] = self.brand_enc.fit_transform(self.df['brand'])
		self.df['categories'] = self.cat_enc.fit_transform(self.df['categories'])
		self.df['colors'] = self.col_enc.fit_transform(self.df['colors'])
		self.df['manufacturer'] = self.man_enc.fit_transform(self.df['manufacturer'])

	def split_df(self):
		self.x=self.df.iloc[:,:-1].values
		self.y=self.df['reviews.rating'].values

	def train_test(self,test_size):
		self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(self.x,self.y,test_size = 0.25,random_state=0)

	def train(self,model_name):
		if model_name == "LogisticRegression":
			self.model = LogisticRegression()
		elif model_name == "KNeighborsClassifier":
			self.model = KNeighborsClassifier(n_neighbors=3)
		elif model_name == "GaussianNB":
			self.model = GaussianNB()
		elif model_name == "SVC":
			self.model = SVC(kernel="rbf")
		elif model_name == "DecisionTreeClassifier":
			self.model = DecisionTreeClassifier()
		elif model_name == "RandomForestClassifier":
			self.model = RandomForestClassifier()
		self.model.fit(self.x_train,self.y_train)
		return self.model

	
	def pretty_ev(self):
		self.y_pre=self.model.predict(self.x_test)
		self.class_rep=classification_report(self.y_test,self.y_pre)
		#return classification_report(self.y_test,self.y_pre)
		f = open('ev.html','w')
		code =self.class_rep
		message = """<html>
		<head></head>
			<body>
				<p>
					<br><h1>{code}</h1><br>
				</p>
			</body>
		</html>
		""".format(code=code)
		f.write(message)
		f.close()
		webbrowser.open_new_tab('ev.html')
		#return message
				

	



	def predict(self,brand,colors,manufacturer):
		#self.df['brand'] = brand_enc.inverse_transform(self.df['brand'])
		#self.df['categories'] = cat_enc.inverse_transform(self.df['categories'])
		#self.df['colors'] = col_enc.inverse_transform(self.df['colors'])
		#self.df['manufacturer'] = man_enc.inverse_transform(self.df['manufacturer'])
		#test=[self.df['brand'],self.df['categories'],self.df['colors'],self.df['manufacturer']
		brand = self.encoder['brand'].transform([brand])[0]
		colors = self.encoder['colors'].transform([colors])[0]
		manufacturer = self.encoder['manufacturer'].transform([manufacturer])[0]
		return self.model.predict(np.array([brand,colors,manufacturer]).reshape(1,-1))


		self.y_pred = self.clfs.predict(test)
		return self.y_pred


