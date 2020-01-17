# A short description of the application and its intended user communities. This includes both regular users and administrative users.
This application is called flea market which is aimed to provide a platform for university students to sell and buy second-hand products. All the products are divided into five categories including house, car, clothing, book and other things.
The user group communities include regular student user who has the permission to post products and view all the products that others shared and administrative users who can view all products and create new products, delete and update existing selling product no matter who the owner is.

# A description of the authentication and permissions scheme that have implemented and how it corresponds to the communities described above.
First is the log-in requirement, I used the LoginRequiredMixin in Django and incorporate it into the create, update and delete views so that all the users are required to log in to view users’ personal post page and make modification about posting products, or they can only view the selling products overall.
Then for regular student user, they are only allowed to modify their own posts and view the personal post page of their own. To realize this, I have created verification condition in the template and get relevant data from view function to check if the request user’s id is the same with the post pages’ owner, if a user visit a URL of personal page which doesn’t belong to his own, the website will provide messages that “you cannot view others’ personal page”.
However, for the administrative users, they can make modification which override the owner limit. To achieve this, the view checks if the current user is an administration member and passed into the template. If the user is, then he can see an edit and delete button in every detail page of product and are allowed to make modification.

# Lists of user IDs and passwords with an explanation of how they map to the communities described above.
User: tester
Password: (secret)
Group: administration
User: student Password: (secret) Group: user

# Instructions for testing the application using the sufficient test data, user IDs, and passwords that have provided.
1. It is a good way to check database CRUD in any of the “my” page and try to create a new post or edit existing post.
Ps: for each post you may need to provide an online picture URL,
one is provided below for the convenience of testing: https://images.pexels.com/photos/106399/pexels-photo- 106399.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500
2. switch account to check that administration user could edit any post by clicking any of them in the House, Car, Clothing, Book or Other page. But normal user could only edit the post of their own in the “my” page.

# Further information that will help understand my application for the purposes of fairly and fully evaluating it.
This project is divided into six parts: The House, Car, Clothing, Book, Other and My page. And “My” is also divided into five parts including MyHouse, MyCar, MyClothing, MyBook and MyOther, each of them stores different data schema based on the product feature.
User could view all the products in the five overall pages but can only edit products in their own ‘my’ page, however administration member can override this limit.
