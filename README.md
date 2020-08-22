# Yggdrasil Labs

Yggdrasil Labs is a cybernetics and bioware company providing implants and other transhuman upgrades. Site visitors can browse the range of products and add to their cart. Due to the nature of the business it is required to register before checking out, as it is possible a booking must be created. Also the business offers technical support to it's clients.
This is a full stack website developed for Code Institute milestone project 4.

## Contents:
* User Experience
    * Project Goals
    * Target Audience Goals
    * Site Owner Goals
    * User Stories
    * Requirements
    * Expectations
* Design Choices
    * Colours
    * Fonts
    * Icons
    * Styles
        * Folder structure
    * Images
    * Wireframes
* Information Architecture
    * Data models
        * User
        * Profiles App
            * User Profile Model
        * Products App
            * Product Model
            * Category Model
        * Checkout App
            * Order Model
            * Order Lineitem Model
        * Bookings App
            * Booking Model
        * Reviews App
            * Review Model
* Features
    * Implemented Features
    * Planned Features

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

I am also using the following colour for message alerts
* Warning colour - #FC440F
* Error colour - #FF0033
* Success colour - #00FF00
* Info colour - #F2EA02

### Fonts
* Title/Logo - [Elianto](https://www.behance.net/gallery/33808280/Elianto-Free-Font) - A unique font used for the business title and logo
* Display - [Orbitron](https://fonts.google.com/specimen/Orbitron) - This font is perfect for the desired feel of the website. Bold, solid, and professional with a unique character
* Body font - [Raleway](https://fonts.google.com/specimen/Raleway) - Easy to read and well spaced, compliments the display font

### Icons
I have used a range of font awesome icons across the website to aid in displaying content and navigation options instead of using only text.

### Styles
I have wanted to use scss for some time and this project I have decided to implement it for the first time. I have used [this](https://matthewelsom.com/blog/simple-scss-playbook.html) resource as a guide for the architechture.

#### Folder structure
* scss
    * abstracts - this is for variables, mixins, etc. and has no direct output
    * base - top of the document resets, utility classes, etc.
    * components - reusable components with general styles
    * layout - specific styles for individual pages or components
    * vendor - any third party imports

### Images
Credits

### Wireframes
Using the program Pencil I designed wireframes for desktop and mobile/tablet. The mobile/tablet are combined because there will be minimal differences in the design. The wireframes can be viewed [here](/wireframes/).

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
##### User Profile
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
Product|product|ForeignKey|Product, null=False, blank=False, on_delete=models.CASCADE
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
* Manually set timed cookie to notify the user if they have a booking waiting to be placed
* Contact Form for general enquiries

#### User Profile
* User Profile dashboard with inner navbar. Display and update personal information, access technical support, manage bookings and view order history
* Auto generation of a personal key once a purchase is made that gives clients access to the business' mobile app for managing products

#### Products & Reviews
* Products card display with a detailed page on clicking. Buttons to buy on all products for ease of adding to cart
* Featured review on the product details, with a full page for all reviews. Clients can leave a review about products they have purchased

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

#### API
* An internal API to handle dynamic updating of the booking system
* Users will select a desired date from the range available and open times are enabled. Already existing bookings on that day will not be available
* To plan the logic of the API I created a flowchart which can be viewed [here](/wireframes/booking-api-flowchart.jpg). This helped me understand how I needed to send requests to the backend, what to query, and how to process the response


### Planned Features
* Expanded client technical support to include detailed information about their installed products
* News page with featured articles to post updates about the company's latest developments


## Technologies Used
### Languages
* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)
* [Python](https://www.python.org/)

### Tools and Libraries
* [Django](https://www.djangoproject.com/)
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
* [PostgreSQL](https://www.postgresql.org/)
* [Black](https://pypi.org/project/black/)
* [Pylint](https://pypi.org/project/pylint/)
* [Pylint-django](https://pypi.org/project/pylint-django/)
* [Gunicorn](https://gunicorn.org/)
* [Django-allauth](https://pypi.org/project/django-allauth/)
* [Django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
* [Pillow](https://pypi.org/project/Pillow/)
* [Django-countries](https://pypi.org/project/django-countries/)
* [Stripe](https://stripe.com/ie)
* [Whitenoise](https://pypi.org/project/whitenoise/)
* [dj-database-url](https://pypi.org/project/dj-database-url/)
* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
* [Django-tastypie](https://pypi.org/project/django-tastypie/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [JQuery UI](https://jqueryui.com/)
* [Popper.JS](https://popper.js.org/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com)
* [Git](https://git-scm.com/)
* [Slick](https://kenwheeler.github.io/slick/)
* [SASS/SCSS](https://sass-lang.com/)


## Testing
A full testing write up is available [here](/testing.md)
