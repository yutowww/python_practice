#Flaskとrender_template(HTMLを表示させる為の関数)をインポート
from flask import Flask,render_template

#Flaskオブジェクトの生成
app = Flask(__name__)



#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    name = "who"
    #return name
    return render_template('hello.html', title='hello2', name=name)



#おまじない
if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)