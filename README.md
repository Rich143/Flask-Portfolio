### Flask-Portfolio
[![Twitter: @longboardcat13](https://img.shields.io/badge/contact-@longboardcat13-blue.svg?style=flat)](https://twitter.com/longboardcat13)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat)](https://github.com/longboardcat/Flask-Portfolio/blob/master/LICENSE)

This repo is a website template that includes a projects section and blog.

### How to test:
```
$ pip install Flask Flask-Markdown

$ python applications.py

$ open http://127.0.0.1:5000/
```

It should look something like [this][1].


### What you need to do:
In order to populate the templates on your websites, you will need to fill out template files and
add two images.

1. Fill out info.py.
2. Place a resume into `static/assets/resume.pdf`.
3. Place a banner image in `static/images/banner.jpg`.
4. Place an icon image in `static/images/ico/favicon.ico`.
5. Comment out `application.debug = True` in `application.py`.
6. Deploy to the platform of your choice. We are ready for Elastic Beanstalk.

### Blogging
To blog, place markdown files in `static/assets/posts`. Their filenames should be formatted:
`YYYY-MM-DD-Title-Goes-Here.md`. Feel free to change the logic in `blog.py`.

### Deploying to Elastic Beanstalk
Deploying in Elastic Beanstalk is a simple process you can learn more about [here][2]. I can't speak
for other operating systems, but this repo has been tested on OSX.


### License
    The MIT License (MIT)

    Copyright (c) 2016 James Chang

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

[1]: http://www.jameschang.io/
[2]: http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
