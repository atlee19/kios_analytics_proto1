from flask import Flask 
from flask import request 
from flask import Response 
from flask import jsonify

import os 
import datetime



app = Flask(__name__)
time_stamp = datetime.datetime.now() #later change this so it only stamps day
 


#might turn this into a class
DIRECTORY_NAME = "log"
FILE_NAME = "analytics.json " + str(time_stamp) # adding time stamp 
FILE_PATH = '' 



def CreateDirectory():
	if os.path.isdir("log"): #if directory exists then skip 
		print("directory already exists")
	else:
		os.makedirs(DIRECTORY_NAME) #if directory does not exist make one
	

def CreateFilePath():
	FILE_PATH = os.path.join(DIRECTORY_NAME, FILE_NAME)
	return FILE_PATH

#its overwriting the same file --so save as new file? 
@app.route('/', methods = ['GET','POST'])
def Log():
	data = None
	if request.method == 'POST':
		CreateDirectory() 
		#creates a file path ex. log/analytics
		file_path =  CreateFilePath() 
	 	#creates our actual file ex. analytics.jsonlist
		file = open(file_path, 'a')
		#write the json data into our file
		data = request.get_json(force = True)
		print("Data from file: {}".format(data))
	 	#writing to our file 
		file.write(str(data))
	 	#close the file once we're done writing 
		file.close() 
		return Response()


	elif request.method == 'GET':
		return "<h1>waiting for data...</h1>"

		

	

#this allows us to run our app
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)



