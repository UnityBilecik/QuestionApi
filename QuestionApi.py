from flask import Flask,jsonify,request
import Scripts.QuestionHelper as QH

app = Flask(__name__)

@app.route('/')
def Home():
    return jsonify("Home")

@app.route('/GetQuestion',methods=["GET","POST"])
def GetQuestion():
    amount=5
    diffuculty=""
    questionType=""
    if(request.method == "POST"):
        try:
            if(request.form.get("amount")!=None):
                amount = int(request.form.get("amount"))
            if(request.form.get("diffuculty")!=None):
                diffuculty = request.form.get("diffuculty")
            if(request.form.get("questionType")!=None):
                questionType = request.form.get("questionType")

        except:
            print("Value None")
    return jsonify(QH.GetQuestion(amount,diffuculty,questionType))



if __name__ == '__main__':
    app.run()