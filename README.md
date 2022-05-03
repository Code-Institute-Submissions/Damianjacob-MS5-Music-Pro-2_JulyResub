# MS5-Music-Pro-2

See deployed site here: 

## Table of Contents

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## A forum for bakers and bread enthusiasts


## Project Goals
The goals for this project are:

<!-- - Creating a forum where users can talk and discuss about baking
- Users can sign up and log in to take advantage of the main features
- Users can create, update and delete their posts. They can also engage with posts of other users by liking them and commenting. -->

My own goals for this project are:
<!-- - Creating a user-friendly and simple application
- Improving my skills of web development, especially regarding frameworks(Django), back-end development and python. -->

## User Goals
<!-- - Find information or recipes about baking
- Discuss bakery-related things with other users
- Share recipes, pictures or advice with other users -->

## Site Owner Goals
<!-- - Keep the site friendly and secure by having access to the admin panel, where it's possible to delete posts, comments and users should it be necessary. -->

## User Stories

### Epic 1: 
1. As a first time user I want to see the most important information on the main site so that I know what services it offers.
2. As a user I want to browse through different products so that I can decide which one to buy.
3. As a user I want to be able to order the products by different criteria so that I can find the one I'm looking for.
4. As a user I want to be able to search for keywords so that I can find any product related to that keyword.
5. As a user I want to see more information about a product when I click on it so that I can know more.
6. As a user I want to be able to buy a product without registering to the site.
7. As a customer, I want to receive confirmation that my payment has gone through, or an error message if it hasn't.
8. As a user I want to be redirected to a sign in page if I click on any links or buttons that require me to be logged in.
9. As a use I want to receive feedback on my actions so that I know whether they have been executed correctly.
10. As a User I want to be able to sign up so that I can get access to functions restricted to registered users.
11. As a registered user, I want to save my delivery information so that the delivery form gets filled automatically.
12. As a registered user, I want to be able to see all the orders I did in the past.
13. As a registered user I want to be able to change my default delivery information.
14. As a registered user, I want to be able to rate a product I have bought to express how happy I was with it.
15. As a registered user, I want to be able to ask questions about a product.
16. As the site owner, I want to be able to create, delete and update products.
17. As the site owner, I want to be able to answer questions and comments from my customers.
18. As the site owner, I want to have access to an admin panel, so that I can delete inappropriate comments and users.



<!-- ### Epic 2: 
4. As a user I want to get redirected to the sign in/sign up page if I click on any links or buttons that require me to be logged in so that I can sign in or sign up easily.
5. As a user I want to get feedback from the site on the actions I have performed so that I can see whether my action was carried out correctly or not.
6. As a user I want to be able to get back to the home page in one click so that I can navigate the site easily.
### Epic 3: Authentication and permission
7. As a user I want to sign up and log in so that I can perform actions reserved for registered users.
8. As a registered user I want to be able to log out so that I have more security.
9. As a registered user I want to be able to create posts so that I can share my recipes, tutorials or advice with other users.
10. As a registered user I want to like posts so that I can express my preferences for certain posts.
11. As a registered user I want to leave comments under posts so that I can discuss topics with other users.
13. As a registered user I want to be able to edit my posts so that I can correct mistakes easily if they happen.
14. As a registered user I want to be able to remove my posts so that I can delete them if I don't like them anymore.
### Epic 4: Admin
15. As a site admin I want to be able to access the admin page so that I can monitor posts and comments and remove them if they are inappropriate. -->

## Design Choices
<!-- My goal was to create a simple site with a clean look. I have opted for two warm primary colors, to create a welcoming atmosphere. The brown and gold colors should remind of the colors of bread (crust and inside). -->

### Color palette
<!-- ![]() -->

### Wireframes
I used balsamiq for the wireframes. The final wireframe is a bit different from the first version, as i made some changes while creating the project, in accordance with Agile principles.
<details>
<summary>Wireframes for mobile</summary>
<img src='assets/images/wireframes/wf-mobile-mp2' alt='mobile wireframe'>
</details>

<details>
<summary>Wireframes for tablet</summary>
<img src='assets/images/wireframes/wf-tablet-mp2' alt='tablet wireframe'>
</details>

<details>
<summary>Wireframes for desktop</summary>
<img src='assets/images/wireframes/wf-desktop-mp2' alt='desktop wireframe'>
</details>

## Structure
### Code directories
Music Pro was created with the Django framework, so it is divided into apps:
- breadit is the main app, where settings.py can be found

Other directories:
- static: This is where the custom CSS and JavaScript files for this project are stored.
- templates: This is where all the templates (html files) are stored, as is usual with Django.
- docs: in this directory I stored all the images and screenshots needed for this Readme file.

### Database
<!-- This website relies heavily on a databse. I used postgreSQL as database both for development and for the deployed version. -->

### Data Models
<!-- Data Models are a central part of this project. There are three data models I used:

- User: This is a built-in data model that comes with Django. It is used for authentication and authorisation.
- Post: This is my own data model, used for all the posts you see on my site.
- Comment: This is another data model I created. I drew a lot of inspiration for this model from CodeInstitute's Django walkthrough project, which has a similar model. -->

### Data Model scheme
<img src="" alt="database schema">

This scheme was made with Lucidchart.

## Features 

### Navbar

<!-- The navbar is sticky and thus offers a quick and easy way to return to the Homepage, wherever the user is in the page.
For users that are logged out, it will display the option to sign up or log in, and for users who are already logged in it will display their username (so they know that they are logged in) and if they are a superuser or staff member they will see a link to the admin panel. -->

<details>
<summary>Navbar when not logged in</summary>
<img src='' alt='Navbar screenshot'>
</details>
<details>
<summary>Navbar when logged in (user has admin or staff privilege)</summary>
<img src='' alt='Navbar screenshot'>
</details>

<!-- User stories covered:
- 6. As a user I want to be able to get back to the home page in one click so that I can navigate the site easily. -->

### Home Page

<!-- The home page is the central part of Breadit: this is where all the posts are displayed (the latest posts are displayed on top) and where the user can see more information about them.
From here the user can scroll through the posts and click on the ones they like. Information about the posts is visible from the home page, like the user who created the post, publication date, number of likes and number of comments.
The user can also decide to add their own post to the site, but they need to be logged in to do that. -->
<details>
<summary>Home page</summary>
<img src='' alt='home page screenshot'>
</details>

<!-- User stories covered:
- 1. As a user I want to see all the breadit posts on the main page so that I can scroll through them.
- 3. As a user I want to see likes, user and number of comments of a post without first having to click on it so that I can decide which posts are most relevant to me.
- 8. As a registered user I want to be able to log out so that I have more security. -->

### User log in and sign up
<!-- These are the forms used to sign the user up or log them in. If an anonymous user tries to access a forbidden view, they will be redirected to the login page. -->
<details>
<summary>Log in</summary>
<img src='' alt='log in screenshot'>
</details>

<details>
<summary>Sign up</summary>
<img src='' alt='sign up screenshot'>
</details>
<!-- 
User stories covered:
- 4. As a user I want to get redirected to the sign in/sign up page if I click on any links or buttons that require me to be logged in so that I can sign in or sign up easily.
- 7. As a user I want to sign up and log in so that I can perform actions reserved for registered users. -->

<!-- 
### Post Detail page
This is where the users can see more details about a post. The full lenght of the post text can be seen here, and the comments and likes as well. The user can also like a post if they are signed in. -->
<details>
<summary>Post detail</summary>
<img src='' alt='post detail screenshot'>
</details>

<!-- User stories covered:
- 10. As a registered user I want to like posts so that I can express my preferences for certain posts.
- 13. As a registered user I want to be able to edit my posts so that I can correct mistakes easily if they happen.
- 14. As a registered user I want to be able to remove my posts so that I can delete them if I don't like them anymore. -->

<!-- ### Leaving Comments
This is where registered users can leave a comment.
<details>
<summary>Comments</summary>
<img src='https://github.com/Damianjacob/MS4_breadit/blob/main/breadit/docs/features/post-detail2.png' alt='comment screenshot'>
</details> -->

<!-- User stories covered:
- 11. As a registered user I want to leave comments under posts so that I can discuss topics with other users. -->

## Technologies used
The primary technology used here was the Django framework
### Languages
- HTML5 for building the web pages
- CSS3 for styling the web pages (although I used mainly Bootstrap 5)
- JavaScript for validating the media input field 
- Python 3 for the backend programming and database manipulation

### Other technologies
Apart from the programming languages, I have used the following:

- [Heroku](https://www.heroku.com/) for deploying and hosting my site.
- [Git](https://git-scm.com/) and [GitHub](https://github.com/) for version control and storage of my code 
- [Cloudinary](https://cloudinary.com/) for hosting the image files
- [postgreSQL](https://www.postgresql.org/) as a database
- [Balsamiq Wireframes](https://balsamiq.com/) for creating my wireframes
- [Lucidchart](https://www.lucidchart.com/pages/de) for creating the data schema for my models
- [Font Awesome](https://fontawesome.com/) - All icons are from Font Awesome
- [Google Fonts](https://fonts.google.com/) - I used the Roboto and Open Sans fonts from Google Fonts
- [VSCode](https://code.visualstudio.com/) - The code editor where I wrote all my code.

## Testing

### HTML
No errors were returned when passing through the official [W3C validator](https://validator.w3.org/).
Please see the screenshots for HTML here: [HTML validation](https://github.com/Damianjacob/MS4_breadit/tree/main/breadit/docs/validation/html-validation) .

### CSS
No errors were found when passing through the [Jigsaw validator](https://jigsaw.w3.org/css-validator/).
<img src="">

### Python
All my Python documents passed through the PEP8 validator without any errors. The result was the following for all of them.
<img src="">

### JavaScript
My JavaScript file passed through the JSHint validation without any errors.
<img src="">

### LIGHTHOUSE
<!-- All of the pages in this site have achieved a total score of at least 89 in Google Lighthouse (for performance, accessibility, SEO and best practices.) -->
You can see the results [here]().

### Devices
<!-- The testing was done on a Mac Mini and iPhone. I tested Google Chrome and Safari, and the site was functional and responsive for all devices (I used the list of devices available in the web inspector). -->

## Bugs

- While trying to run the server after having set up Amazon S3 as default file storage, I had issues accessing my admin page. It raised "ValueError: Required parameter name not set" and pointed to the Django static tag where the CSS link was defined. 
Fix: In settings.py I deleted the STATICFILES_STORAGE variable (which I had set to the boto link, needed for AWS) and only left DEFAULT_FILE_STORAGE. This resolved the issue.

## Deployment

### Creating the Github repository and cloning it
- Go to Github to your profile
- Go to repositories and click on "New"
- Choose a name and the settings you prefer, then click on "create repository"
- Go to the repository
- Click on "code", and copy the HTTPS address
- In VSCode, click on "Clone Git repository"
- Paste the address of your repository and press enter. 

### Deploying to Heroku
- Create account at Heroku
- Create new app, give it a name and select your region
- Go to Settings
- Under Config Vars add your secret data (for example environment variables like API keys)
- Add Heroku Postgres Add-on
- In the deployment tab, select the preferred deployment method (I chose Github)
- Connect your app to your GitHub repository
- Enable automatic deploys
- For any issues it's useful to consult the build log in the activity tab
- Before going public, it's very important to set DEBUG to false in the django settings.py file.


## Credits

### Tutorials and other resources

I have used the [Django Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/) and read the Django documentation extensively during the creation of this project.

Tutorial followed to use AWS for file storage: https://www.section.io/engineering-education/using-amazon-web-service-for-django-media-files-storage/#setting-up-the-django-application

Documentation for using AWS' S3 service with the django-storage library : https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html