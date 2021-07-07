from flask import request

@app.route('/')
def index():
    module = request.args.get("module")
    exec("import urllib%d as urllib" % module
	
@app.route('/2')
def index2():
    module2 = request.args.get("module")
    exec("import urllib%d as urllib" % int(module2)
	
@app.route('/3')
def index3():
    module3 = int(request.args.get("module"))
    exec("import urllib%d as urllib" % module3
