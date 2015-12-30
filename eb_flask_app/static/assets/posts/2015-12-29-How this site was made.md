This website was made using a [template][1] written in Flask over the holidays.
<hr>

I first learned about Flask on Quora. I viewed it as a framework that is gaining popularity in the
large shadow of Django. What drew me to Flask was its simplicity, but I stayed for its profoundness.
A developer could get a site up and running in a matter of seconds:

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()

The most difficult "bug" for me in cranking out the template was figuring out Elastic Beanstalk. Up
until the last moment, everything was going fine. Then, I chose to deploy my app to `us-west-1`
(N. California) and view my dashboard for `us-west-2` (Oregon) instead. After a few hours of
frustration that my dashboard was empty, I figured out what was wrong.

This project served as a good intro to Flask, S3, and Elastic Beanstalk. There's a lot more to do,
at least on the Flask end. I hope more teams adopt Flask for its simplicity and modularity.

[1]: http://longboardcat.github.io/Flask-Portfolio/
