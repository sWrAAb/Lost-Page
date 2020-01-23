[Readme file](https://github.com/sWrAAb/Lost-Page/blob/master/readme.MD)

[Heroku Live - The Lost Page](http://the-lost-page.herokuapp.com)

### Python testing

Some of the functions of the app.py file were tested using unittest.
Because of testing complexity and lack of time only 5 functions were tested.
They can be found in [test.py](https://github.com/sWrAAb/Lost-Page/blob/master/test.py) file.

#### Testing instructions

To run tests use command:  python test.py

## UX Testing

- To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.

- The Lost Page navbar is laid out in the conventional way:

- Navbar is at the top of the screen.

- The logo on the far left of the navbar and links to the home page.

- The primary purpose of the site - the Books page - is easily found in the navbar.

- The footer is also laid out in a conventional way.

- Contact information and links are provided in the footer.

- Social media links also provided in the footer where the user would expect to find them.

- The information I am presented with to be laid out in a way that is easy for me to navigate, so that I find what I need quickly and efficiently.

- The page is broken up into easy to understand sections, and the data displayed in a way that is most easy to read.

- Tables and icons are used where applicable, which all aid in easily accessible information for the user.
- As a user accessing this site from a mobile phone or tablet, I want the site designed responsively so that it is still easy to navigate and use on my smaller devices. 

The Lost Page was carefully planned and designed to be responsive and work well on mobile, tablet and desktop devices.

## Manual Testing

Navbar

  - Tested on all screen sizes to confirm it is positioned correctly.
  - Tested on small screens to confirm dropdown menu appears.
  - Click the The Lost Page logo, confirm it takes the user to the home page.
  - Click the Home link, confirm it takes the user to the home page.
  - Click the Books link, confirm it takes the user to the books page and that displays correct total number of books.
  - Click the Add book link, confirm it takes the add book page where form is displayed.

Footer 
  - Tested on all screen sizes to confirm it is positioned correctly.
  - Clicked he The Lost Page logo, confirm it takes the user to the home page.
  - Tested social icons to confirm they redirect correctly and change color on hover.

Home page

- Tested on all screen sizes to confirm it is positioned correctly.
- Clicked on image to confirm it redirects to book page correctly.

Add book page

  - Form was tested to confirm it inputs data correctly. All form input is required except cover image.
  - Tested alternative cover image appears when no image was given.
  - Buttons were tested to confirm they submit information correctly, and return to book page.

Edit page

- Form was tested to confirm all book information is displayed correctly. For some reason description text input field returns empty every time.
- Buttons were tested to confirm they work as intended.

Books page

- Search bar was tested to confirm it works correctly. However it's case sensitive.
- All book images were tested to confirm they redirect to view book page.

View book 

- All books were tested to confirm they details page is displayed properly.
- When no image was added to book, no image is displayed only alternate text.
- Tested all buttons to confirm they do as they are told.
- Share button was tested to confirm it displays link to page correctly and it can be copied with click on the modal

Delete book
 - Buttons were tested to confirm modal is shown.
 - Buttons on modal were tested.
 - Database was inspected to confirm books were deleted.


