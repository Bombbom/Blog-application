# Django-Blog-Application
> [!NOTE]
> Overview: A blog application was designed and developed to allow users to efficiently explore and view detailed posts. Included features like SEO-friendly URLs, pagination, and a comment system to boost user engagement. A third-party tagging system was integrated for enhanced content categorization, and full-text search was implemented to improve search functionality. The application was deployed using Docker Compose.


## Requirements
| Packages | Description |
|----------|-------------|
| [`python-decouple`](https://pypi.org/project/python-decouple/)| This library simplifies the use of environment variables in the projects|
| `psycopg` | Psycopg is a popular Python library for connecting to and working with PostgreSQL databases.|
| `pillow` |
| `Markdown`|
| `django-taggit`|
| `django-extensions`| 
| `django-debug-toolbar` | 


## Run project in local development
```bash
# Setup database (PostGreSQL and create .env file)
git clone https://github.com/Bombbom/Blog-application.git
pip install -r requirements.txt
cd mysite/
python3 manage.py runserver --settings=mysite.settings.local
```
## Quick deploy
```bash
git clone https://github.com/Bombbom/Blog-application.git
docker compose up
```
## Project Explanation Overview
- Project name: `mysite`
- Project application: `account`, `blog`
- Account:
  - login
  - logout
  - change password
  - reset password
  - register 
  - edit account profiles
- Blog
  - Model: Post, Comment, Tag (third-party Models), ...
  - View all post 
  - View detail post
  - Search post 
  - Create Post 
  - ....
## Features demo

![alt text](Image/admin.png)

![alt text](Image/register.png)

![alt text](Image/login.png)

![alt text](Image/edit_account.png)

![alt text](Image/change_password.png)

![alt text](Image/logged_out.png)

![alt text](Image/post_lists.png)

![alt text](Image/post_detail.png)

![alt text](Image/create_post.png)

![alt text](Image/search.png)

![alt text](Image/comment.png)

## Security Features
- [ ] TODO:
## Testing Results
- [ ] TODO:
## Getting help

## Resources 