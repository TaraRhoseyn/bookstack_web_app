# Bookstack

![Responsive mockup of website](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/readme/responsive-mockup.png)

[View the live project](https://bookstack-ms3.herokuapp.com/)

**User credentials**

To use the website you can either create an account and build your stacks, or use these following test user credentials:

- Username: TestAccount
- Password: Test1234

## Table of Content

## Strategy

### Website owner business goals

- I want users to be able to track their reading goals and potential. 
- I want to be able to generate income through affiliate selling links through my web app. 

### User goals

- I want to be able to track my reading goals. 
- I want to see how I felt about books through book reviews.
- I want to challenge myself to read more or read specific sets of books.
- I want to keep track of books I intend to read.

## User experience

I have designed an app-style site with mobile in mind by building the responsive layout mobile-first using Materialize layout utility classes. 

The user experience is heavily structured around the concept of an app-based user journey. Users can see a slice of all their data from a Dashboard which will display the first or last pieces of collection data associated with that specific user. Users also have multiple entry points to edit, delete or add pieces of data, whether from the Dashboard or the individual landing pages available on the navbar.

## Scope

### User stories

I have divided my user stories into two categories: first-time users and regular visitors, with the understanding that one of the key goals of the website is to encourage returnability in the users of the website.

**First-time users**

1. As a first-time user, I want to be able to register in a simple, intuitive way with as little friction as possible.
2. As a first-time user, I want clear instructions on how to access all of the features of the website. 
3. As a first-time user, I want to be able to personalize my profile with some personal touches such as a profile picture associated with my account. 
4. As a first-time user, I want to be able to add books to my data to keep track of which books I've read or not read. 
5. As a first-time user, I want to be able to log out easily so that I can come back to populating my account at a later date.
6. As a first-time user, I want the website to direct me back home if I trigger a 404 error through a bad link.
7. As a first-time user, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.

**Regular visitors**

8. As a regular visitor, I want to be able to see which book I should read next to guide my reading practices.
9. As a regular visitor, I want to challenge myself to fulfill reading goals I set for myself.
10. As a regular visitor, I want to be able to give feedback to improve the website over time.
11. As a regular visitor, I want to be able to login in a simple, intuitive way with as little friction as possible.
12. As a regular visitor, I want to be able to keep track of my thoughts and feelings about the books I read. 
13. As a regular visitor, I want to be able to change a book from 'read' to 'unread' and vice versa easily. 
14. As a regular visitor, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
15. As a regular visitor, I want to easily be able to edit or delete the books I have marked as read or unread.
16. As a regular visitor, I want to easily be able to edit or delete the challenges I have set for myself, or make them as complete.
17. As a regular visitor, I want to easily be able to edit or delete the reviews I have added. 
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.
19. As a regular visitor, I want to easily be able to view my user information, edit it as necessary or delete it.

**Site owner**

20. As a site owner, I want to be able to collect feedback from users in a simple and easy way that I can iterate versions of the website based on an informed understanding of user needs. 
21. As a site owner, I want users to be able to navigate the website easily so that users are more likely to have an enjoyable experience and return to use the website.

## Features

### Current Features

Please note: Whenever data is added, editted or removed from the database, flash messages are displayed to the users.

**Feature 1: Home page**

The home page is rendered if no session user is found and directs users to either sign up or log in.

![Feature 1](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-1.PNG)

*User stories covered by this feature:*

1. As a first-time user, I want to be able to register in a simple, intuitive way with as little friction as possible.
11. As a regular visitor, I want to be able to login in a simple, intuitive way with as little friction as possible.
21. As a site owner, I want users to be able to navigate the website easily so that users are more likely to have an enjoyable experience and return to use the website.

**Feature 2: Register page**

The registration page allows users to register up to the website through selecting a username, password and uploading a profile picture. The password is passed through to the MongoDB users collection through salt hashing for security. Usernames will only be accepted if the username is not already taken (this error will trigger an error message). The profile picture is uploaded to a AWS S3 Bucket and rendered back to the user through the file path saved as a key value in the MongoDB users collection associated with the user. It's also possible to direct yourself through the Login page if you alredy have an account, through a link next to the main submit button and the login link available on the navbar. Upon successful registration, user's will be directed to their Dashboard and receive confirmation through a flash message.

![Feature 2](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-2.PNG)

*User stories covered by this feature:*

1. As a first-time user, I want to be able to register in a simple, intuitive way with as little friction as possible.
7. As a first-time user, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
21. As a site owner, I want users to be able to navigate the website easily so that users are more likely to have an enjoyable experience and return to use the website.
2. As a first-time user, I want clear instructions on how to access all of the features of the website. 
3. As a first-time user, I want to be able to personalize my profile with some personal touches such as a profile picture associated with my account. 

**Feature 3: Login page**

The login page allows users to log in with their main account credentials: username and password. Once logged in, the session user will be a key piece of data passed between many functions within the app to render the user's data. The user is also directed to the registration page if they cannot login. Upon successful login, user's will be directed to their Dashboard and receive confirmation through a flash message.

![Feature 3](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-3.PNG)

*User stories covered by this feature:*

11. As a regular visitor, I want to be able to login in a simple, intuitive way with as little friction as possible.
7. As a first-time user, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
21. As a site owner, I want users to be able to navigate the website easily so that users are more likely to have an enjoyable experience and return to use the website.


**Feature 4: Dashboard**

The Dashboard serves as the main hub of the app, where users can quickly glance at their most important data points in one centralized place. It acts as the main home page for users once they've registered/logged in. The page is divided into the header/nav (more on this later), the footer (again, this is a seperate feature) and three cards. Users are only able to see data on the Dashboard that has been added by them personally. The page also gives some brief information on how the website uses stacks and instructions to new users on how to get started using the site.

The dashboard as a whole using the above TestAccount credentials (see top of this file):

![Feature 4](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-4.PNG)

*User stories covered by this feature:*

2. As a first-time user, I want clear instructions on how to access all of the features of the website. 
4. As a first-time user, I want to be able to add books to my data to keep track of which books I've read or not read. 
8. As a regular visitor, I want to be able to see which book I should read next to guide my reading practices.
9. As a regular visitor, I want to challenge myself to fulfill reading goals I set for myself.
12. As a regular visitor, I want to be able to keep track of my thoughts and feelings about the books I read. 
14. As a regular vivistor, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.
15. As a regular visitor, I want to easily be able to edit or delete the books I have marked as read or unread.
16. As a regular visitor, I want to easily be able to edit or delete the challenges I have set for myself, or make them as complete.
17. As a regular visitor, I want to easily be able to redit or delete the reviews I have added. 

*Section 1: The first card, 'Next book to read'*

The 'Next book to read' section displays the first book that users add to their data as 'unread', encouraging readers to clear their 'unread' stack from first to last. The book cover, title and author is all generated from data given by the user in the 'Add book' or 'Edit book' pages and held in the 'books' collection in MongoDB. The book data is connected to the session user through the 'added_by' key within the 'books' collection documents. 

The '+' symbol will direct users to add a new book. The '...' symbol will direct users to view all of their books (the Stacks page). Both symbols are tooltipped to display this information on hover.

![Feature 4a](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-4a.PNG)

*Section 2: The second card, 'Challenge to finish'*

The 'Challenge to finish' section displays the last challenge set by the user, with the option of editing the challenge to mark as complete. In future iterations, I hope that users would be able to manually select which of their challenges they'd like to see displayed on their dashboard.

The '+' symbol will direct users to add a new challenge. The '...' symbol will direct users to view all of their challenges (the Challenges page). Both symbols are tooltipped to display this information on hover.

![Feature 4b](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-4b.PNG)

*Section 3: The third card, 'Your last review'*

The 'Your last review' section displays the last review written by the user, along with the book data attached to that review, with the option of editing the review.

The '+' symbol will direct users to add a new review. The '...' symbol will direct users to view all of their reviews (the Reviews page). Both symbols are tooltipped to display this information on hover.

![Feature 4c](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-4c.PNG)

**Feature 5: Navbar**

The navbar is fixed as a panel on the left side of the panel on desktop mode, and is collapsible triggered through a button on mobile and tablet. If a user is logged in and a session user is available, the full gambit of pages will be available to view and click (Dashboard - Stacks - Reviews - Challenges - User profile - Log out). If a session user is not found, only 'Register' and 'Login' will be available. The navbar also runs along top on with the main logo for the website visible.

![Feature 5](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-5.PNG)

*User stories covered by this feature:*

21. As a site owner, I want users to be able to navigate the website easily so that users are more likely to have an enjoyable experience and return to use the website.
5. As a first-time user, I want to be able to log out easily so that I can come back to populating my account at a later date.


**Feature 6: Footer**

The footer is rather plain and doesn't change much from desktop to tablet and mobile view. I designed it to be plain to not distract from the main navigable elements on the page, especially as the design of the pages were largely modular in nature. The same footer is available on all pages apart from the original home page before users are registered/logged in.

![Feature 6](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-6.PNG)

*User stories covered by this feature:*

10. As a regular visitor, I want to be able to give feedback to improve the website over time.
21. As a site owner, I want users to be able to navigate the website easily so that users are more likely to have an enjoyable experience and return to use the website.


**Feature 7: Add books**

The 'Add books' page is available through either clicking the 'Add new book' button the Dashboard or Stacks page. This is a form which collects data such as book title, book author, ISBN, whether the book is read or not and sends it to a document in the 'books' collection in the database. If the book is marked as 'Read' by the switch button, a form input will appear asking for a book review. The data inputted into this element will be sent to a document in the 'reviews' collection of the database. 

![Feature 7](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-7.PNG)

*User stories covered by this feature:*

13. As a regular visitor, I want to be able to change a book from 'read' to 'unread' and vice versa easily. 
14. As a regular vivistor, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
15. As a regular visitor, I want to easily be able to edit or delete the books I have marked as read or unread.
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.

**Feature 8: Edit books**

The 'Edit books' page is available by clicking on an associated 'Edit' button associated whenever book data is displayed back to the user. It will render a form to edit pre-populated data associated with that document in particular. Users are also able to delete a book from this book, though they are discouraged from doing so by the use of the 'danger' color of red on the button.

![Feature 8](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-8.PNG)

*User stories covered by this feature:*

13. As a regular visitor, I want to be able to change a book from 'read' to 'unread' and vice versa easily. 
14. As a regular vivistor, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
15. As a regular visitor, I want to easily be able to edit or delete the books I have marked as read or unread.
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.

**Feature 9: Stacks page**

The 'Stacks' page displayed all of the books a user has added to the database. In my original design for this page (available in the wireframes) the page was divided by two cards, one for Unread books and one for Read. However, this became too complex to implement with the time scales and jinja templating limitations due to all of the data coming from the same collection within the database, making repeated iterations difficult. Instead, a description accompanies the books to tell the user which stack they belong to. Stacks work like shelves do in a website such as Goodreads, they're a format to categorise objects. Users can also edit individual books from this page.

![Feature 9](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-9.PNG)

*User stories covered by this feature:*

8. As a regular visitor, I want to be able to see which book I should read next to guide my reading practices.
21. As a site owner, I want users to be able to navigate the website easily so that users are more likely to have an enjoyable experience and return to use the website.
15. As a regular visitor, I want to easily be able to edit or delete the books I have marked as read or unread.
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.

**Feature 10: Reviews page**

The 'Reviews' page displays all of the reviews a user has added to the database. Again like with this other pages, a user can be redirected to edit individual reviews they leave, or add new reviews.

![Feature 10](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-10.PNG)

*User stories covered by this feature:*

12. As a regular visitor, I want to be able to keep track of my thoughts and feelings about the books I read. 
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.

**Feature 11: Add reviews**

Users are able to add new reviews through a form. It takes the data of book title, book author and book review. 

![Feature 11](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-11.PNG)

*User stories covered by this feature:*

17. As a regular visitor, I want to easily be able to edit or delete the reviews I have added. 
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.

**Feature 12: Edit reviews**

Users are able to edit individual reviews by clicking the associated 'edit' button whenever the review is displayed back to the user. The form is mostly pre-populated (with the exception of the textarea element) and users also have the ability to delete the review if they wish. 

![Feature 12](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-12.PNG)

*User stories covered by this feature:*

17. As a regular visitor, I want to easily be able to edit or delete the reviews I have added. 
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.

**Feature 13: Challenges page**

Users are able to view all of the challenges they've added and add new challenges by clicking the '+' sign on the card or clicking the 'edit' button associated with each challenge. In future versions of the website, I would like to add the ability for the user to clickly click 'Challenge complete' directly on this page and not have to go through the Edit challenge page to mark the challenge as achieved. If a challenge is marked as complete, that information will be displayed to the user.

![Feature 13](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-13.PNG)

*User stories covered by this feature:*

9. As a regular visitor, I want to challenge myself to fulfill reading goals I set for myself.


**Feature 14: Edit challenges**

Users are able to edit individual challenges by clicking the associated 'edit' button whenever the challenge is displayed back to the user. The form is pre-populated with the existing data and users also have the ability to delete the challenge if they wish. The main purpose of this page is to allow users to mark the challenge as completed, see above for future feature preference for this method.

![Feature 14](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-14.PNG)

*User stories covered by this feature:*

9. As a regular visitor, I want to challenge myself to fulfill reading goals I set for myself.
14. As a regular vivistor, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
16. As a regular visitor, I want to easily be able to edit or delete the challenges I have set for myself, or make them as complete.

**Feature 15: Add challenges**

Users are able to add new challenges through a form. It takes the data of challenge name. I purposefully left out whether users can mark this challenge as already completed or not as I wanted users to really challenge themselves and only add goals they have not already achieved.

![Feature 15](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-15.PNG)

*User stories covered by this feature:*

9. As a regular visitor, I want to challenge myself to fulfill reading goals I set for myself.
14. As a regular visitor, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
16. As a regular visitor, I want to easily be able to edit or delete the challenges I have set for myself, or make them as complete.

**Feature 16: User profile**

This page allows users to see their username, how many books they have read and how many they have yet to read. I decided to add this information in here as it was difficult for the users to get a sense of how many books are in associated with their account just by viewing them all together on the Stacks page. It also gives users a sense of where their reading habits are in terms of whether they're primarily reading or planning to read. Users can also see the profile picture that they uploaded when they created their account. Users can edit or delete their accounts from this page also. To edit their profile, a user only has to press the 'Edit account' button and a form will drop down.

![Feature 16](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-16.PNG)

![Feature 16a](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-16a.PNG)

*User stories covered by this feature:*

3. As a first-time user, I want to be able to personalize my profile with some personal touches such as a profile picture associated with my account. 
14. As a regular visitor, I want clear feedback as to whether my data has been successfully changed/added/deleted at all touch points on the website.
18. As a regular visitor, I want the process of adding data such as book or reviews to be simple and easy enough so that I can easily do multiple within a session.
19. As a regular visitor, I want to easily be able to view my user information, edit it as necessary or delete it.


**Feature 17: Contact Us page**

This page is navigable from the footer on all pages (bar the home page). The form is fully functional and uses Email JS to send a message to the site owner (myself). The form is also validated with JavaScript to prevent users being able to submit a message without fully filled in input fields. The message is sent to my email address through the use of the EmailJS API (more information on APIs used in this project further down).

![Feature 17](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-17.PNG)

*User stories covered by this feature:*

10. As a regular visitor, I want to be able to give feedback to improve the website over time.
20. As a site owner, I want to be able to collect feedback from users in a simple and easy way that I can iterate versions of the website based on an informed understanding of user needs. 

**Feature 18: 404 Error page**

This page displays when a user enters a URL that does not exist. The main purpose of this page is to let users know that an error has occurred and to redirect them back to the website. The design of this page is simple as I want users to return the main pages of the site as soon as possible upon seeing this page. 

![Feature 18](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/features/feature-18.PNG)

*User stories covered by this feature:*

6. As a first-time user, I want the website to direct me back home if I trigger a 404 error through a bad link.

### Future Features

The following features are features I would like to implement in future iterations of the website. They are by no means extensive, and any future versions would be in consultation with user needs through collected feedback. 

1. More visual and better designed flash messages - Whenever data is added, editted or removed from the database, flash messages are displayed to the users. These flash messages are currently displayed to the user at the top of the page in big, bold red writing. There are lots of design opportunities to improve upon this. 
2. Seperated cards on the Stacks page - Greater separation between 'read' and 'unread' books on the Stacks page (see earlier Feature profile for details on original design vs current design)
3. Ability to create new 'Stacks' - This concept was the original reason for pursuing the 'Bookstack' idea. In future versions, users will be able to create any stack they want and fully customize the organisation & presentation of their books.
4. Ability to mark challenges are complete from the Dashboard/Challenges page - Currently users have to click the 'Edit' button associated with individual challenges to render a 'Edit challenge' page then mark challenge as complete. In future versions, users will be able to mark the challenge as read alongside the 'Edit' button where challenges appears. 
5. Ability to pick which challenges and books appear on Dashboard - Currently the first unread book added to the database and the last challenge added to the database are displayed on the user's Dashboard. In future versions, users will be able to determine which book and challenge will be featured there. 
6. Data stored in relational database - although outside of the scope of the project goals in the timeframes given, in an ideal world this project's data would be stored within a relational database. This would give the project much greater ability to cross-populate data through the use of foreign & primary keys and inform users of interesting reading insights.
7. Search function - A nice-to-have feature would be for users to have a search engine that they could either (a) search for data they have added or (b) search for books held in APIs such as Open Library or Google Books to be add books directly without having to input all of the data fields manually. 
8. User profile picture used on Dashboard - In future versions, users will be able to see a small avatar of their profile picture in the top right of the page on the Dashboard where they can be redirected to their user profile if clicked.


## Design

My overall approach to the design of the website was so create a SaSS or webapp style that was contemporary in layout but classic in it's overall Look and Feel. 

I was heavily inspired by webapps such as Coinbase and Heroku with their clean, minimalist and modular way of designing web pages. 

**Color scheme**

I chose to stick with earthy colors to mimic the feel of old libraries and nostalgic memories of schools. I also wanted to bring in natural colors to create a sense of calm/peace that would invite the user to come back again and again. The primary colors used are green, brown, black and white. 

**Typography**

Sticking with the classic look & feel, I chose a serif font, Merriweather, for the header font. I chose this font because I thought it brought a gravitas and traditional feel to the look of the website. 

For body font, I chose to stick with the default Segoe that comes with Materialize CSS because it's readily available on almost all devices and I wanted a simple sans-serif font to balance against the header font.

**Imagery**

The only image used on the website that is not user-generated is the illustration of the girl reading a picture (see Credits for credits). I chose this illustration because I thought it gave the feeling of cosiness and was inviting to the user. I chose the illustration style for the same reason. The other imagery used on the website is generated one of two ways: (a) a profile picture uploaded to AWS S3 Bucket by the user and displayed back to the user on their user profile page and (b) book covers retrieved by the user-inputted ISBN number ran through the Open Covers API. I felt it important for book covers to be attached to book data to give the pages a more visual element. If a book cover cannot be generated by the API/ISBN, the design continues without it and nothing is generated in its place. I discovered this was difficult to avoid because according to the codebase a source would technically be found, thought it would be a blank 1x1 image.

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

![New database model](https://github.com/TaraRhoseyn/CI_MS3_Bookstack/blob/main/bookstack/static/docs/readme/new_database_model.PNG)

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
- [Open Library Covers API](https://openlibrary.org/dev/docs/api/covers) - For retrieving the images of book covers based on the book's ISBN inputted by users.
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
