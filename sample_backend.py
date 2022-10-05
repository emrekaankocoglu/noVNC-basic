from flask import Flask, jsonify,request,abort
app=Flask(__name__,static_url_path='',static_folder='')
@app.route('/session')
def health():
    return jsonify(host="164.92.227.51",port=6080)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)