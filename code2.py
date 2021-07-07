from flask import request

@app.route('/')
def index():
    module = request.args.get("module")
    exec("import urllib%d as urllib" % module
	
@app.route('/2')
def index2():
    module = request.args.get("module")
    exec("import urllib%d as urllib" % int(module)
	
@app.route('/3')
def index3():
    module = int(request.args.get("module"))
    exec("import urllib%d as urllib" % module
