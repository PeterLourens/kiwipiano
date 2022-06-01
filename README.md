# Kiwi Piano Studio

Kiwi Piano website targets the user who wants to learn to play piano, or wants to play music piece on a grand piano, or wants to make a recording, or wants to practice for music competition, or wants to perform a piano virtual recital, or simply enjoys a play in a small concert-like environment. 

The website provides different user interface. User can register an account, login to the user’s account, log out from the account, edit profile or delete account, book or cancel a session. Admin user can manange the site's data. 

## Table of Content

# UX

## User Stories

* ### Admin CRUD / Super User
  * [#1]() As an **admin** I can **navigate the admin panel** so that **I can create, read, update and delete the data on the site.**
  * [#2]() As an **admin** I can **use the admin privilege** so that **I can filter out and approve the comments that user wants to post on site.**

* ### New and unregistered User
  * [#3]() As a **first time user** I can **access the site easily** so that **I can view the site on any media screens with different browsers.**
  * [#4]() As a **first time user** I can **navigate the site easily** so that **I know what the site is about and decide if I am interested or not.**
  * [#5]() As a **user** I can **view the lesson details** so that **I can choose a lesson that it is suitable for me**.
  * [#6]() As a **user** I can **view the lesson schedule** so that **I can book a lesson available to fit into my own schedule**.
  * [#7]() As a **user** I can **sign up an account** so that **I can manage my activities with the studio.**

* ### Registered User
  * [#8]() As a **registered user** I can **login / logout** so that **I can book or cancel a lesson as well as managing my own account profile.**
  * [#9]() As a **registered user** I can **book a lesson** so that **I can select a lesson suitable for me.**
  * [#10]() As a **registered user** I can **cancel a booking** so that **I can manage my schedule in case I am not available**.
  * [#11]() As a **user** I can **receive feedback** so that **I know whether my registration is successful or not as well as my booking status**.
  * [#12]() As a **register user** I can **view my booking history** so that **I have a clear view about my study**.
  * [#13]() As a **registered user** I can **post a review** so that **I can share my opinion about my experience with the studio**.
  * [#14]() As a **user** I can **contact the studio** so that **I can ask any questions regarding my bookings or other things**.
  * [#15]() As a **registered user** I can **edit my profile** so that **I can edit and manage my own account as I wish**.

[Back to top](#kiwi-piano-studio)

## Site Owner Stories

* The website is accessible and responsive. It targets the user who would like to learn to play piano or other activities using the studio.

* The site offers different user interface that user can sign up an account, log in and log out as well as edit the user profile. 

* The site has a booking system that user can book a piano session according to user’s interests.

* The site offers user a platform that user can create and post a review about their experience with the piano studio. 

* The site offers many different contact methods that user can make contact easily to the piano studio.

* The site has an admin functionality that admin can manage the site.

[Back to top](#kiwi-piano-studio)

## Wireframes

I used Balsamiq to create the project’s wireframes that displays an overview of how the site looks like. However, the end result might be slightly different than the initial design due to the development of the project. 

## Agile Project Management

## Data Model

## Design

### Color Scheme

The site uses white color for the background and black color for the text. The bright colors are used for the buttons and links.

* Color source image
  <details><summary>The color theme was extracted from this image.</summary>

  ![Image](media/images/piano4.jpg)

  </detials>

* Colors for the site

![Color Theme](media/readme-pics/colortheme.png)

* Color contrast grid
  
![Color contrast grid](media/readme-pics/contrast-grid.png)

[Back to top](#kiwi-piano-studio)

### Typography

## Database ERD

# Exsiting Features

## Home Page

## About Page

## Offers Page

## Contact Page

## Reviews Page

## Sign Up Page

## Login Page

## Sign Up Confirmation Page

## Bookings Page

## Future Development

# Technologies Used

* [HTML5]()
* [CSS]() 
* [JavaScript]() 
* [Python]() 

* [Bootstrap]() - used to style the websie.
* [Django]() - used to create the project.
* [Heroku]() - used to deploy and host the project's live site.
* [Heroku]() PostgreSQL - used to connect the project to the database.
* [Cloudinary]() - used to store project's static and media files.
* [Summernote]() - used to add the editor with full feature.
  
* [GitHub]() - used to host the project's code and make deployment.
* [GitPod]() - used to write the code for the project.
* [Balsamiq]() - used to create project's wireframes.
* [Chrome Dev Tools]() - used to debug and light house testing.
* [Am I Responsive]() - used to generate the responsive preview screens.
* [Responsive Design Checker]() - used to check responsiveness.
* [Lucidchart]() - used to create the database ER diagram.
* [Font Awesome]() - used to download the icons.
* [Google Fonts]() - used to style the text.
* [JSHint]() - used to validate the JavaScript code.
* [Pep8]() - used to validate the Python code.
* [W3C Markup Validation Service]() - used to validate the HTML code.
* [W3C CSS Validation Service]() - used to validate CSS code.
* [Compressor.io]() - used to compress the images and screenshots.

# Testing

## Code Validation

## Responsiveness Test

## Browser Compatibility Test

## Automated Tests

## Light House Test

## Manual Test

## Resolved Known Bugs

## User Story Test

## Bugs

# Deployment

1. I used Code Institute GitPod full template to set up an environment to created the project. Installed ```Django``` and required packages / libraries using commands in GitPod terminal. Created a project named ```kiwipiano``` and connected the project to use ```Cloudinary``` and ```PostgreSQL```.

2. Logged in to Heroku account and created an app named kiwipiano.
Attached the database to the app and set up the Config vars.

3. Created ```env.py``` file and ```Procfile```, updated ```settings.py``` file and then made migrations to the database for all the changes.

4. Commands to deploy ```kiwipiano``` project in GitPod terminal:
   
    * ```heroku login -i``` ---login to my Heroku account.
    * ```heroku apps``` ---get the names of Heroku apps.
    * ```heroku git:remote -a kiwipiano``` ---set the Heroku remote.
    * ```git add . && git commit -m "Deploy project to Heroku via CLI."``` ---add and commit.
    * ```git push origin main``` ---push to GitHub repository.
    * ```git push heroku main```---push to Heroku.

5. Deployment successful. Here is the site's URL: https://kiwipiano.herokuapp.com/
   
   ![Kiwi Piano](media/readme-pics/deployment-heroku.png)

[Back to top](#kiwi-piano-studio)

# Credits

## Content

## Media

## Code

# Acknowledgement