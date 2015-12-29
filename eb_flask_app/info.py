meta = {
    "title" : "jameschang.io",
    "author" : "James Chang",
    "description" : "James Chang's website",
    "url" : "http://www.jameschang.io",
    "icon_path" : "static/images/ico/favicon.ico",
    "keywords" : "james, chang, caltech, square, fastclone, longboardcat"
}

nav = [
    {
        "name" : "projects",
        "link" : "index.html#projects"
    },
    {
        "name" : "blog",
        "link" : "blog",
    },
    {
        "name" : "resume",
        "link" : "resume"
    }
]

about = [
    {
        "description" :
            """
            Welcome to my website made with <a target="_blank" href="http://getbootstrap.com/">Bootstrap</a>
            and <a target="_blank" href="http://flask.pocoo.org/">Flask</a>.
            I'll be making more improvements as I learn Flask.
            Flask is pretty amazing, but I'm still resorting to "non-pythonic"
            and "non-flasky" ways of doing things.
            """
    },
    {
        "description" :
            """
            I'm currently working as a Software Engineer at <a target="_blank" href="https://squareup.com/">Square</a> on the release
            team specializing in the iOS release process.
            If you want to talk to me about how messy codesigning is, I'm your man.
            I also do a little work on <a target="_blank" href="https://corner.squareup.com/2015/11/fastclone.html">git-fastclone</a>,
            a tool that allows for significantly quicker repeating checkouts. We use fastclone in our iOS
            release toolchain, and I'd appreciate any improvements, suggestions,
            and pull requests.
            """
    },
    {
        "description" :
            """
            In my spare time, I like to play video games, watch movies, and hang out
            with my friends. Check out my <a target="_blank" href="http://www.jameschang.io/blog.html">blog</a>
            to get more insight into my life,
            or check out my <a target="_blank" href="http://www.jameschang.io/resume.pdf">resume</a>
            if you want to chat.
            """
    }
]

projects = [
    {   "link" : "http://longboardcat.github.io/Flask-Portfolio/",
        "icon_class" : "fa fa-bookmark icon-md icon-color-dark",
        "name" : "Flask-Portfolio",
        "description" : "Lightweight flask implementation to create templated portfolio websites, like this one."
    },
    {
        "link" : "https://corner.squareup.com/2015/11/fastclone.html",
        "icon_class" : "fa fa-github-alt icon-md icon-color-dark",
        "name" : "git-fastclone",
        "description" : "A Ruby gem that performs lightning-fast checkouts of git repos."
    },
    {
        "link" : "https://corner.squareup.com/2015/07/ios-build-infrastructure.html",
        "icon_class" : "fa fa-apple icon-md icon-color-dark",
        "name" : "iOS build infrastructure",
        "description" : "Working on the in-house ios builder application at Square, Inc."
    },
    {
        "link" : "https://github.com/longboardcat/RoboTrike",
        "icon_class" : "fa fa-power-off icon-md icon-color-dark",
        "name" : "RoboTrike",
        "description" : "Robotics is challenging. Now try writing it all in assembly."
    },
    {
        "code" :
            '''
            <script type="text/javascript" src="static/js/toggle.js"></script>
            <script type="text/javascript" src="static/js/countUp.js"></script>
            <h1 id="countUpElement">0</h1>
            <script type="text/javascript">
                var options = {
                    useEasing : true,
                    useGrouping : true,
                    separator : ',',
                    decimal : '.',
                    prefix : '',
                    suffix : ''
                };
                var countingAnimation = new CountUp("countUpElement", 0, 4, 0, 4, options);
                countingAnimation.start();
            </script>
            ''',
        "name" : "Technical Interviews Given",
        "description" : "Giving interviews is fun, and I'm perfecting a few questions."
    }
]
