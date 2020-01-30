# Email Platform Engineering Exercise
## Installing
**Note**: This has only been tested in a dev environment, as of now.

1. [Download and install](https://wiki.python.org/moin/BeginnersGuide/Download) Python 
2. Install the Flask and Requests libraries:
* `pip install flask`
* `pip install requests`
3. Navigate to directory where this project is installed
4. Set FLASK_APP environment variable to `main.py`
* In Windows Powershell, this can be done with `$env:FLASK_APP = "main.py"`
* On Mac and Linux, this can be done with `export FLASK_APP = "main.py"`
5. Run Python with Flask with the following command: `python -m flask run`
6. Send a JSON POST request like the following to `http://127.0.0.1:5000/email`:
```{
	"to": "fake@fake.com",
	"to_name": "Mr. Fake",
	"from": "norpely@myfakewebsite.com",
	"from_name": "Fake Website",
	"subject": "A message from Fake Website",
	"body": "<h1>Your Bill</h1><p>$10</p>"
}```

## Languages, Libraries, etc.
Python is not my language of choice, most of the time. However, it is really good at quick iteration, and for distributing small projects with very little setup. Packages can be installed quickly and easily with short terminal commands. This also presented something of a learning opportunity for me, as I had never used Flask before this; most of my Python work was done automating tasks.
