# Testing & Bugs

## Contents:
* Testing
    * Authentication
    * Feature Tests
        * User Profile
        * Products
        * Reviews
        * Cart & Checkout
        * Booking system
        * API
        * Toast Messages
        * Contact Form
    * Stripe
    * Responsiveness
    * Browser Compatibility
    * Forward and Back button navigation
    * Code Validation
        * W3 HTML
        * W3 CSS
        * JavaScript
        * Python
    * Chrome devtools Lighthouse
    * User Testing
* Bugs


## Testing
The whole project was testing thorougly throughout the development process using Chrome Dev Tools and personally using the features.

### Authentication

#### Expectation
There are certain parts of the website not accessable to unregistered users
#### Implementation
Using Django template varaibles to remove certain options to anonymous users and login required decorators to ensure that even if a page is accesed by the address bar the user will be redirected. In conjunction with custom functions in order to pass a Django message to inform the user of the problem
#### Test
* While not logged in -
    * Confirm the navbar is displaying a link to login and not to account dashboard
    * In the address bar enter '/profile/' and confirm redirect to the login page with a toast notification
        * Login and confirm redirect to account dashboard
    * Add a product to cart, navigate to cart page, click 'checkout'
    * Confirm redirect to login page with a toast notification
        * Login and confirm redirect to checkout page with current cart
            * If a product in the cart had already been purchased by the user, instead they are redirected to cart informing them of the issue and the product is removed from cart
#### Result
Unregistered users are not provided with options to access areas intended for registered users, and if they access it via address bar there are systems to deal with it
#### Verdict
This test has passed



Doing these feature tests I have ensured that I cover all requirements and expectations of the user stories, as well as adding additional functionality and user experience through testing initial implementation and improving on the experience.

----

### User Profile

#### Expectation
Users can register, login and have a personal profile. If they want they can store their billing information, access order history and manage other aspects of their use of the site
#### Implementation
Using Django-Allauth to handle registration, a custom User Profile model that is related to the Django user model is created upon registering. An account dashboard that includes saving and updating personal information and has sections for technical support, bookings management and order history
#### Test
* Navigate to the login page and register for a new account, confirm that a new user profile was created in the database
* Navigate to the products page, add a product that requies a booking to the cart, navigate to cart, click checkout, fill out and submit checkout form, confirm order has been placed
* Navigate to the dashboard. Using the personal info form enter details and click update, confirm they have been saved to the profile in the database
* Click Technial Support, fill in the form, submit it and confirm the form content is processed and delivered, checking with Django's console email backend
* Click Bookings, confirm booking display with booking information or notification booking must be made, with a link to do so
* Click Order History, see the order history summary is displayed with a link to a detailed version
#### Result
Users can sign up and a profile will automatically be created. There is a functional dashboard with sections displaying information help manage their experience using the service
#### Verdict
This test has passed

### Products

#### Expectation
View a list of products, view detailed information about specific product
#### Implementation
A products page with cards displaying all products with a little bit of information. There is a javascript category filter to sort products by category, which updates dynamically to avoid reloading the page. Clicking on the product image or details button navigates to a page with full information about the product
#### Test
* Navigate to the products page and check all products are displaying
* Click on category buttons and confirm filtering displays intended products
* Navigate to product details and confirm all products access the correct page through both available links
#### Result
All products are displaying, filtering works and products have their own page with more details displaying
#### Verdict
This test has passed

### Reviews

#### Expectation
Users can leave a review informing other potential clients of their experience
#### Implementation
A featured review section on the product details page, which displays one review, and a link to a reviews page which displays all reviews and a form to leave a review. A reviews app with a Review model, which has a foreign key to the User Profile and Product models. Once a user has made a purchase the option of leaving a review for the product they purchased is made available. To ensure reviews are genuine it is not possible to leave reviews for products that a user has not purchased
#### Test
* While not logged in, navigate to any product details page, if there are no reviews for the product there is a message informing of that and no link to the review page
* If there are reviews, click 'all reviews' and confirm there is no form available to leave a review
* Login to account, navigate to the details page of a product the account has not purchased and has reviews, click 'all reviews' and confirm there is no form available to leave a review
* Navigate to the details page of a product the account has purchased, click 'create one' or 'all reviews', click icon to create a review, fill in form and submit. Confirm review is on the page, a toast notification is displayed and there is an option to edit or delete the review
* Click edit, change the reviews and submit. Confirm review is updated
* Click delete, click delete on popup, confirm review is deleted
#### Result
Users can write a review about products they are confirmed to have purchased, ensuring their reviews are genuine and can inform potential clients. It is not possible to leave a review if not verified to have purchased the product
#### Verdict
This test has passed

### Cart & Checkout

#### Expectation
Select products and add them to cart, remove products, purchase selection through a secure checkout and book an appointment if required
#### Implementation
Create a cart using session storage. Unintended actions (eg; duplicate product in cart, multiple bookings required per order) are blocked with checks and the user is notified via toast message. A cart summary page to confirm their selection before proceeding to checkout, which is a simple process using a form and Stripe. Form is created from the Order model and validates information before processing, informing the user of any issues. After successful submission a success page is shown with the order confirmation
#### Test
These tests assume the user is registered, as unregistered checkout is covered in the authentication test.
* Navigate to the products page, click 'buy' to add a product to cart
* Navigate to cart, click 'remove from cart' and confirm product is removed with a toast confirmation message
* With an empty cart, a message is displayed informing user and providing a link to products page. There is no checkout button if cart is empty
* With an empty cart, type '/checkout/' in the address bar, confirm redirect to products page with a toast message informing of empty cart
* With products in the cart, click 'checkout', fill out and submit checkout form
* Order confirmation is displayed with an order summary and thank you message
* Navigate to account dashboard, click order history and confirm order is also displayed there
#### Result
It is simple to add products to cart and view the contents before checkout. Users can remove products and cannot checkout with an empty cart. The checkout process is easy to navigate, the user does not have to fight against poor design. They are notified of actions they take with appropriate message levels depending on the action
#### Verdict
This test has passed

### Booking system

#### Expectation
Users can make a booking if they purchase a product that it is required for
#### Implementation
A bookings app with a Booking model with foreign keys to Order and User Profile. The system is tied automatically to the checkout process. Product and Order models have a BooleanField that marks if a booking is required. If a product with this is part of an order, that order will be flagged as booking required. Once the checkout is complete of that order, a related booking model will be automatically created. There is a link directly from the checkout success page to create a booking, as well as a booking section in the account dashboard to manage bookings. Users will be notified via toasts if they need to create a booking at 10 minute intervals by using a custom session variable. There is page to handle booking creation using a form that validates date and time. Users select a date and time from what is available. The date is up to one month and times are set through buttons that set a value
#### Test
* Navigate to the products page, add a product that requires a booking to cart, navigate to cart, click checkout, fill out and submit checkout form
* On the checkout success page click 'make booking'
* Complete the form by selecting a date, choose an available time, submit
* Confirm booking is placed via toast message and in the bookings section of the dashboard under upcoming bookings heading
* Click change booking, fill out the form again and submit
* Confirm the booking time is changed and displayed in dashboard
* Purchase a product that requires a booking, but don't immediately place the booking
* Confirm toast notification is displayed after 10 minutes and does not repeat on every page change
#### Result
The booking system works in conjunction with the checkout process and takes into account situations where the user might not create a booking immediately after placing an order. Users are given predetermined dates and times to make a booking based on business hours and availability in the system
#### Verdict
This test has passed

### API

#### Expectation
A system that queries existing bookings in the database and returns the objects to ensure only available times can be selected
#### Implementation
An API app, using the Django-Tastypie package to handle fetch requests from the browser. Through the booking system a user selects a date, the date is processed and a url is created to query the database with that information. The server responds with booking objects that match the date. The objects are handled with a script that checks the times and enables selection of times that are available on that date. If no times are available the user is informed of this and asked to choose a different date
#### Test
* Using Postman, confirm the server is sending the intended response
* On the booking page, select a date and confirm the correct query URL is generated and sent to the server via console.log
* After creating multiple bookings in the database, use the booking system to confirm functionality
    * Select a date with no bookings - all times are available
    * Select a date with one booking - confirm the correct times are available
    * Select a date with two bookings - confirm the correct time is available
    * Select a date with three bookings - confirm no times are available
#### Result
The API handles requests and provides the expected response and the booking system updates as expect
#### Verdict
This test has passed

### Toast Messages

#### Expectation
Users are notified of actions or errors via a popup message
#### Implementation
Using Bootstrap Toast system and the Django messages module, users are notified of many different actions or errors across the website. The messages use appropriate levels and the toasts are styled using conventional colours based on those levels
#### Test
* Add a product to cart, a success toast is displayed with green styling
* Try to add a product to cart that is already there, an info toast is displayed with yellow styling
* Submit a form that does not validate, an error toast is displayed with red styling
#### Result
Toast messages are displayed for most actions and all errors across the site, ensuring users have confirmation of actions and are informed about errors
#### Verdict
This test has passed

### Contact Form

#### Expectation
Users can submit a contact form to ask questions or otherwise contact the business. Should be available to unregistered users
#### Implementation
A page dedicated to this, a form with email and body fields
#### Test
* While not logged into, navigate to contact page and fill in the form
* Submit it and confirm the form content is processed and delivered, checking with django's console email backend
* While logged into, navigate to contact page and confirm registered email address is automatically applied to the form field, with the option to choose a different address
#### Result
Users can enter their email and write in the textarea to contact the business, and it is processed successfully
#### Verdict
This test has passed

### Stripe

#### Expectation
Payments are handled securely to protect sensitive user information
#### Implementation
Using the Stripe package and creating webhooks to verify communication with the Stripe server. Following the Boutique Ado project and referencing [Stripe docs](https://stripe.com/docs) on how to set up their system properly
#### Test
Test the checkout process as referenced above, additionally checking the Stripe developer dashboard for webhook response confirmation. I studied the Stripe docs to test thoroughly and spent a lot of time analyzing the responses and my logs to figure out how it was working and to solve any issues
#### Result
The payments are handled securely use the systems provided by Stripe
#### Verdict
This test has passed

### Responsiveness

#### Expectation
The website is accessable on the majority of different screen sizes and devices
#### Implementation
Using the Bootstrap framework to develop the website means I had access to their grid system, which greatly aids in implementating responsive design. Combining this with sass mixins I was able to ensure responsiveness on all elements. I used 320px as the base size and a custom variable for 'xs' of 400px, because the gap between 320 and 'sm' of 576 is too much
#### Test
Using Chrome dev tools with iPhone 5 as the base size of 320px, and using various different screen sizes as well as responsive mode. I made sure the content was accessable and readable at all different sizes. Additionally I tested on my personal phone - Samsung Galaxy S10E
#### Result
The website is responsive and accessable on a large majority of available devices and screen sizes
#### Verdict
This test has passed

### Browser Compatibility

#### Expectation
The website displays and functions on major browsers
#### Implementation
Using modern code that is widely supported
#### Test
Aside from the development in Chrome, I tested on Firefox, Edge and Safari. I checked the usage share of browsers and found this to an acceptable coverage of approximately 93%. I repeated all the tests outlined in the other sections of this documents and there was no obvious broken functionality
#### Result
The website functions as intended on major browsers
#### Verdict
This test has passed

### Forward and Back button navigation

#### Expectation
The website is navigable using the forward and back buttons and does not break or have unintended actions
#### Implementation
Through checks in the views to redirect, prevent resubmissions, and defensive programming
#### Test
* Navigate to every page via clicking, and then navigate back and forward through all selections with back and forward buttons
* Make a purchase using the checkout process and navigate back to checkout page, confirm cart is empty and redirect to product page with a notification of empty cart
* Submit a contact form, navigate back and confirm form does not resubmit
#### Result
The whole website is navigable with forward and back buttons
#### Verdict
This test has passed

### Code Validation

#### [W3 HTML Validator](https://validator.w3.org/)
Using this validator I tested every page and dealt with any issues that came up, such as mistaken double attributes. After fixing the errors the whole website validates without errors

#### [W3 CSS Validator](https://jigsaw.w3.org/css-validator/)
Using this validator I tested all the css, the only errors are from third party libraries

#### JavaScript
Using the VSCode extensions JShint and Error Lens I am notified in real time of any errors and use this system to validate the code

#### Python
Using the python packages Black, Pylint and Pylint-Django in conjunction with VScode extension Error Lens I am notified in real time of any errors and use this system to validate the code

### Chrome Dev Tools Lighthouse
I tested every page using Lighthouse and fixed any issues to do with accessibility and best practice. After fixing issues every page is receiving 95+ in both of these categories

### User tests
Two of my housemates and two fellow students have tested the website by using it and did not report any bugs. The feedback was positive and they used all the systems without any guidance required, aside from one student not knowing the Stripe testing credentials. This is why I have included them at the top of the README


## Bugs

### Development bugs

### Booking notification toast message

#### Bug
There is a toast message that pops up informing the user of an open booking they have to make, using a contxt processor to make it available across the whole site. On first implementation it was showing every time the page was reloaded or changed to a different view, becoming very annoying
#### Fix
Using datetime create a session variable with a value of 10 minutes from current time, then on every page load check the value of this variable and if it has been 10 minutes, notify the user and set a new variable
#### Verdict
This bug was fixed and the user isn't overloaded with toast notifications


### Booking time button not enabling or disabling properly

#### Bug
When there were 0, 1 or 3 bookings it was working as intended, but with 2 it would not enable correct buttons. This is because my initial implementation was looping through the response objects and enabling buttons that did not match the time. But when there were 2 bookings it would match a time on the first booking and then match a different time on the second, therefore enabling the first time button
#### Fix
I created the permanentTimes array, which has the slots the business has made pre-set for bookings. Then I query the database and from the results create the bookedTimes array. I filter the permanentTimes with bookedTime to create the availableTimes array. Using this have a list of times to create a true match rather than false, meaning only one button can ever match this and ensure the correct times are made available
#### Verdict
This bug was fixed and the correct times are made available to the user

### Booking query not working on single digit days

#### Bug
I tried to make a booking on days in early September and confirmed there were bookings in the database, but all times were made available. I realised while I had accounted for single digit months I had not done so for the days, so the query to the database was incorrect
#### Fix
Add the same process to the month by converting the date to a string and adding a 0 if the length is 1. Since I was using this twice I made it a function called addZero and call it inside the function to create the query
#### Verdict
This bug was fixed and the correct queries are sent to the database


### Checkout caused crash when not logged in

#### Bug
When created a cart while not logged in, clicking checkout caused a server crash because it was not set up to handle anonymous checkouts
#### Fix
I added a login required decorator to the checkout view. While this worked fine, it left the user wondering why they were suddenly on a login page and not at the checkout. So I created a custom function that returns the checkout view, which also creates a Django message informing the user why this occured
#### Verdict
This bug was fixed and the checkout does not crash


### Deleting repeat items from the cart

#### Bug
If a user has made purchases before and creates a cart when logged out, and then logs in through the checkout redirect, there is a system to remove products they have already purchased. It was working but would return after the first item found, even if they had multiple repeat items
#### Fix
To fix this I created a list called duplicate products and appended any id of a product they have already purchased. Then looping over this array will remove any matches, guaranteeing the only items removed are duplicates
#### Verdict
This bug is fixed and the user is unable to add repeat purchases to their cart

### Microsoft Edge css 'content: url' property

#### Bug
Images on the navbar and index page were not displayed properly because Edge does not recognise this property
#### Fix
Using Bootstrap utility classes I have created multile image elements that display based on media queries, allowing the images to be responsive on all major browsers
#### Verdict
This bug is fixed and the images change for different screen sizes
