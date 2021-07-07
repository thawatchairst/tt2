from flask import request

@app.route('/3')
def index():
    module = int(request.args.get("module"))
    exec("import urllib%d as urllib" % int(module)
