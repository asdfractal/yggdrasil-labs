# Yggdrasil Labs

Yggdrasil Labs is a cybernetics and bioware company providing implants and other transhuman upgrades. Site visitors can browse the range of products and add to their cart. Due to the nature of the business it is required to register before checking out, as it is possible a booking must be created. Also the business offers technical support to it's clients.

This is a full stack website developed for Code Institute milestone project 4. Since this website is for educational purposes, email verification is not required.
If you want to use the full functionality of this website, Stripe test payments are enabled with the card number `4242 4242 4242 4242` and any CVC, future expiry date, and postcode.

## Contents:
* [User Experience](#user-experience)
    * [Project Goals](#project-goals)
    * [Target Audience Goals](#target-audience-goals)
    * [Site Owner Goals](#site-owner-goals)
    * [User Stories](#user-stories)
    * [Requirements](#requirements)
    * [Expectations](#expectations)
* [Design Choices](#design-choices)
    * [Colours](#colours)
    * [Fonts](#fonts)
    * [Icons](#icons)
    * [Styles](#Styles)
    * [Images](#images)
    * [Wireframes](#wireframes)
    * [Code Styling](#code-styling)
* [Information Architecture](#information-architechture)
    * [Data models](#data-models)
        * [User](#user)
        * [Profiles App](#profiles-app)
            * [User Profile Model](#user-profile-model)
        * [Products App](#products-app)
            * [Product Model](#product-model)
            * [Category Model](#category-model)
        * [Checkout App](#checkout-app)
            * [Order Model](#order-model)
            * [OrderLineitem Model](#orderlineitem-model)
        * [Bookings App](#bookings-app)
            * [Booking Model](#booking-model)
        * [Reviews App](#reviews-app)
            * [Review Model](#review-model)
* [Features](#features)
    * [Implemented Features](#implemented-features)
    * [Planned Features](#planned-features)
    * [Extra Comments](#extra-comments)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries](#libraries)
    * [Tools](#tools)
* [Testing & Bugs](#testing--bugs)
* [Development & Deployment](#development--deployment)
    * [Local Development & Set-Up](#local-development--set-up)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)
    * [Image Credits](#image-credits)
* [Acknowledgements](#acknowledgements)
* [Disclaimer](#disclaimer)


## User Experience

### Project Goals
To offer users a service for purchasing and installing cybernetic implants. Users will be able to browse products, view detailed information and specifications, create an account, order products, book an appointment, post reviews and receive technical support.

### Target Audience Goals
* Browse various products including detailed product information
* Create an account to purchase items and track orders
* Book appointments and receive technical support
* Post reviews and feedback about the products and the service
* Intuitive and visually appealing website design
* Website can be used on all devices

### Site Owner Goals
* Create a platform to promote and provide the companies products and services
* Provide users with a platform to view what the company offers and opportunity to learn more
* Ensure the platform is secure for users to safely purchase the products and services
* Have a way to update users on new developments within the company

### User Stories
* As a shopper:
    * As a user, I want to view a list of products so that I can make a selection to purchase
    * As a user, I want to view detailed information about a product so that I can learn more about it before making a decision
    * As a user, I want to be able to ask questions so that I can learn more about it before making a decision
* As a site user:
    * As a user, I want to register for an account so that I can have a personal profile on the website
    * As a user, I want to personalise my profile so that I can save my information and keep track of orders
* As a client:
    * As a user, I want to easily purchase and book an appointment so that I can ensure everything will go smoothly
    * As a user, I want to receive technical support so that I can solve any issues
    * As a user, I want to leave a review so that I can inform other shoppers of my experience

#### Requirements
* View products in a list and with detailed product information
* Purchase the products using a secure checkout system
* Book an appointment for installing the product
* Create an account, view/update personal information and view previous orders
* Contact the business for further information and technical support

#### Expectations
* Website is visually appealing and easy to navigate on all devices
* User can leave a review of the business and product
* Personal information will be stored securely

## Design Choices
Due to the nature of this business' products, I have taken inspiration from the cyberpunk sci-fi culture, with a bit of influence from synthwave and vaporwave. However since it is a business providing a service, clients need to feel they are safe to proceed with the installation. The desired impression is to be reliable and professional, and to still stand out and make an impression. To achieve this I have chosen a colour and font theme with this in mind.

### Colours
The overwhelming colour aesthetic in the aformentioned inspirations are blues, purples and pinks on a dark backdrop. There is also an emphasis on neon style colours. With this in mind I have created this colour scheme.

![Colour Pallete](/wireframes/colour-palette.png).

* Primary colour - #00C2CE - This blue/green brings a nice contrast to the overall dark theme of the website, drawing attention where it is present
* Secondary colour - #D76EE5 - A slightly toned down neon pink/purple, complimenting the primary colour and highlighting elements
* Tertiary colour - #F22CA6 - A vibrant flower pink, to be used sparingly to add extra highlights
* Grey - #3D3D3D - A lighter shade of the dark grey
* Dark Grey - #1F1F1F - A dark grey not far off black

I am also using the following colours for message alerts
* Warning colour - #FC440F
* Error colour - #FF0033
* Success colour - #00FF00
* Info colour - #F2EA02

### Fonts
* Title/Logo - [Elianto](https://www.behance.net/gallery/33808280/Elianto-Free-Font) - A unique font used for the business title and logo
* Headers - [Orbitron](https://fonts.google.com/specimen/Orbitron) - This font is perfect for the desired feel of the website. Bold, solid, and professional with a unique character
* Body font - [Raleway](https://fonts.google.com/specimen/Raleway) - Easy to read and well spaced, compliments the display font

### Icons
I have used a range of font awesome icons across the website to aid in displaying content and navigation options instead of using only text.

### Styles
I have wanted to use scss for some time and this project I have decided to implement it for the first time. I have used [this](https://matthewelsom.com/blog/simple-scss-playbook.html) resource as a guide for the architechture. I am using the [BEM](http://getbem.com/) naming convention for my CSS classes to create modular, reusable components.

Note on CSS: I have chosen to use vw/vh on padding and margins in a lot of cases as I believe this allows for an even more responsive experience than using solely rem. My decision was influenced by my own experimentation as well as researching, particularly [this](https://www.elegantthemes.com/blog/divi-resources/better-mobile-website-design-how-to-use-vw-vh-and-rem-to-create-fluid-divi-pages) article.

#### Folder structure
* scss
    * abstracts - this is for variables, mixins, etc. and has no direct output
    * base - top of the document resets, utility classes, etc.
    * components - reusable components with general styles
    * layout - specific styles for individual pages or components

### Images
I created the logo and index page title using the Elianto Font. The rest of the images are taken from the internet and credited in the credits section of the readme.

### Wireframes
Using the program Pencil I designed wireframes for desktop and mobile/tablet. The mobile/tablet are combined because there will be minimal differences in the design. I used them as a blueprint and then adjusted based on further testing to reach the final design. The wireframes can be viewed [here](/wireframes/).

### Code styling
For consistency and readable code I am using formatters and format on save option.
* HTML - Beautify
* SCSS - Formate
* JavaScript - Prettier (options)

    ```json
    "printWidth": 88,
    "tabWidth": 4,
    "trailingComma": "all",
    "semi": false
    ```

* Python - Black

#### Rationale
I spent quite a bit of time reading about JavaScript and Python formatting conventions and settled on this configuration for a few reasons. For JS, I prefer the clean look without semicolons but I understand it can cause ASI errors. The 'semi: false' setting of Prettier covers this and will insert them where this could occur.
I decided to use Black as my Python formatter because I liked what I read about it and after using it I like the code it produces. It has a line length of 88 and solid reasoning behind this choice, I chose the same number for Prettier to be consistent across the project. Using pylint-django and a vscode extension called Error Lens I am notified immediately of errors in my code and this has helped me to write functional code and learn about best practices.

## Information Architecture

### Data models
In order to map the relationships between the models in this project I created an entity relationship diagram using symbols denoting the type of relationship. This can be viewed [here](/wireframes/entity-relationships.jpg).
I followed this process -
* Identify entities (user, order, etc.)
* Identify attributes (user has: name, phone number, etc.)
* Identify relationships (users place orders, lineitems are part of orders)
* Identify cardinality and optionality (how many orders, how many users per order, etc.)

#### User
I am using the [default django user model](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#user-model). Additionally I have decided to use allauth for this project as it seems to be the best option to allow users to login with their email instead of a username, which is what I want. For reference I am using the allauth docs and [this](https://www.mattlayman.com/building-saas/user-accounts-django-allauth/) page.


#### Profiles App
##### User Profile Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
User|user|OneToOneField|django.contrib.auth.get_user_model(), on_delete.models.CASCADE
Full Name|default_full_name|CharField|max_length=100, null=True, blank=True
Phone Number|default_phone_number|CharField|max_length=20, null=True, blank=True
Street 1|default_street_address_1|CharField|max_length=100, null=True, blank=True
Street 2|default_street_address_2|CharField|max_length=100, null=True, blank=True
City|default_city|CharField|max_length=50, null=True, blank=True
Postcode|default_postcode|CharField|max_length=20, null=True, blank=True
State|default_state|CharField|max_length=20, null=True, blank=True
Country|default_country|CountryField|blank_label='Country', null=True, blank=True
Client check|is_client|BooleanField|default=False
Personal Key|personal_key|CharField|max_length=32, null=True, blank=True


#### Products App
##### Product Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name|name|CharField|max_length=50, null=False, blank=False
Category|category|ForeignKey|'Category', null=True, blank=True, on_delete=models.SET_NULL
SKU|sku|CharField|max_length=50, null=False, blank=False
Description|description|TextField|null=False, blank=False, default=''
Booking required|booking_required|BooleanField|default=False, null=False, blank=False
Shipping required|shipping_required|BooleanField|default=False, null=False, blank=False
Featured|featured|BooleanField|default=False, null=False, blank=False
Price|price|DecimalField|max_digits=6, decimal_places=2
Image URL|image_url|URLField|max_length=1024, null=True, blank=True
Discontinued|discontinued|BooleanField|default=False

##### Category Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name|name|CharField|max_length=20


#### Checkout App
##### Order Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Order Number|order_number|CharField|max_length=32, null=False, editable=False
Associated User|user_profile|ForeignKey|UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='orders'
Full Name|full_name|CharField|max_length=100, null=False, blank=False
Email|email|EmailField|max_length=254, null=False, blank=False
Phone Number|phone_number|CharField|max_length=20, null=True, blank=True
Street 1|street_address_1|CharField|max_length=100, null=True, blank=True
Street 2|street_address_2|CharField|max_length=100, null=True, blank=True
City|city|CharField|max_length=50, null=True, blank=True
Postcode|postcode|CharField|max_length=20, null=True, blank=True
State|state|CharField|max_length=20, null=True, blank=True
Country|country|CountryField|blank_label='Country', null=True, blank=True
Date|date|DateTimeField|auto_now_add=True
Total Price|total_price|DecimalField|max_digits=10, decimal_places=2
Booking Required|booking_required|BooleanField|default=False
Shipping Required|shipping_required|BooleanField|default=False
Stripe PID|stripe_pid|CharField|max_length=254, null=False, blank=False, default=''

##### OrderLineItem Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Order|order|ForeignKey|Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product|product|ForeignKey|Product, null=False, blank=False, on_delete=models.PROTECT
Total|total|DecimalField|max_digits=6, decimal_places=2, null=False, blank=False, editable=False, default=0,


#### Bookings App
##### Booking Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Associated Order|order|OneToOneField|Order, on_delete=models.SET_NULL, null=True, blank=True, related_name="booking"
Associated User|user_profile|ForeignKey|UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='bookings'
Booking Date|booking_date|DateField|auto_now_add=False, null=True, blank=True
Booking Time|booking_time|TimeField|auto_now_add=False, null=True, blank=True


#### Reviews App
##### Review Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Associated User|user_profile|ForeignKey|UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='reviews'
Associated Product|product|ForeignKey|Product, blank=False, Null=False, related_name='reviews'
Review content|review_content|TextField|null=False, blank=False, default=''


## Features

### Implemented Features
#### Pages
* Toasts to display messages as popups on every page using django messages module, with messages for most actions across the website
* Featured product and social proof carousel on the index page
* Custom error page templates that extend the base template and keep the user experience consistant
* Contact Form for general enquiries

#### User Profile
* User Profile dashboard with inner navbar. Display and update personal information, access technical support, manage bookings and view order history
* Option during checkout to save data to profile automatically
* Auto generation of a personal key once a purchase is made that gives clients access to the business' mobile app for managing products

#### Products & Reviews
* Products card display with a detailed page on clicking. Buttons to buy on all products for ease of adding to cart
* Featured review on the product details, with a full page for all reviews. Clients can leave a review about products they have purchased
* Verification system to ensure reviews are only from clients who have purchased the product

#### Cart & Checkout
* Cart in the session that stores selection of products and has checks to stop unintended behaviour such as multiple items requiring bookings per order
* Cart view that displays a summary of the order before checking out. Can remove items from the cart in this view
* Before checkout there is a login check that will notify user of the need to create an account or login, and will redirect to checkout with the stored cart
* Checkout view with secure Stripe payments. Personal information is taken from the user profile if it exists, and there is a full order summary displayed
* Checkout process involves a webhook with Stripe to ensure the order is processed if there are any issues

#### Bookings
* A booking system for orders with products that require a booking
* After successfully placing an order that requires a booking, a related booking model is created and the user is notified they need to set the time
* Datepicker calendar using JQuery UI and buttons to select from a range of times
* Manually set timed session variable to notify via toast messages the user if they have a booking waiting to be placed

#### API
* An internal API to handle dynamic updating of the booking system
* Users will select a desired date from the range available and open times are enabled. Already existing bookings on that day will not be available
* To plan the logic of the API I created a flowchart which can be viewed [here](/wireframes/booking-api-flowchart.jpg). This helped me understand how I needed to send requests to the backend, what to query, and how to process the response

### Planned Features
* Expanded client technical support to include detailed information about their installed products
* News page with featured articles to post updates about the company's latest developments
* Community hub for people to connect and share open source apps for cyberware

### Extra Comments
I was on a very tight schedule for this project, and to manage it I created a plan of development based on the MVP (minimum viable product) concept. To do this I worked in an iterative process where I created the whole project at a functional level and then improved features with the remaining time I had. I think this taught me valuable lessons in planning and time management while developing a project. It also made me decide what were the most important things to focus on to have a project ready in time, which I believe is relevant to real-world situations


## Technologies Used
### Languages
* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)
* [Python](https://www.python.org/)

### Libraries
* [Django](https://www.djangoproject.com/)
* [Black](https://pypi.org/project/black/)
* [Pylint](https://pypi.org/project/pylint/)
* [Pylint-django](https://pypi.org/project/pylint-django/)
* [Gunicorn](https://gunicorn.org/)
* [Django-allauth](https://pypi.org/project/django-allauth/)
* [Django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
* [Django-countries](https://pypi.org/project/django-countries/)
* [Stripe](https://stripe.com/ie)
* [Whitenoise](https://pypi.org/project/whitenoise/)
* [Dj-database-url](https://pypi.org/project/dj-database-url/)
* [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
* [Django-tastypie](https://pypi.org/project/django-tastypie/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [JQuery UI](https://jqueryui.com/)
* [Popper.JS](https://popper.js.org/)
* [Slick](https://kenwheeler.github.io/slick/)

### Tools
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
* [PostgreSQL](https://www.postgresql.org/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com)
* [Git](https://git-scm.com/)
* [SASS/SCSS](https://sass-lang.com/)
* [Postman](https://www.postman.com/)
* [Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify)
* [Formate](https://marketplace.visualstudio.com/items?itemName=MikeBovenlander.formate)
* [JShint](https://jshint.com/)
* [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)

## Testing & Bugs
A full write up for testing and dealing with bugs is [here](/TESTING.md)

## Development & Deployment
Note: *These instructions are applicable to Windows and VSCode, and will be using the tool [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/). A requirements.txt file is also available if you are not using Pipenv. If you are not using Windows or VSCode please refer to your IDE documentation for any differences.*

### Local Development & Set-Up
Requirements to run locally:
* An IDE such as [VSCode](https://code.visualstudio.com/)

You have have installed
* [Python 3](https://www.python.org/downloads/)
* [PIP](https://pip.pypa.io/en/stable/installing/)
* [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

You have a free account with [Stripe](https://dashboard.stripe.com/register). To get your testing secret keys for Stripe and assistance in setting it up for the project, please visit the developer section of their website and follow the instructions.

*All commands from this point should be entered in the terminal of your IDE*

Install Pipenv with this command

`pip install --user pipenv`

#### Instructions

1. Clone the repository with this command

    `git clone https://github.com/asdfractal/yggdrasil-labs`

2. In your IDE terminal, navigate to this folder
3. Install the required packages and start your virtual environment with these commands

    `pipenv install`

    `pipenv shell`

4. Set up your environment variables
    * create a folder in project root called `.vscode`, inside this folder create a file called `settings.json` and create this json object. Remove the angle brackets `<>` and place your variables inside the quotes.

    ```json
        "terminal.integrated.env.windows": {
            "DEVELOPMENT": "1",
            "STRIPE_PUBLIC_KEY": "<your key>",
            "STRIPE_SECRET_KEY": "<your key>",
            "STRIPE_WEBHOOK_SECRET": "<your key>",
            "STRIPE_CURRENCY": "<payment currency>",
            "SECRET_KEY": "<your key>",
            "EMAIL_HOST": "<your email host server>",
            "EMAIL_HOST_USER": "<your email address>",
            "EMAIL_PASSWORD": "<your email app password>",
            "EMAIL_PORT": "<your email host port>"
        }
    ```

    * Note: `SECRET_KEY` is a long random string and can be generated [here](https://miniwebtool.com/django-secret-key-generator/)
    * Close your VSCode terminal session and open a fresh terminal to activate the variables, and restart your environment with `pipenv shell`
    * Create a `.gitignore` file and add `.vscode` to ensure the security of your environment variables

5. Migrate the database models with this command

    `python manage.py migrate`

6. Load the data into the database with this command

    `python manage.py loaddata products.json`

7. Create a superuser and set up the credentials with this command

    `python manage.py createsuperuser`

8. Run the app with this command

    `python manage.py runserver`

    * The address to access the website is displayed in the terminal
    * add `/admin` to the end to access the admin panel with your superuser credentials

### Heroku Deployment

1. On the [Heroku](https://www.heroku.com/) website, create an account or login
2. Create a new app from your dashboard by clicking **New** and then **Create new app**
3. Enter a name, select a region and then click **Create app**
4. On the app page, click on **Resources**
5. In the add-ons section of the page, type `postgres` and select Heroku Postgres
6. Select the **Hobby Dev — Free** option from the dropdown and click **Provision**
7. Navigate to the **Settings** page, click on **Reveal Config Vars** in the Convig Vars section
8. Set the following Config Vars

    | Key | Value |
    --- | ---
    `PRODUCTION` | `1`
    `STRIPE_PUBLIC_KEY` | `your key`
    `STRIPE_SECRET_KEY` | `your key`
    `STRIPE_WEBHOOK_SECRET` | `your key`
    `STRIPE_CURRENCY` | `payment currency`
    `SECRET_KEY` | `your key`
    `EMAIL_HOST` | `your email host server`
    `EMAIL_PASSWORD` | `your email/app password`
    `EMAIL_HOST_USER` | `your email address`
    `EMAIL_PORT` | `your email host port`

9. From this screen, copy the value of DATABASE_URL
10. Add a new entry to the settings.json `"terminal.integrated.env.windows"` setting

    ```json
    "DATABASE_URL": "<Value copied from Heroku>"
    ```
    * Close your VSCode terminal session and open a fresh terminal to activate the variables, and restart your environment with `pipenv shell`

11. Migrate the models to the database with this command

    `python manage.py migrate`

12. Load the data into the database with this command

    `python manage.py loaddata products.json`

13. Create a superuser with this command

    `python manage.py createsuperuser`

14. In the project settings.py add your heroku app url to the allowed hosts setting

    `ALLOWED_HOSTS = ["YOUR_URL"]`

15. Before proceeding further you must create a new repo on github by following these steps
    * On the [GitHub](https://github.com/) website, sign in or create an account
    * Click on the *green* **New** button and give your repo a name, then click **Create repository**
    * From the **Quick setup** section copy the github url to your repo
    * In the terminal in your IDE, make sure you are in the project folder, change the remote and push with these commands

    `git remote set-url origin YOUR_REPO_URL`

    `git push`

16. In Heroku, click on **Deploy** in the navigation bar
17. In the **Deployment** section, select **GitHub** as the deployment method
18. Search for your repository and click **Connect**
19. Click Deploy Branch
    * Optionally enable automatic deploys to deploy every time a the repository is updated
20. Click on **Activity** tab to see the build log
21. When build has succeeded, click on **Open App** to view the deployed site

## Credits
* This project was developed following Chris Zielinski and the Boutique Ado project code provided by [Code Institute](https://codeinstitute.net/), but was customized and expanded on to meet my needs
* Code for the booking session variable was aided by [Vadim Serdiuk's](https://stackoverflow.com/a/54983291/10828019) answer on Stack Overflow
* I followed [Scott Domes](https://codeburst.io/create-a-django-api-in-under-20-minutes-2a082a60f6f3) article on setting up an API
* The loading spinner is taken from [loading.io](https://loading.io/css/)
* During development I constantly referred to and used code from [Django](https://docs.djangoproject.com/en/3.1/) and [Stripe](https://stripe.com/docs) documentation


### Image Credits
* [Index Background](https://www.wallpaperflare.com/)
* [About Background](https://wallpapersafari.com/)
* Order page tree - [adoomer](https://www.deviantart.com/adoomer)
* [Augment](https://www.facebook.com/Techsupportnow/)
* [Immerse](https://visualmodo.com/keep-up-tech-trends/)
* [SecureMe](https://www.vectorstock.com/)
* [Synanpse](https://www.shutterstock.com/)
* [Cortical Stack](https://www.gamespot.com/articles/altered-carbon-review-netflix-spins-up-a-new-cyber/1100-6456241/)
* [Cyberoptics](https://www.polygon.com/2020/3/15/21180442/westworld-incite-ai-rehoboam-season-3-explained)
* [Netdeck](https://www.redbubble.com/i/t-shirt/CPU-Computer-Heart-White-by-UnitedsWorld/11402131.FB110#&gid=1&pid=3)
* [Neural Network](https://www.shutterstock.com/)
* [Clock Upgrade](https://www.wallpaperize.cc/)
* Cortical Dose - [Jie Liou](https://www.artstation.com/jie8241)
* [Haptic Feedback](https://pngtree.com/)
* [Neuron Capacity](https://vironit.com/neural-network-why-it-is-so-necessary-to-use-it-in-it-development/)
* [Stack Capacity](https://no.pinterest.com/pin/731975745677155963/)

## Acknowledgements

Huge thanks to [Simen Daehlin](https://github.com/Eventyret) for being an incredible mentor and teacher, and for helping me stay on top of everything when I was struggling.

Thanks to [Chris Zielinski](https://github.com/ckz8780) for being very active on slack and answering questions and personal messages, as well as the amazing Boutique Ado mini project.

Thanks to fellow students [Stephen Seagrave](https://github.com/nemixu) and [Sam Laubscher](linkedin.com/in/sam-laubscher-559a4215b) for testing the deployed website and offering feedback.

[Code Institute](https://codeinstitute.net/) for this great course and network that I am grateful to be a part of.

### Disclaimer
This site is part of a course project and is intended for educational purposes only
