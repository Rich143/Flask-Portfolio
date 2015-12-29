import info
from blog import construct_blog_posts
from flask import Flask
from flask import render_template
from flaskext.markdown import Markdown


# This is the main file for the website. Here you will find various apps routes and pages the app
# manages, as well as the means to run the actual app.
#
# Test with:
#
#     python application.py

# This is the core flask application that Elastic Beanstalk recognizes.
#
# ---------------------------------------------------------
# DO NOT CHANGE THIS LINE IF DEPLOYING TO ELASTIC BEANSTALK
# ---------------------------------------------------------
#
application = Flask(__name__)

# Enabling markdown allows us to write prettier blog posts
Markdown(application)

# These are the arguments passed into the templates that will be used with every rendered page. They
# take care of Search Engine Optimization and nav-bar stuff and can be edited in info.py.
layout_args = {
    "meta" : info.meta,
    "navigation" : info.nav,
}

# The root directory of our website. We're only concerned with rendering the homepage and our list
# of projects that will be loaded from info.py.
@application.route("/")
@application.route("/index")
@application.route("/index.html")
def index():
    return render_template("index.html",  about=info.about, projects=info.projects, **layout_args)

# This is where our blog routes to. The blog post page is constructed in blog.py and is currently
# one long page, capable of writing posts in markdown. Posts are written as individual files in
# /static/assets/posts.
@application.route("/blog")
@application.route("/blog.html")
def blog():
    path = 'static/assets/posts/'
    return render_template("blog.html", blog_posts=construct_blog_posts(path), **layout_args)

# Our resume will be served as a static file, simple and easy to download.
@application.route("/resume")
@application.route("/resume.pdf")
def resume():
    return application.send_static_file("assets/resume.pdf")

if __name__ == "__main__":
    # Uncomment this line if you wish to see debug messages and exceptions rendered in the browser.
    # application.debug = True
    application.run()
