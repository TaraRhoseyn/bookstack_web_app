# Bookstack

![Responsive mockup of website](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/readme/responsive-mockup.png)

[View the live project](https://bookstack-ms3.herokuapp.com/)

**User credentials**

To use the website you can either create an account and build your stacks, or use these following test user credentials:

- Username: TestAccount
- Password: Test1234

## Table of Content

## Project Goals

### Website owner business goals

- I want users to be able to track their reading goals and potential. 
- I want to be able to generate income through affiliate selling links through my web app. 

### User goals

- I want to be able to track my reading goals. 
- I want to see what other users are saying about books I've read or want to read. 
- I want to challenge myself to read more books.

## Design

### Wireframes

You can view the [PDF file](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/readme/wireframes.pdf) of the wireframes on this repo. If you find the file is taking too long to load, please visit the [Figma file](https://www.figma.com/file/4TWPdbIVCakRCiTsi93FH8/MS3-Wireframe?node-id=0%3A1).

**Changes from wireframe to production**

1. In my original design...

## Structure

### Physical database model

**Original database model**

![Original database model](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/readme/og_database_model.PNG)

The model above was my original intention for the schema of the database used for the project. Due to need for foreign keys I realised this schema would be better deployed using a relational database rather than a NoSQL document-based database that I was using for this project. 

Upon realising this I changed my database model to reflect better use of the MongoDB database. Please note: the connections shown in the model here do not reflect foreign keys but when the same data is pushed to the different collections.

**Current/updated database model** 

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)

### Frameworks & Libraries

- [Flask](https://flask.palletsprojects.com/) - Python web framework, used for displaying data from backend databases to frontend presentation.
- [Materialize](https://materializecss.com/) - CSS framework, mainly used for components.
- [jQuery](https://jquery.com/) - JavaScript library, used for refactoring code.
- [MongoDB](https://www.mongodb.com/) - Cloud-based NoSQL database, used for housing data.
- [Google Fonts](https://fonts.google.com/) - Merriweather font used in the design throughout.
- [Google Icons](https://fonts.google.com/icons) - Used in the design throughout.
- [Boto](http://boto.cloudhackers.com/en/latest/) - Python interface to AWS.
- [Werkzeug](https://pypi.org/project/Werkzeug/) - WSCI web application library to assist in debugging and security validations.
- [DNSPython](https://pypi.org/project/dnspython/) - DNS toolkit for Python.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - Helpers to bridge Flask and PyMongo.


### APIs and Integrations

- [EmailJS API](https://www.emailjs.com/) - For taking data from the contact form and sending it to my email. 
- [Open Library Covers API](https://openlibrary.org/dev/docs/api/covers) - For retrieving the images of book covers based on the book's ISBN.
- [Amazon Web Services (AWS) S3 Buckets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html) - For storing and displaying user's profile picture once user uploads the image as part of the registration process.

### Workspace and version control

- [GitHub & Git](https://github.com/) - Remote repository storage, used for storage and version control. 
- [Gitpod/VSCode](https://www.gitpod.io/) - Integrated Development Environments (IDEs), Gitpod was used mainly with desktop VSCode being used occassionality.
- [Heroku](https://www.heroku.com/) - Used for deployment. 

## Resources

### Design resources

- [Figma](https://www.figma.com/) - Used for wireframing.
- [Freepik](https://www.freepik.com/) - Imagery used in design.
- [Favicon Generator](https://www.favicon-generator.org/) - Generating Favicon.
- [Canva](https://www.canva.com/) - For generating responsive mockup.
- [Image Compressor](https://imagecompressor.com/) - For compressing PNG files to optimize webpage performance.


### Testing resources

- [WebAIM's WAVE tool](https://wave.webaim.org/) - For testing accessibility.
- [The W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) - For validating HTML.
- [The W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/#validate_by_input) - For validating CSS.
- [JSHint](https://jshint.com/) - For testing JavaScript.
- [PEP8 Online](http://pep8online.com/) - For checking PEP8 compliance.
- [Google Lighthouse](https://developers.google.com/web/tools/lighthouse/) - For checking performance, SEO and accessibility.

### General resources

- [Stack overflow](https://stackoverflow.com/) - For general best practice.
- [W3Schools](https://www.w3schools.com/) - For general best practice on formatting code and fixing small issues.
- Code Institute Slack - For seeing examples of similar projects and understanding where others aimed to improve.


## Bugs

### Bugs found and resolved during development:

**Bug 1**: When rendering user information to the user_profile template, the data for the number of books users had read or not read was causing an error due to the data being a cursor Object. 
- **Solution**: I researched the topic on Stack Overflow I converted the cursor Object into a dictionary to then loop over and append to existing variable, which is where the data is displayed from. 

**Bug 2**: When updating your username and password in the user_profile template, the data would be successfully updated in the database but not in the variables stored that displayed the data to the frontend. So you would change your username, but the username you'd see at the top of the user_profile template would remain the same.
- **Solution**: Removing the render_template that kept users on the same page and updated the flask session (using session.pop()) to allow the browser to refresh session user upon the user re-logging in with their new credentials.

**Bug 3**: When submitting the user registration form, a 400 Bad Request exception would be raised on keyerror 'user_image', preventing the POST form from being submitted.
- **Solution**: Fixed by adding in a name attribute onto the form elements that I had mistakenly left off. 

**Bug 4**: Again when submitting the user registration form, a botocore exception (No Credentials Error) would be raised, preventing form submission.
- **Solution**: I was using the incorrect variable names for the access keys.

**Bug 5**: When submitting a profile picture in the registration form (using Boto and AWS), the image would successfully be sent the AWS s3 bucket and the filepath would successfully be stored in the 'user_image' key within my Mongo database. However, I could not get the file path displaying back to the user on the frontend. 
- **Solution**: This was the most complex bug to solve in the project. It involved many hours of research into AWS policies and outreach support from the Code Institute support team. The bug was fixed following this process:
1. **Updating S3 Bucket policy**: Updating value of the key 'Sid' to 'AllowPublicRead', updating the value of key 'Principle' from being IAM-user based to general.
2. **Updating S3 ACL policy**: Allowing full access to all global users (public access)
3. **Updating function that stores image to S3**: Adding in an extra argument, 'ACL='public-read'' to the function.
4. **Updating method of rendering image path on frontend**: Originally, I was pulling the file path data from the database within an iteration method that returned an array of objects. Since there is only 1 unique file path per user, this was unnecessary. Instead of pulling data from the DB to frontend through a function, I went straight through with jinja templating in user_profile.html.  

**Bug 6**: When trying to implement filtering on the dashboard to make sure users can only see books they themselves have added, I ran into the issue of no books at all being rendered after a user has added book/s, despite all data being correct in the database.
- **Solution**: Although my if logic within the jinja template was correct in filtering down to only the user's books, I realised that the conditions I had in the for loop that only display the first three items in loop was causing no books to display. This was because the index was not long enough in my tests to trigger the loop to look for this specific number of items. I removed the loop indexing condition ([0-3]) from the for loop in dashboard.html and the issue was resolved.

**Bug 7**: When trying to display both read and unread books to the user in stack.html, my method of displaying the unread books was not rendering the data from the database despite all correct key and value names. 
- **Solution**: My original method was to use two *for* loops to iterate over the 'books' dictionary in the database and in each *for* loop have an *if* statement that found either books marked as read or unread. I realised that having two iterating methods was not going to work, as the dictionary was already being unpacked by the first so the second didn't have anything to iterate over. I adjusted my design to make only one *for* loop work. Now in this *for* loop there's one *if* statement that has an *else* condition that can correctly display unread books to the user. 

### Fixes required for validation purposes:

#### HTML Validation

- Removed duplicate IDs on Register page.
- Removed value attribute from input elements from Register page.
- Added alt attribute to image found on home page. 
- Added alt attribute to image found on navbar across the site. 
- Removed duplicate main element rendered by the Dashboard template.
- Removed duplicate IDs on Dashboard page. 
- Removed redundant aria-describedby attributes on all i elements across the site.
- Added space between attributes found on form elements across the site.
- Removed stray end div tags on all form elements across the site.
- Removed pattern attribute from textarea eleements. 

#### CSS Validation

- None required. 

#### PEP8 Compliance

- Added docustrings to all functions.
- Added new blank line at the end of files.
- Added two blank lines above functions.
- Adjusted indentation on a handful of functions.

#### JSHint

- None required.

#### WAVE

- Made all button text black for contrast.
- Make all form input labels black for contrast.
- Added aria-label to empty link (navbar).

## Credits

### Code

- **Code Institute** - For their lessons on Jinja, Flask and Python. Especially their 'Task Manager Mini Project'. 
- **Geek for Geeks** - For [404 error handling](https://www.geeksforgeeks.org/python-404-error-handling-in-flask/) within Flask.
- **Stack Overflow** - For using [classList.toggle() method](https://stackoverflow.com/questions/52556194/how-to-toggle-on-off-javascript) to display or hide content upon event listeners. For [converting a cursor object into a dict](https://stackoverflow.com/questions/28968660/how-to-convert-a-pymongo-cursor-cursor-into-a-dict)
- **Angela Delise** - For informing [responsive CSS grid layout](https://www.youtube.com/watch?v=68O6eOGAGqA) best practices.
- **W3 Docs** - For [vertical alignments](https://www.w3docs.com/snippets/css/how-to-vertically-align-elements-in-a-div.html) of elements.
- **Corey Schafer** - For [Blueprints and Configuration guidance for codebase structure](https://www.youtube.com/watch?v=Wfx4YBzg16s&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=12)
- **Ansible** - For [indexing loop methods](https://ansiblemaster.wordpress.com/2016/07/27/jinja2-using-loop-index-and-loop-length-examples-etchosts-and-workers-properties/) that allows me to only display to the user the first/last item in dicts on dashboard.html
- **Paul Meeneghan** - For codebase structure based on Blueprints method in [their own MS3](https://github.com/pmeeny/CI-MS3-FootballMemories). 
-**Be a Better Dev YouTube tutorial** - Helpful in [configuring S3 Bucket](https://www.youtube.com/results?search_query=aws+s3+bucket+public) to display images publically.

### Media

- **Freepik** - For using [illustration](https://www.freepik.com/free-vector/cozy-home-composition-with-character-girl-warm-clothes-reading-book-lounge-chair-illustration_17345961.htm#page=1&query=book%20reading&position=47&from_view=search) in the main navbar and home page of the site.
- **Canva** - For [generating responsive mockup](https://www.canva.com/).
