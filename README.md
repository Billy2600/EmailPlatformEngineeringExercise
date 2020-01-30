# Email Platform Engineering Exercise
## Installing
**Note**: This has only been tested in a dev environment, as of now.

1. [Download and install](https://wiki.python.org/moin/BeginnersGuide/Download) Python 
2. Install the Flask and Requests libraries:
* `pip install flask`
* `pip install requests`
3. Navigate to directory where this project is installed
4. Set all variables inside config.json
5. Set FLASK_APP environment variable to `main.py`
* In Windows Powershell, this can be done with `$env:FLASK_APP = "main.py"`
* On Mac and Linux, this can be done with `export FLASK_APP = "main.py"`
6. Run Python with Flask with the following command: `python -m flask run`
7. Send a JSON POST request like the following to `http://127.0.0.1:5000/email`:
```{
	"to": "fake@fake.com",
	"to_name": "Mr. Fake",
	"from": "norpely@myfakewebsite.com",
	"from_name": "Fake Website",
	"subject": "A message from Fake Website",
	"body": "<h1>Your Bill</h1><p>$10</p>"
}
```

## Languages, Libraries, etc.
Python is not my language of choice, most of the time. However, it is really good at quick iteration, and for distributing small projects with very little setup. Packages can be installed quickly and easily with short terminal commands. This also presented something of a learning opportunity for me, as I had never used Flask before this; most of my Python work was done automating tasks. This did end up making the project take longer, expectedly.

* Flask was the natural choice for creating the API layer. It's popular, well supported, and had a lot of documentation available. I could get it up and running quickly.
* Requests was used because it provided an easy way to integrate existing APIs, necessary for actually sending the emails. Calls could be made within a few lines of code.

## Tradeoffs, What I'd Do Differently, etc.
* Again, because I chose technologies I wasn't completely familiar with it ended up taking longer, and some of the technologies might not have been used to their full potential.
* Were this a 'full' project, I probably would've tried to separate the controller, model, and service into their own subdirectories
* An obvious thing I'd change is configuration loading being a part of EmailService -- in a 'real' project I'd probably implement this as its own class.
* Only basic validation is being done on the different email fields, as well as stripping the HTML tags. It doesn't even check that that email addressess are valid address -- should include a @, domain name, etc. (There's probably a library to do this out there) There probably is in fact a smarter way to handle stripping the HTML tags, but I think most modern HTML clients read HTML anyway, so I'm not sure what that'd be without more research.
* There's probably a faster way to convert to/from a Python object and a JSON object.
* Ran into an issue early on where `from` is a reserved keyword in Python.
* Unit tests should definitely be added, with Python's `unittest` framework.
* Error messages are not super descriptive, and there is currently no indication which email service was used.