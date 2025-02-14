# Athletes Corner

Athletes Corner is a sports e-commerce created for people who are looking for sports gear, jerseys or shoes for basketball, football, and rugby. This website aims to give users a quick and easy way to search for sporting goods and see if they are worth buying.

![Athletes Corner Mockup](media/mockup.png)

[View live website here](https://athletes-corneru-cb4d865ddf18.herokuapp.com/)

## User Experience

### First Time Visitors

As a first-time visitor I want to be able to:

- Easily use the site across a wide range of devices.

- Easily find where to go for each product.
 
- Easily be able to search for products.

### Frequent Visitors

As a Frequent visitor, I want to be able to:

- Create an account.

- Save details like delivery information and order history.

- Review products.

### Site Admin

As a  site admin I want to be able to:

- Add, edit or delete products or reviews from the store using site owner-only front-end page.

## Business Model

- This business aimed to provide users with access to a range of sporting goods for Football, Basketball, and Rugby.

- The business model for Athletes Corner is B2C (Business to Customer).

- The business uses a single payment system.

- This business is an online-only store.

- A Facebook page was also created to give users multiple ways to see the store.

## Design

### Wireframes

- **Home Page**
![Home Page Wireframe](media/homepage.png)

![Mobile Home Page Wireframe](media/mobilehome.png)

- **Products Page**
![Product Page Wireframe](media/productspage.png)

![Mobile Product Page Wireframe](media/mobileproduct.png)

- **Product Details Page**
![Product Details Page Wireframe](media/productdetailspage.png)

![Mobile Product Details Page Wireframe](media/mobileproductdet.png)

- **Returns Page**
![Returns Page Wireframe](media/returnspage.png)

![Mobile Returns Page Wireframe](media/mobilereturns.png)

- **Sign In Page**
![Sign In Wireframe](media/signinwire.png)

![Mobile Sign In Wireframe](media/mobilesignup.png)

- **Sign Out Page**
![Sign Out Wireframe](media/signoutwire.png)

![Mobile Sign Out Wireframe](media/mobilesignout.png)

- **Profile Page**
![My Profile Wireframe](media/profilewire.png)

![Mobile My Profile Wireframe](media/mobileprofile.png)

- **Product Management Page**
![Product Management Wireframe](media/productmanwire.png)

![Mobile Product Management Wireframe](media/mobileproductmanage.png)

- **Bag Page**
![Bag Wireframe](media/bagwire.png)

![Mobile Bag Wireframe](media/mobilebag.png)

- **Checkout Page**
![Checkout Wireframe](media/checkoutwire.png)

![Mobile Checkout Wireframe](media/mobilecheckout.png)

- **Checkout Success Page**
![Checkout Success Wireframe](media/csuccesswire.png)

![Mobile Checkout Success Wireframe](media/mobilecheckoutsuccess.png)

- **Error 404 Page**
![Error Wireframe](media/error404page.png)

![Mobile Error Wireframe](media/mobileerror.png)

### Color Scheme
![Color Scheme](media/bgcolor.png)

- I went with this colour scheme because the color blue is usally associated with sports and I used white to help contrast between the blue, black, and grey text that will be seen throughtout the website. 

- I only chose two colors because whilst researching multiple sports websites like Footlocker, JD sports, and the Nike website a maximum of 3 different colors were present at each time.

### Database Design

![ERD Diagram](media/erd.png)

## Features

This section covers the different parts of this project and explains what the features provide the user.

### Existing Features

**Top Page**

- This will be shown on every page the user goes on.

- It contains a link to return the user to the home page(the store name).

- It contains a search bar to give users a more tailored item-finding tool.

- It contains a My Account dropdown list which contains the link to their account page and the ability to sign in, sign out, or register.

- It also contains the checkout button for when a user finishes browsing the catalog and wants to pay for their order they can click that and get sent to the checkout section

![Top Page](media/toppage.png)

**Nav Bar**

- This will be shown on every page the user goes on.

- The navbar contains the links to view all the products, a single product group (Basketball, Football, and Rugby), and specific types or products in these groups (shoes, jerseys, and gear).

- It also contains a link to a returns section if you feel like you have to return items.

- It has a link to the home page if the user wants to sign up for the newsletter.

- Below the nav bar there is a message incentivizing users to spend above $150 for free delivery. 

![Nav Bar](media/navabr.png)

**Notifactions**

- When users do specific things like checkout, add products to bags, submit a return application, sign up to the newsletter, leave a review, or edit products a notification comes up.

- This is used to give users confirmation throughout the site to not leave them questioning if they have done what they expected to do.

- There are 5 types of notifications, error, info, success, item, and warning.

*Info*

- The info is used to give users a message usually when they are doing something like editing a product.

- It will display an "Alert!" message above the text.

![Info Notification](media/info.png)

*Error*

- The error message is shown when something is unable to properly work like a failed review edit.

- It will display an "Error!" message above the text.

![Error Notification](media/error.png)

*Success*

- The success message is shown when an objective a user wants to do works e.g. signing up for the newsletter, checking out or submitting a review

- It will display a "Success!" message above the text.

![Success](media/success.png)

*Item*

- When a user adds an item to their bag a success notification will display.

- What also shows is an image of the item with the ability to go to checkout from there.

- It also shows the user how much they need to spend for the discount code to come into effect

![Item Success](media/itemsuccess.png)

*Warning*

- The warning message is only used if the stripe public key is missing.

**Profile Page**

- This page shows the users' order history and allows them to change their delivery details.

- This helps the user as it gives them easy access to find past orders and gives them the ability to quickly check out as their details will automatically be entered in the delivery field when they checkout.

![Profile Page](media/profilepage.png)

**Product Management Page**

- This page is where users with staff status can add or edit products.

- The user can describe what category, name, price, and rating the product has. 

- This is to give users with staff status a quicker and more efficent way of adding and editing products in the online store instead of going into the admin page.

![Product Mangement Page](media/prodmanpage.png)

**Sign Out Page**

- This page allows users to remove their accounts from any device.

- This helps the user as they can remove peoples ability to access their personal information if they use it on shared devices.

![Sign Out Page](media/signout.png)

**Sign In Page**

- This page allows users to enter their accounts from any device.

- This helps the user as they have ability to access their personal information if they use it on any device.

![Sign In Page](media/signinpage.png)

**Sign Up Page**

- This page allows the user to create an account for the website.

- The creation of this account is what allows the user to save their delivery information, see past order history, and create reviews.

![Sign Up Page](media/signuppage.png)

**Products Page**

- This page shows all the products available in the online store.

- It can be specialized to show items in alphabetical order (A-Z or Z-A), price (low-to-high, or high-to-low), and ratings (low-to-high, or high-to-low).

- It can only show items from a particular sport if the sport name is clicked on in the nav bar.

![Product Page](media/productpagee.png)

**Product Details Page**

The product details page had two sections:

*Product Item*
- The first thing a user see when they click on an item from the products page is an image of the item, name, rating, and description of said item.

- If the item is shoes a form comes whith shoes sizes ranging from a uk size 9 to a uk 13.

- If the item is clothes a form comes whith shoes sizes ranging from a uk size 9 to a uk 13.

- A quantity bar is also their if the user wants to add more than 1 item to their bag.

- Their button to go back to the product page or add the item into the bag.

- For users with staff access to button appears beside the ratings which allows them to edit or delete the product.

- Clicking edit brings them to the product management page for the item.

- Clicking delete instantly removes the item from the store.

![Product Detail Section](media/productdetailpaage.png)

*Product Review*

- Under the product item there is a review section.

- This allows user to give their opinions on a product for other user to see.

- Users can edit and delete their reviews.

![Reveiw Section](media/reviewsection.png)

**Returns Page**

- This page allows users to make a return item request.

- This helps user give us a good outlook on why they want to return their order.

- It also gives them a quick and easy way to find out how to return their order.

![Returns Page](media/returns.png)

**Bag Page**

- This page is for users to look over the products that they want to purchase.

- It shows them the name, price, quantity, and subtotal.

- It also give them the ability to change the product quantity amount or remove the product from the bag.

- It can also show the user how close they are to getting free delivery if they have not hit the threshold yet.

![Bag Page](media/bagpage.png)

**Checkout Page**

- This is the last page of the website before a user makes their order.

- It allows them to see their order items one more time.

- It is where the user would put their order details like name, address, email and country they reside in.

![Checkout Page](media/checkoutpage.png)

**Checkout Success Page**

- This page is used as a success page to show that the order has gone through.

-  It also give users a confirmation of their order number, date, details, and address that will be put into the system.

- The user is also shown which email address it will be sent  to.

![Checkout Success Page](media/csuccess.png)

**Error 404 Page**

- This page comes up when a user enters an invalid URL.

- It allows them to make a quick return to the website's main pages.

![Error 404 Page](media/error404.png)

**Facebook Buisness Page**

- When a user clicks on the facebook icon at the bottom of the home page it takes them to a facebook page.

- This page will be used to promote the website on another app and give them exclusive offers.

![Facebook Page](media/facebookpage.png)

### Future Features

- Wishlist was a feature that I thought of putting on my website but due to prioites other features where added instead.

- Discount codes was also another feature I thought of putting on but aswell but chose to keep it close to the MVP.

- I thought about sending emails for Newsletters and Returns but just like discounts, I chose to keep this close to the MVP.

## Testing

Testing can be found on the [TESTING.md](TESTING.md)

## Technologies Used

This project used a varitey of coding languages, tools, libraries, and frameworks to build, style, and run the app.

### Languages Used

- Python

- Javascript

- CSS

- HTML

### Libraries & Frameworks

- Asgiref 3.8.1
- Boto3 1.35.29
- Botocore 1.35.29
- Dj-database-url 0.5.0
- Django 3.2.25
- Django-allaut 0.50.0
- Django-countrie 7.2.1
- Django-crispy-form 1.14.0
- Django-extension 3.2.3
- Django-storage 1.14.4
- Gunicorn 23.0.0
- Jmespat 1.0.1
- Oauthli 3.2.2
- Pillo 10.4.0
- Psycopg 2.9.9
- PyJW 2.9.0
- Python3-openid 3.2.0
- Pytz 2024.1
- Requests-oauthlib 2.0.0
- S3transfer 0.10.2
- Sqlparse 0.5.1
- Stripe 10.10.0

### Tools

- Github
- Gitpod
- W3C HTML Validator
- W3C CSS Validator
- JSHint
- Font Awesome
- Looka

## Deployment

Three steps were used when deploying this website:

1. Creating Heroku App. 
2. Connecting Heroku to Stripe for payment configuration.
3. Connecting Heroku to Amazon Web Services to store static and media files.


**Heroku Deployment**

  1. Create an account on [Heroku](https://dashboard.heroku.com/apps).

  2. In the Heroku Dashboard click Create a new app.

  3. Type in the app name (athletes-corneru) and select a region (Europe) and click create app.

  4. Once done go to settings and click Reveal config vars.

  5. Inside config vars add the word "DATABASE_URL" to the key with a value of the database URL from the PostgreSQL that was given from Code Institute.

  6. Next add the word "SECRET_KEY" to the key with a value of the secret key you name (this key is then removed from the settings.py file).

  7. Connect the Github to the Heroku through the deploy section of the page.

  8. Finally activate automatic deploys.

**Stripe**

  1. Create an account on [Stripe](https://stripe.com/ie).

  2. In Heroku go back to settings and reveal config vars then add your Stripe public and secret key.

  3. Create a webhook endpoint and select all events.

  4. Then add your Heroku URL to the endpoint URL with the addition of /checkout/wh/ (e.g. https://xxxx.com/checkout/wh/).

  5. Go back to Heroku and add the stripe webhook endpoint secret key to the config vars.

**Amazon Web Services**

  1. Create an [AWS](https://aws.amazon.com/free/?trk=d5254134-67ca-4a35-91cc-77868c97eedd&sc_channel=ps&ef_id=Cj0KCQjw99e4BhDiARIsAISE7P8GFY3G_vJGdC1mh0Y5sLDqNP6Qx9UtDLRtse2jtjoz-v-U6FHK9RoaAl6wEALw_wcB:G:s&s_kwcid=AL!4422!3!433803620861!e!!g!!amazon%20web%20services!1680401428!67152600204&gclid=Cj0KCQjw99e4BhDiARIsAISE7P8GFY3G_vJGdC1mh0Y5sLDqNP6Qx9UtDLRtse2jtjoz-v-U6FHK9RoaAl6wEALw_wcB) account.

  2. Once created go to the S3 and create a bucket.

  3. Inside the bucket turn on static website hosting.

  4. In the permissions tab add the following to the CORS configuration:
    
    [
      {
        "AllowedHeaders": [
        "Authorization"
        ],
        "AllowedMethods": [
        "GET"
        ],
        "AllowedOrigins": [
        "*"
        ],
        "ExposeHeaders": []
      }
    ]

  5. Then go to the bucket policy generator to create a security policy for this bucket (policy type = S3 bucket policy).

  6. Then generate policy and add policy in the bucket policy editor (adding a /* to the end of resource key).

  7. Go to the access control list and give public access to everyone.

  8. Go to the IAM section.

  9. Go to group part

  10. Create a group.

  11. Go to the policy part.

  12. Create a policy.

  13. In policy creation, import the S3 Full Access policy.

  14. Add the bucket ARN into the resource section.

  15. Attach policy to the group.

  16. Go to user.

  17. Add a user.

  18. Add user to group.

  19. Get the user key and secret access key from a .csv file made when adding the user.

  20. Install boto3 and Django-storages in the workspace.

  21. Type the following code into settings.py.

    if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = ''
    AWS_S3_REGION_NAME = ''
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

  22. Add "AWS_SECRET_ACCESS_KEY" and "AWS_SECRET_ACCESS_KEY" to Heroku config vars.

  23. Add "USE_AWS" and set its value to true in the config vars.

  24. Remove "DISABLE_COLLECTSTATIC" from config vars.

  25. Create a file called "custom_storages.py" and put in the following code:
  
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION

  26. Git add and push these changes to Heroku.

  27. Go back to AWS S3 for the app and create a new folder called media.

  28. Click the media file and upload all images into it.

  29. Grant public read access to these images (under manage public permissions) and upload.

## Credits

**Layout**

- The layout was taken from the Code Institute project [Boutique-Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218).

**Reviews Form**

- The Review section layout was taken from the code institute [i think therefore i blog](https://learn.codeinstitute.net/ci_program/diplomainfullstacksoftwarecommoncurriculum).

**Logo**

- The logo was created using [Looka](https://looka.com/logo-maker/?gad_source=1&gclid=CjwKCAjwko21BhAPEiwAwfaQCBaSXuNOSQH7pCUHNiMb9HN7ELRIqC5eUdh3_e5hNUJSRkRM4QMiYhoC4acQAvD_BwE).

**Icons**

- The icons used throughout the app (My account button, Checkout button, etc) were made using [Font Awesome](https://fontawesome.com/).
