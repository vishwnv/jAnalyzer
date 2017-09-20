from flask import Flask, request, render_template, flash, url_for , redirect
from Scripts.CategoryClassifying import CatClassifier
from Scripts.SentimentClassifying import SentimentAnalyzer

from JustTest.SubPackage import Cat


t = Cat.Cat("s");
t.add_trick("num1");
t.add_trick("num2");
result = t.get_tricks();

print(result)

"""
    This area defines global functions
    -------------------------------------------------
    -------------------------------------------------
    -------------------------------------------------
"""
def WriteDataToFile(text , file):
    open(file, "w").close()
    with open(file, "a+") as text_file:
        print(text, file=text_file)



def AnalyzeForCategory():
    d = CatClassifier.CatClassF()
    d.ClearFiles()
    d.DoClassification()

app = Flask(__name__)
app.secret_key = 'Dont tell anyone'


"""
    This specifies the routes used in the application 
    -------------------------------------------------
    -------------------------------------------------
    -------------------------------------------------
"""
@app.route('/')
def index():
    return  'Method used is : %s' % request.method

@app.route('/dashboard')
def dashboard():
    return  render_template("dashboard/dashboard.html")

@app.route('/dashboard' , methods = ['GET' , 'POST'])
def dashboard_post():
    text = request.form['input_review']
    processed_text = text.lower()

    txt_file = "E:/CDAP/FlaskProject/Testing/TestInputs/reviewToBeTested.txt"
    try:
        WriteDataToFile(processed_text,txt_file)
        AnalyzeForCategory()
        flash('Successfully Analyzed')
    except ValueError:
        flash('Analyzing interrupted')


    return render_template("dashboard/dashboard.html")


@app.route('/category')
def category():
    commonFilePath = "E:/CDAP/FlaskProject/TextFiles/Outputs/"

    try:
        directing = open(commonFilePath + "directing.txt", "r").read()
        acting = open(commonFilePath + "acting.txt", "r").read()
        storyline = open(commonFilePath + "storyline.txt", "r").read()
    except Exception as e:
        print(e)

    if directing is not None and acting is not None and acting is not None :
        return render_template("dashboard/category.html" , dir=directing , act=acting , stor=storyline)
    else :
        return render_template("dashboard/category.html")


@app.route('/category' , methods = ['GET' , 'POST'])
def category_post():
    resultSents = []

    s = SentimentAnalyzer.Analyzer()
    s.PrintclassierAccuracies()
    commonFilePath = "E:/CDAP/FlaskProject/TextFiles/Outputs/"

    try:
        directing = open(commonFilePath + "directing.txt", "r").read()
        acting = open(commonFilePath + "acting.txt", "r").read()
        storyline = open(commonFilePath + "storyline.txt", "r").read()
    except Exception as e:
        print(e)

    if directing is not None and acting is not None and acting is not None:
        try:
            tempAct = s.sentiment(acting)
            tempStory = s.sentiment(storyline)
            tempDirect  = s.sentiment(directing)
        except Exception as e:
            print("Exception for sentiment of categories " + e)

    if tempAct is not None and tempStory is not None and tempDirect is not None:
        if directing is not None and acting is not None and storyline is not None:
            flash('Sentiment Analyzing Succeeded')
            return render_template("dashboard/category.html", dir=directing, act=acting, stor=storyline , act_sent = tempAct , act_dir = tempDirect , act_stor = tempStory)
    else:
        flash('Sentiment Analyzing interrupted')
        return render_template("dashboard/category.html")


@app.route('/gh')
def tt():
    return render_template("dashboard/dashboard.html",)


@app.route('/bacon' , methods = ['GET' , 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using Post"
    else:
        return  "You are using Get"


@app.route('/tuna')
def tuna():
    return  '<h2> Tuna is good </h2>'


@app.route('/profile/')
@app.route('/profile/<username>')
def profile(username = None):
    return  render_template("profile.html" , name = username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return  "Post Id is  %s" % post_id


def tuna():
    return  '<h2> Tuna is good </h2>'


@app.route('/shopping/')
def shopping():
    food = [ "Cheese" , "Orange" , "Apple" , "Butter"]
    return render_template("shopping.html", food=result)

if __name__ == "__main__":
    app.run(debug=True)