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
    - [**Remote Deployment**](#remote-deployment)

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
    - Flask is a micro framework that I've used to render the back-end Python with the front-end Materialize.

#### Icons

- [Font Awesome 5.11.2](https://fontawesome.com/) 
  - I only used icons for home and social networks.

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
- On the **books** page above books is a search bar that uses users query to search books by author name, book name or genre. Trying to make it case insensitive resulted in a bug and becouse of lack of time, the search bar is case sensitive.

**Add a Book**
- [**C**RUD] Create or 'add' a new book. Defensive programming in place means users must adhere to minimal requirements when adding a new book. 

**View a Book**
- [C**R**UD] Read or 'review' books can be achieved by clicking on book image on books page. It is also possible to share a link to book via the share icon and modal. 

**Update a Book**
- [CR**U**D] Update or 'edit' book information.

**Delete a Book**
- [CRU**D**] Delete or 'remove' a book from the website and database.


### Features Left to Implement

Becouse of lack of time for finnishing this project some requirements were not completed.

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