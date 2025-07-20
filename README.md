📌Blog Platform

✅ Overview
A blog platform built with Django, featuring user authentication, category subscriptions with email notifications, post interactions (like, dislike, comments), and an admin panel for full CRUD operations.

🚀 Features
🔹 Landing Page
Header
- Login/Register links (or Logout if authenticated).
- Admins see an additional "Manage Blog" link.

![Landing Page](screenshots/landing_page.png)

🔹 Sidebar (Categories)
Lists all categories with Subscribe/Unsubscribe buttons.

Redirects to posts filtered by category.

Email confirmation upon subscription.

🖼 Screenshot:

Body (Top Posts)
Displays top posts sorted by publish date.

Clicking a post image redirects to its page.

🖼 Screenshot:

Footer (Pagination)
Displays 5 posts per page with Next/Previous buttons.

🖼 Screenshot:

🔹 Authentication Pages
Registration Page
Unique username & email validation.

Password confirmation.

🖼 Screenshot:

Login Page
Authenticates users.

Shows error message if account is blocked.

🖼 Screenshot:

🔹 Post Page
Content: Title, Image, Content, Category, Tags, Comments.

Interactions:

Add comments & replies (signed-in users only).

Inappropriate words censored automatically (stupid → ******).

Like/Dislike counter (auto-deletes posts with >10 dislikes).

🖼 Screenshot:

🔹 Normal User Features
View posts & categories.

Search by tag or title.

Like, dislike, comment, and reply (if logged in).

🖼 Screenshot:

🔹 Admin Panel Features
CRUD Operations: Posts, Categories, Forbidden Words, Users.

User Management: Block/unblock users, promote users to admin.

UI: Based on AdminLTE template.

🖼 Screenshot:


