This website was made using a [template][1] written in Flask over the holidays.
<hr>

I first learned about Flask on Quora. Flask is a framework that is gaining popularity in the
large shadow of Django, and it's most apparent advantage is simplicity.
A developer could get a site up and running in a matter of seconds:

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()

It's sticking point, however, is its profoundness.

The most difficult "bug" that caused much frustration was figuring out Elastic Beanstalk. Up
until the last moment, everything was going fine. Then, I deployed my app to `us-west-1`
(N. California) and viewed my dashboard for `us-west-2` (Oregon) instead. Only after a few hours was
the discrepancy found.

This project served as a good intro to Flask, S3, and Elastic Beanstalk. There's a lot more to do,
at least on the Flask end. More teams should adopt Flask for its simplicity and modularity.

[1]: http://longboardcat.github.io/Flask-Portfolio/
