# http://localhost:5000 - should display 8 by 8 checkerboard
# http://localhost:5000/4 - should display 8 by 4 checkerboard
# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('index.html')

@app.route("/<num>")
def small_board(num):
  print('javan')
  print(num)
  return render_template('index.html', num = 8)



if __name__ == "__main__":
  app.run(debug=True)