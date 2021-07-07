from flask import request

@app.route('/')
def index():
    module = request.args.get("module")
    exec("import urllib",int(module),"d as urllib") 
