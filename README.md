📌Blog Platform

✅ Overview
A blog platform built with Django, featuring user authentication, category subscriptions with email notifications, post interactions (like, dislike, comments), and an admin panel for full CRUD operations.

🚀 Main Features

🔹 Landing Page

- Header
  - Login/Register links (or Logout if authenticated).
  - Admins see an additional "Manage Blog" link.


-Sidebar (Categories)
  - Lists all categories with Subscribe/Unsubscribe buttons.
  - Redirects to posts filtered by category.
  - Email confirmation upon subscription.


-Body (Top Posts)
  -Displays top posts sorted by publish date.
  -Clicking a post image redirects to its page.


-Footer (Pagination)
  - Displays 5 posts per page with Next/Previous buttons.

![Landing Page](Blog_Screenshots/home.jpeg)



🔹 Authentication Pages

-Registration Page
  - Unique username & email validation.
  - Password confirmation.

![Registration Page](Blog_Screenshots/register.jpeg)


-Login Page
  -Authenticates users.
  -Shows error message if account is blocked.

![login Page](Blog_Screenshots/login.jpeg)



🔹 Post Page

-Content: Title, Image, Content, Category, Tags, Comments.
![post Page](Blog_Screenshots/post.jpeg)


-Interactions:

  - Add comments & replies (signed-in users only).
  - Inappropriate words censored automatically (stupid → ******).
  - Like/Dislike counter .

![comments Page](Blog_Screenshots/comments.jpeg)



🔹 Normal User Features

  - Doesn't have access over the admin panel
  - View posts & categories.
  - Search by tag or title.
  - Like, dislike, comment, and reply (if logged in).

![user Page](Blog_Screenshots/normal_user.jpeg)
![search Page](Blog_Screenshots/search.jpeg)


🔹 Admin Panel Features

  - CRUD Operations: Posts, Categories, Forbidden Words, Users.
  - User Management: Block/unblock users, promote users to admin.
  - UI: Based on AdminLTE template.

![admin Page](Blog_Screenshots/admin_panel.jpeg)


- Admin Can perform all CRUD operations on posts
  ![admin Page](Blog_Screenshots/crud_users.jpeg)
  ![admin Page](Blog_Screenshots/create_post.jpeg)
-  Admin Can perform all CRUD operations on categories
  ![admin Page](Blog_Screenshots/crud_categories.jpeg)
-  Admin Can perform all CRUD operations on forbidden words
-   ![admin Page](Blog_Screenshots/orbidden_list.jpeg)
    ![admin Page](Blog_Screenshots/add_forbidden.jpeg)
-  Admin Can perform all CRUD operations on users.
   ![admin Page](Blog_Screenshots/crud_users.jpeg)
 

