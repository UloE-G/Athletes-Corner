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