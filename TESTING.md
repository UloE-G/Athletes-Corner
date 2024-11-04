# Testing

Back to [README.md](README.md)

## Manual Testing

### Home Page
|What was tested|Result|
|---|---|
|Newsletter sign up gives confirmation|Passed|
|Shop Now button takes you too product page|Passed|
|All Nav links work|Passed|
|Athletes Corner Name loads home page|Passed|
|Shopping bag takes user to bag page|Passed|
|Staff only access nav link is visible in my account icon|Passed|
|User only access nav link is visible in my account icon|Passed|

### Product Page
|What was tested|Result|
|---|---|
|Each product specification (e.g. basketball gear/ rugby shoes) loads only that|Passed|
|Details placed into search bar loads all products with that detail|Passed|
|Back to top button works|Passed|
|Sort by categories list works|Passed|

### Product Detail Page
**Product**
|What was tested|Result|
|---|---|
|Staff only access buttons (edit/delete) visible|Passed|
|Products can be deleted|Passed|
|Clicking edit brings you to edit product page|Passed|
|Correct size selector for items (shoes or clothing) appears|Passed|
|Quantity input|Passed|
|Keep shopping button takes you bag to all products page|Passed|
|Add to bag button adds product to bag|Passed|
|Added to bag confirmation message|Passed|
|Message shows product images and total price |Passed|
|Message shows how close you are to free delivery|Passed|
|Message loads bag page link|Passed|
|Quantity can't go below 1|Passed|

**Creating Reviews**
|What was tested|Result|
|---|---|
|Review Section loads|Passed|
|Visible reviews|Passed|
|Logged in Users are only allowed to create reviews|Passed|
|Reviews successfully loads onto page|Passed|
|Reviews can be edited|Passed|
|Reviews can be deleted|Passed|
|Error messages functional|Passed|
|Confirmation messages functional|Passed|

### Returns Page
|What was tested|Result|
|---|---|
|Return error messages|Passed|
|Return confrimation messages|Passed|

### Login page
|What was tested|Result|
|---|---|
|Sign up link works|Passed|
|Username/Email error checking|Passed|
|Password error checking|Passed|
|Forgotten Password link works|Passed|
|Home page link works|Passed|
|Sign in button works|Passed|

**Logged in users**
|What was tested|Result|
|---|---|
|Staff user only link loads in my account icon|Passed|
|Logout button loads in my account icon|Passed|
|My profile page loads in my account icon|Passed|

### Logout Page
|What was tested|Result|
|---|---|
|Cancle button works|Passed|
|Logout button works|Passed|
|Logot confirmation message|Passed|

### Sign Up Page
|What was tested|Result|
|---|---|
|Sign in link works|Passed|
|Email error checking|Passed|
|Password error checking|Passed|
|Sign up button works|Passed|
|Back to login button works|Passed|
|Sign up button sends confirmation email|Passed|
|When sign up button is selected take user to a Verify Your E-mail Address page|Passed|

**Confiramtion Page**
|What was tested|Result|
|---|---|
|Confirmation page loads from email link|Passed|
|When confirm button is pressed change users email to verified (in admin page)|Passed|

### Product Management Page
|What was tested|Result|
|---|---|
|Page blocked from users without staff access (takes them to home page)|Passed|
|Blocked user get error message|Passed|
|Page loads for user with staff access|Passed|
|Product error messages checking|Passed|
|Cancle button takes user back to product page|Passed|
|Add product adds product to correct category|Passed|


### My Profile Page
|What was tested|Result|
|---|---|
|Shows order history (number, item, date and total)|Passed|
|Order number history links to order confimrmation page|Passed|
|Order confimrmation page message loads|Passed|
|Allows user to add in devliver information|Passed|

### Bag Page
|What was tested|Result|
|---|---|
|Show product image|Passed|
|Show product name|Passed|
|Show product size|Passed|
|Show product SKU|Passed|
|Show Price|Passed|
|Show subtotal|Passed|
|Show quantity|Passed|
|Allow users to update their product quantity|Passed|
|Allow users to remove their products|Passed|
|Show user how much they need for a discount (if valid)|Passed|
|Keep shopping button takes you back to product page|Passed|
|Secure Checkout takes them to checkout page|Passed|

### Checkout Page
|What was tested|Result|
|---|---|
|Order summary loads (Item, date and total)|Passed|
|Details section loads|Passed|
|Details section error handling|Passed|
|Delivery section loads|Passed|
|Delivery section error handling|Passed|
|Stripe payment loads|Passed|
|Stripe payment error handling|Passed|
|Adjust bag button takes user back to bag page|Passed|
|Complete order functional|Passed|
|Complete order loads a new page if valid|Passed|

**Checkout Success Page**
|What was tested|Result|
|---|---|
|Completed order message|Passed|
|Continue shopping button loads product page|Passed|

### Error 404 page
|What was tested|Result|
|---|---|
|Page loads when user enters invalid page|Passed|
|Return to Shop button takes user back to product page|Passed|

## Bugs

### Fixed Bugs

**Review Editing/Deletion**

- Whenever a user tried to delete or confirm edits to their review an error would come up stating that the url for the editing and deletion was not found.

- The problem came from the review.js file in the products folder.

- In the file the links to the urls in the urls.py file was incorrectly type so to solve it the correct url structure was made.

**Confirmation Emails**

- Another problem that presented itself was when a user has completed their order a no confirmation email was sent out.

- The problem came from the fact that the website was that the location of the confirmation email was in the wrong folder so to solve it the folder was moved to the correct one.

## Validation

### HTML

HTML was verified through the [W3C Markup Validation Service](https://validator.w3.org/)

|HTML Page|Result|
|---|---|
|Home Page|No Errors, 1 Warning|
|Products Page|No Errors, 3 Warnings|
|Products Detail Page|No Errors, 2 Warnings|
|Bag Page|No Errors, 4 Warnings|
|Checkout Page|No Errors, 3 Warnings|
|Checkout Success Page|No Errors, 1 Warnings|
|Returns Page|No Errors, 1 Warning|
|Register Page|No Errors, 1 Warning|
|Sign Up Page|No Errors, 1 Warning|
|Logout Page|No Errors, 1 Warning|
|Password Reset Page|No Errors, 1 Warning|
|Password Reset Done Page|No Errors, 1 Warning|
|Add Product Page|No Errors, 1 Warning, 1 Info|
|My Profile Page|No Errors, 1 Warning, 1 Info|

In total their was:

- 0 Errors

- 22 Warnings

- 2 Info

### CSS

CSS was verified through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

|CSS File|Result|
|---|---|
|base.css|No Errors, 6 Warnings|
|Checkout.css|No Errors, 0 Warnings|

In total their was:

- 0 Errors

- 6 Warnings

### Javascript

Javascript was verified through [JSHint](https://jshint.com/)

|Js File|Result|
|---|---|
|stripe_element.js|3 warnings, 2 undefined variables|
|review.js|26 warnings, 1 undefined variable|

In total their was;

- 29 Warnings,

- 3 Undefined variables

both js files were obtained through the the Code Institute "boutique-ado" and "i think therefore i blog" walkthroughs so I opted not to modify the variables.

### Python

Python was verified throught the Code Institute [Pyhton Linter](https://pep8ci.herokuapp.com/)

**Profiles Folder**

|Python File|Result|
|---|---|
|views.py|Passed|
|urls.py|Passed|
|models.py|Passed|
|forms.py|Passed|
|apps.py|Passed|

**Products Folder**
|Python File|Result|
|---|---|
|widgets.py|Passed|
|views.py|Passed|
|urls.py|Passed|
|models.py|Passed|
|forms.py|Passed|
|apps.py|Passed|
|admin.py|Passed|

**Home Folder**
|Python File|Result|
|---|---|
|views.py|Passed|
|urls.py|Passed|
|models.py|Passed|
|forms.py|Passed|
|apps.py|Passed|
|admin.py|Passed|

**Contact Folder**
|Python File|Result|
|---|---|
|views.py|Passed|
|urls.py|Passed|
|models.py|Passed|
|forms.py|Passed|
|apps.py|Passed|
|admin.py|Passed|

**Checkout Folder**
|Python File|Result|
|---|---|
|webhooks.py|Passed|
|webhook_handler.py|Passed|
|views.py|Passed|
|urls.py|Passed|
|signals.py|Passed|
|models.py|Passed|
|forms.py|Passed|
|apps.py|Passed|
|admin.py|Passed|
|init.py|Passed|

**Bag Folder**
|Python File|Result|
|---|---|
|views.py|Passed|
|urls.py|Passed|
|contexts.py|Passed|
|apps.py|Passed|

**Athletes Corner Folder**
|Python File|Result|
|---|---|
|wsgi.py|Passed|
|views.py|Passed|
|urls.py|Passed|
|settings.py|1 Error|
|asgi.py|Passed|

In total their was only 1 Error which was in the settings.py file in the athletes corner folder. 

I did not changed that error as it was their when django was installed.