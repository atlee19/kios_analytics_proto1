from flask import Flask 
from flask import request 
from flask import Response 
from flask import jsonify
from flask import abort 

import os 
import datetime



app = Flask(__name__)
time_stamp = datetime.datetime.now() 
 


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

def CheckFileToBig(this_file, size_limit):
	if os.stat(this_file).st_size >= size_limit:
		print("FILE TOO LARGE!!!")
		abort(404)
		return 1; 

		
@app.route('/', methods = ['GET','POST'])
def Log():
	if request.method == 'POST':
		CreateDirectory() 
		#creates a file path ex. log/analytics
		file_path =  CreateFilePath() 
	 	#creates our actual file ex. analytics.jsonlist
		file = open(file_path, 'a')
		#read in the data from the json file 
		data = request.get_json(force = True)
	 	#writing to our file 
		file.write(str(data))
		file.close() 
		#print("{} bytes (FILE)".format(os.stat(file_path).st_size))

		return Response()


	elif request.method == 'GET':
		return "<h1>waiting for data...</h1>" #this is just a place holder

		

#this allows us to run our app
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)



