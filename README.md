# Yggdrasil Labs

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
The overwhelming colour aesthetic in the aformentioned inspirations are blues, purples and pinks on a dark backdrop. There is also an emphasis on neon style colours. With this in mind I have created this colour scheme. A palette of the scheme can be viewed [here](/wireframes/colour-palette.png).

* Primary colour - #00C2CE - This blue/green brings a nice contrast to the overall dark theme of the website, drawing attention where it is present
* Secondary colour - #D76EE5 - A slightly toned down neon pink/purple, complimenting the primary colour and highlighting elements
* Tertiary colour - #F22CA6 - A vibrant flower pink, to be used sparingly to add extra highlights
* Dark Grey - #1F1F1F - A dark grey not far off black
* Grey - #3D3D3D - A lighter shade of the dark grey

### Fonts
* Display font - [Elianto](https://www.behance.net/gallery/33808280/Elianto-Free-Font) - This font is perfect for the desired feel of the website. Bold, solid, and professional with a unique character
* Body font - [Josefin Sans](https://fonts.google.com/specimen/Josefin+Sans) - Easy to read and well spaced, compliments the display font

### Icons
_Font awesome(expand)_

### Styles
I have wanted to use scss for some time and this project I have decided to implement it for the first time. I have used [this](https://matthewelsom.com/blog/simple-scss-playbook.html) resource as a guide for the architechture.

### Wireframes
Using the program Pencil I designed wireframes for desktop and mobile/tablet. The mobile/tablet are combined because there will be minimal differences in the design. The wireframes can be viewed [here](/wireframes/).

## Information Architecture

### Data models

#### User
I am using the [default django user model](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#user-model). Additionally I have decided to use allauth for this project as it seems to be the best option to allow users to login with their email instead of a username, which is what I want. For reference I am using the allauth docs and [this](https://www.mattlayman.com/building-saas/user-accounts-django-allauth/) page.

#### User Profile
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
User|user|OneToOneField|django.contrib.auth.get_user_model(), on_delete.models.CASCADE
Full Name|default_full_name|CharField|max_length=100, null=True, blank=True
Email|default_email|EmailField|max_length=254, null=False, blank=False
Phone Number|default_phone_number|CharField|max_length=20, null=True, blank=True
Street 1|default_street_address_1|CharField|max_length=100, null=True, blank=True
Street 2|default_street_address_2|CharField|max_length=100, null=True, blank=True
City|default_city|CharField|max_length=50, null=True, blank=True
Postcode|default_postcode|CharField|max_length=20, null=True, blank=True
State|default_state|CharField|max_length=20, null=True, blank=True
Country|default_country|CountryField|blank_label='Country', null=True, blank=True

#### Product
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name|name|CharField|max_length=50, null=False, blank=False
SKU|sku|CharField|max_length=50, null=False, blank=False
Description|description|TextField|null=False, blank=False, default=''
Booking required|booking_required|BooleanField|default=False, null=False, blank=False
Shipping required|shipping_required|BooleanField|default=False, null=False, blank=False
Price|price|DecimalField|max_digits=6, decimal_places=2
Image URL|image_url|URLField|max_length=1024, null=True, blank=True
Image|image|ImageField|null=True, blank=True

#### Categories
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name|name|CharField|max_length=20

#### Order
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Order Number|order_number|CharField|max_length=32, null=False, editable=False
Booking Number|booking_number|ForeignKey|Booking, null=True, Blank=True, on_delete=models.SET_NULL
Associated User|user_profile|ForeignKey|UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='orders'
Full Name|full_name|CharField|max_length=100, null=False, blank=False
Email|email|EmailField|max_length=254, null=False, blank=False
Phone Number|phone_number|CharField|max_length=20, null=False, blank=False
Street 1|street_address_1|CharField|max_length=100, null=False, blank=False
Street 2|street_address_2|CharField|max_length=100, null=True, blank=True
City|city|CharField|max_length=50, null=False, blank=False
Postcode|postcode|CharField|max_length=20, null=False, blank=False
State|state|CharField|max_length=20, null=False, blank=False
Country|country|CountryField|blank_label='Country', null=False, blank=False
Date|date|DateTimeField|auto_now_add=True
Total Price|total_price|DecimalField|max_digits=10, decimal_places=2
Original bag|original_bag|TextField|null=False, blank=False, default=''
Stripe PID|stripe_pid|CharField|max_length=254, null=False, blank=False, default=''

#### OrderLineItem
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Order|order|ForeignKey|Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product|product|ForeignKey|Product, null=False, blank=False, on_delete=models.CASCADE
Cost of product|lineitem_total|DecimalField|max_digits=6, decimal_places=2, null=False, blank=False, editable=False

#### Booking
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Associated User|user_profile|ForeignKey|UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='user_booking'
Associated Order|order|ForeignKey|UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='order_booking'
Booking Time|booking_time|DateTimeField|auto_now_add=False

#### Review
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Associated User|user_profile|ForeignKey|UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='user_review'
Associated Product|product|ForeignKey|Product, blank=False, Null=False, related_name='product_review'
Review content|review_content|TextField|null=False, blank=False, default=''

