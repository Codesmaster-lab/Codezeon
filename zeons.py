from flask import Flask,make_response,json
from flask import render_template
import requests

API_ENDPOINT = "https://api.jdoodle.com/v1/execute"

client_id = "af5b6520583c5fb9b0de01aa63fa786c"
client_secret = "d29432192af458d541c7d3f1bc8af09686938ab0aa2c8da964176161c938cb7c"
source="x=10;y=25;z=x+y;print (z);"
lang="python3"
stdini=""
LANG_CODE="0"
app=Flask(__name__)

@app.route('/')
def your_code():
    return render_template('editor.html')


@app.route('/compile',methods=['GET','POST'])
def compile():
    data = {'clientId': client_id,
            'clientSecret': client_secret,
            'script': source,
            'stdin': stdini,
            'language': lang,
            'versionIndex': LANG_CODE,
            }
    try:
        headers = {'Content-type': 'application/json'}
        r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)
        json_data = r.json()
        print(json_data)
        status = r.status_code
        print(status)
        output = json_data['output']
        print(output)
    except Exception as e:
        print(e)


    #  x= input("Enter data as : ")
   # cart1 = json.loads(x)
    #collection.insert_one(cart1)
    return make_response('',201)

if __name__=='__main__' :
    app.run()