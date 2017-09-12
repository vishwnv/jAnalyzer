from flask import Flask , request , render_template
from JustTest.SubPackage import Cat

t = Cat.Cat("s");
t.add_trick("num1");
t.add_trick("num2");
result = t.get_tricks();

print(result)

app = Flask(__name__)

# @ signifies a decorator
@app.route('/')
def index():
    return  'Method used is : %s' % request.method

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