#import modules
import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World ...testing'


Global settings
if __name__ == '__main__':      
    app.run(host=os.environ.get('IP'),              
    port=int(os.environ.get('PORT')),              
    debug=True)

# # local settings
# if __name__=='__main__':
#     app.run(host = '0.0.0.0',
#     port = int('8080'),
#     debug=True) 