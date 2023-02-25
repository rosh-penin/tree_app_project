# tree_app_project
#### Project for creating tree-view menus in django.
#### Menu is builded with 1 query to db.

## Install
You may want to do this in virtual env.
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
After running server create superuser and add your menu.  
A menu is called by:
```sh
{% draw_menu 'your_menu_slug' %}
```
There is already exists placeholder template that awaits menu with slug
```sh
'main_menu'
```

### Author: Rosh_penin
### About: Pet project. Building trees from db in templates.
