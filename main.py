from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
    #Quick Main information about me
@app.route("/about")
def about():
    return render_template("about.html")
    #Tells more about me and what I do 

@app.route('/project')
def project():
    return render_template("project.html")
    #Projects such as my autoclikcer 
    #Also need to do more projects
    #MAke anime website as a project


@app.route("/achivements")
def achivements():
    return render_template("achivements.html")
    #Things that I did in robotics and coding competion over 11th and 12th grade.


@app.route("/goals")
def goals():
    return "goals"
    #List my goals and things I want to do
if __name__ == '__main__':
    app.run(debug=True)