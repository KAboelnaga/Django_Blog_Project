# 📌 Django Blog Project

 ## ✅ Overview
A blog platform built with Django, featuring user authentication, category subscriptions with email notifications, post interactions (like, dislike, comments), and an admin panel for full CRUD operations.


## 🔹 How To Run 



## 🚀 Main Features

### 🔹 Landing Page

### - Header
  - Login/Register links (or Logout if authenticated).
  - Admins see an additional "Manage Blog" link.


 ### - Sidebar (Categories)
  - Lists all categories with Subscribe/Unsubscribe buttons.
  - Redirects to posts filtered by category.
  - Email confirmation upon subscription.


### - Body (Top Posts)
  - Displays top posts sorted by publish date.
  - Clicking a post image redirects to its page.


### - Footer (Pagination)
  - Displays 5 posts per page with Next/Previous buttons.

![Landing Page](Blog_Screenshots/home.jpeg)



### 🔹 Authentication Pages

- **Registration Page**
  - Unique username & email validation.
  - Password confirmation.

![Registration Page](Blog_Screenshots/register.png)


- **Login Page**
  - Authenticates users.
  - Shows error message if account is blocked.

![login Page](Blog_Screenshots/login.png)



### 🔹 Post Page

 - Content: Title, Image, Content, Category, Tags, Comments.

   
![post Page](Blog_Screenshots/post.png)


### - Interactions:

  - Add comments & replies (signed-in users only).
  - Inappropriate words censored automatically (stupid → ******).
  - Like/Dislike counter .

![comments Page](Blog_Screenshots/comments.png)



### 🔹 Normal User Features

  - Doesn't have access over the admin panel
  - View posts & categories.

![user Page](Blog_Screenshots/normal_user.png)

 - Search by tag or title.

![search Page](Blog_Screenshots/search.png)


  - Like, dislike, comment, and reply (if logged in).

![search Page](Blog_Screenshots/logout_comment.png)
    


### 🔹 Admin Panel Features

  - CRUD Operations: Posts, Categories, Forbidden Words, Users.
  - User Management: Block/unblock users, promote users to admin.
  - UI: Based on AdminLTE template.

![admin Page](Blog_Screenshots/admin_panel.png)


### - Admin Can perform all CRUD operations on posts
  ![admin Page](Blog_Screenshots/crud_users.png)
  ![admin Page](Blog_Screenshots/create_post.jpeg)
### -  Admin Can perform all CRUD operations on categories
  ![admin Page](Blog_Screenshots/crud_categories.png)
### -  Admin Can perform all CRUD operations on forbidden words
   ![admin Page](Blog_Screenshots/forbidden_list.jpeg)
   ![add forbidden Page](Blog_Screenshots/add_forbidden.png)
### -  Admin Can perform all CRUD operations on users.
   ![admin Page](Blog_Screenshots/crud_users.png)
 

