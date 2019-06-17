from flask import Flask 
from flask import request 
from flask import Response 

import os 

app = Flask(__name__)

os.environ['LOG_FILE_PATH'] = "log/analytics.json"

LOG_FILE_PATH = os.environ['LOG_FILE_PATH']

print(LOG_FILE_PATH)


#GET DIRECTORY OF FILEPATH (IN OS LIBRARY
directory = os.path.dirname(LOG_FILE_PATH)
os.makedirs(directory, exist_ok = True) #if directory does not exist make one
	
		
@app.route('/', methods = ['GET','POST'])
def Log():
	if request.method == 'POST':
		data = request.get_json(force = True)

		with open(LOG_FILE_PATH, 'a') as file:
			file.write(str(data)) 
		
		return Response()


	elif request.method == 'GET':
		return Response()

		

#this allows us to run our app
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)



