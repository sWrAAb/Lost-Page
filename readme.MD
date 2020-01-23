<h1 align="center">The Lost Page</h1>
<h2 align="center"> Bookworm's last resort</h2>

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Heroku Deployment**](#heroku-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

## UX

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, specifically the **Data Centric Development** module. The objective for this milestone project is to "*Create a web application that allows users to upload details of books, including book name, author name, link to cover image and any other relevant fields.*", using the **CRUD** operations of **C**reate, **R**ead, **U**pdate, and **D**elete for their books.
Users can also search for books that contain searched word or letter in author's name, title or genre. <br><br>The Lost Page can be viewed https://the-lost-page.herokuapp.com.
<br><br>
The Website is fully responsive and uses Mongo DB to hold book collection.
Some books in collection are my personal favorites so feel free to add your favorite books.<br>
By clicking on the share link modal is shown with an option to copy link of the book.

"**_As a user, I would like to_**:"

- *view the website* from **any device** *(mobile, tablet, desktop)*
- *search for books by* **book name**, **author name** or **genre**
- *add* my **own favorite book**
- *view* **book details**
- *edit* **book information**
- *delete* **book** from database
- **share** a *particular book*
- *buy* **book online**

### Design

The Lost Page was designed to be simple and presentable using book images as links to book information page.

#### Framework

- [Bootstrap 4.4.1](https://getbootstrap.com/)
    - I really like Bootstrap as a framework with great number of components and  its simple-to-understand documentation.
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
    - In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Flask 1.1.1](http://flask.pocoo.org/)
    - Flask is a microframework that I've used to render the back-end Python with the front-end Bootstrap 4.

#### Icons

- [Font Awesome 5.11.2](https://fontawesome.com/) 
  - I only used icons for home, social networks, share icon and copy for modal.

#### Typography

- I have incorporated two of [Google Fonts](https://fonts.google.com/) throughout the entire application. The font I have selected for page titles is
[Indie Flower](https://fonts.google.com/specimen/Indie+Flower) and [Roboto](https://fonts.google.com/specimen/Roboto) for rest of the text.

### Wireframes

- For my wireframes, I have used [Mockflow](https://mockflow.com/)
- Images can be viewed in my [Wireframe](https://github.com/sWrAAb/Lost-Page/tree/master/static/images/Wireframes) folder


##### back to [top](#table-of-contents)

---

## Features

### Existing Features

**View All Books**
- On the *books* page, all books are initially displayed in order of adding.

**Search Books**
- On the **books** page above books is a search bar that uses users query to search books by author name, book name or genre. Trying to make it case insensitive resulted in a error and becouse of lack of time, the search bar is case sensitive.

**Add a Book**
- [**C**RUD] Create or 'add' a new book. Defensive programming in place means users must adhere to minimal requirements when adding a new book. 

**View a Book**
- [C**R**UD] Read or 'review' books can be achieved by clicking on book image on books page. It is also possible to share a link to book via the share icon and modal. 

**Update a Book**
- [CR**U**D] Update or 'edit' book information.  

**Delete a Book**
- [CRU**D**] Delete or 'remove' a book from the website and database. Deletion requires confirmation in the form of modal.


### Features Left to Implement

Because of lack of time for finishing this project some requirements were not completed.

**Pagination**
- At this time all books are displayed on a single page. It works now but might take long time to load when more books are added.

**Comment and upvote section**
- In the future will be added on view book page for users to share information about books.

**User account** 
- Password protected account will be added with a feature of saving books to favorites and shopcart.

**Dynamic search bar**
- Toggle buttons for categories will be added and they will display books from selected genres on the books page. 

##### back to [top](#table-of-contents)

---

## Technologies Used

- [VS Code](https://code.visualstudio.com/) - Used as my primary IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code online.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- [Bootstrap 4.4.1](https://getbootstrap.com/) - Used as the overall design framework.


### Back-End Technologies

- **Flask**
    - [Flask 1.1.1](http://flask.pocoo.org/) - Used as a microframework.
    - [Jinja2 2.10.3](http://jinja.pocoo.org/docs/2.10/) - Used for templating with Flask.
    - [Werkzeug  0.16.0](https://werkzeug.palletsprojects.com/en/0.16.x/) - Used for password hashing, authentication, and authorization.
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
- **Python**    
    - [Python 3.7.1](https://www.python.org/) - Used as the back-end programming language.
    - [MongoDB Atlas](https://www.mongodb.com/) - Used to store my database in the 'cloud'.
    - [PyMongo 3.10.0](https://api.mongodb.com/python/current/) - Used as the Python API for MongoDB.

##### back to [top](#table-of-contents)

## Testing

Testing information can be found in separate [testing.md]() file



### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - Unfortunately the W3C Validator for HTML does not understand the Jinja templating syntax, so it therefore shows a lot of errors with regards to `{{ variables }}`, `{% for %} {% endfor %}`, etc. Aside from the Jinja warnings and errors, all of the remaining code is perfectly validating. 

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Did not show any problems


**JavaScript**
- [JShint](https://jshint.com/) - 
    - There are 3 functions in this file.
    - Function with the largest signature take 0 arguments, while the median is 0.
    -  Largest function has 3 statements in it, while the median is 3.
    - The most complex function has a cyclomatic complexity value of 1 while the median is 1.
    - Undefined variable $ for jQuery 6 times
**Python**
- [PEP8 Online](http://pep8online.com/)
    - My `.py` file returns 2 errors
    - E127 continuation line over-indented for visual indent
    - E128 continuation line under-indented for visual indent

### Compatibility

To ensure a broad range of users can successfully use this site, I tested it on major browsers in both desktop and mobile configuration.

- Chrome 
- Edge 
- Firefox 
- Opera 
- Internet Explorer

[Autoprefixer](https://autoprefixer.github.io) was used for parsing CSS and adding vendor prefixes

### Known Issues

- Search bar is case sensitive at this time so words need to be capitalized 
- If no image was added to book, on books page alternative image is added, however I could not make it fit on book details in time. Instead there is blank space with text added in html alt="".
- Edit book information modal does not display description. Textarea returns empty every time.



##### back to [top](#table-of-contents)

### Local Deployment

In order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- Any IDE such as [Microsoft Visual Studio Code](https://code.visualstudio.com).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [MongoDB](https://www.mongodb.com) to develop your own database either locally or remotely on MongoDB Atlas.


### Instructions

1. Save a copy of the github repository located at https://github.com/sWrAAb/Lost-Page by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/sWrAAb/Lost-Page
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter.<br> To create virtual environment enter the command:
```
python -m .venv venv
```  

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.flaskenv`.

7. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database.

8. You can now run the application with the command
```
python app.py
```

9. You can visit the website at `http://127.0.0.1:5000`

## Heroku Deployment

To deploy The Lost Page to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
MONGO_URI | `<your_uri>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

##### back to [top](#table-of-contents)

## Credits

### Content

Books and descriptions were linked from various websites such as:

- [Goodreads](https://www.goodreads.com/)
- [Wikipedia](https://en.wikipedia.org/wiki/Main_Page)

### Media

#### Logo

Logo was made on [Freelogodesign](https://www.freelogodesign.org/)

#### Images

All images except logo and image that is shown when no cover image is selected are linked with url.

### Code

- Template code was taken from [Bootstrap](https://getbootstrap.com) and [W3Schools](https://www.w3schools.com)
- CSS code from [CSS Tricks](https://css-tricks.com)
- Python code from Code Institute lessons
- Search bar, show total books in navbar and show alternate image when no cover image was added from [RealPython](https://realpython.com)

### Acknowledgements

- To my mentor, Spencer Barriball, for incredible mentoring, support and for assisting during my project reviews with great insight.

##### back to [top](#table-of-contents)