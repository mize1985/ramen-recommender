from flask import Flask as Flask
from flask import request
from flask import render_template
from recommender_api import get_recommendation

app = Flask(__name__)  # create instance of Flask class

@app.route("/")
def hello_world() -> str:
    """Let's say Hi to the world.

    Returns:
        str: The HTML we want our browser to render.
    """

    return render_template('intro_recommender.html')
    
    
@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    x_inputs,recommended_list,recommended,vector = get_recommendation(request.args)
    return render_template('recommender.html',
                             x_inputs=x_inputs,
                             recommended=recommended,
                             recommended_list=recommended_list)
    
    app.run(debug=True)
if __name__=='__main__':
    app.run()
