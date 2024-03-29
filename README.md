# Flask-app

This is a project i created while teaching myself the Flask web framework. My aim was to learn more about backend-developement and learn some HTML, 
CSS and Java along the way. I chose the Flask web framework as I have some experience in Python and it was described as a good entry point for web developement. 


## Project Description:

This project was mainly created following the [Flask Tutorial](https://flask.palletsprojects.com/en/2.2.x/tutorial/), as this was an easy way for me to learn
the basics of Flask. I then added some of my own while learning more about HTML, CSS and JavaScipt with the 
[MDN Web Docs] (https://developer.mozilla.org/en-US/docs/Learn).  
Things I added are:  
A client-side form validation for my register form using HTML, CSS and JavaScript. I also implemented further validity checks on the backend in my `auth.py` blueprint.  
A new blueprint and .html page for contacting, including the option to upload files. 
For this I looked into [Flask's pattern for file uploads](https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/).  
I also added some elements to my index page while looking into the specifics of Flex-Boxes and Responsive Web Design and made some minor changes to the SQL database,
the config settings of my app and some page's HTML and CSS, added a favicon, etc.

### Example images

![Index Page](/Flask_Index.JPG)
![Register Page](/Flask_Register.JPG)
![Contact Page](/Flask_Contact.JPG)

## Usage

Project installable with `pip install -e`.  
Initialize database with `flask --app flaskr init-db`.  
Run app with `flask --app flaskr (--debug) run`.

## Further plans and ideas

- "about me" and "misc" page
- adding a `maxlength="200"` property to the textarea of contact page together with a character count feedback
- detailed view for single posts
- comment option for posts
- tags for posts
- search box which filters the blog index page
- page display of blog index page
- fix upload of multiple files on contact page
- give blog blueprint an url-prefix like auth and define seperate index in `__init.py__`
