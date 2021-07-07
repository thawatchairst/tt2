from flask import request

@app.route('/')
def index():
    module = int(request.args.get("module"))
    exec("import urllib%d d as urllib" % modlue) 
