# Note

- Some points


---
@ref
- NR-Django

---
## About Django
- Django, Web Application framework
- DTL: Django Template Language
- MVT = MCV (~MVC), Model = Model, View = Controller, Template = View


---
## Django Project Structure
- Django Project Structure
>https://djangobook.com/mdj2-django-structure/

---
## create project
- => python3 manage.py startproject proj_name
- create files on system
> + proj_name [dir]
>> + proj_name [dir]
>> - __init__.py
>> - settings.py
>> - urls.py
>> - wsgi.py
> - manage.py
> - db.sqlite3


---
## create application
- => python3 manage.py startapp app_name
- create files on system
> + app_name [dir]  
>> + migrations [dir]
>> - __init__py
> - __init__.py
> - admin.py
> - apps.py
> - models.py
> - tests.py
> - views


---
## Template Ref
- Google Search: travello colorlib
>https://colorlib.com/wp/template/travello/


---
### install postgreSQL database adapter
- => pip install psycopg2


### pillow : python imaging library
- when you work related to images, upload, download ...
- => pip install pillow


## make migration
- => python3 manage.py makemigrations
- create 0001_initial.py file (webs/migrations/0001_initial.py)
- create migration files, Not migrate something
- op:
```
    Migrations for 'webs':
      webs/migrations/0001_initial.py
        - Create model Destination
```

### sqlmigrate
- migrate something
- => python3 manage.py sqlmigrate webs 0001
- op:
```
BEGIN;
--
-- Create model Destination
--
CREATE TABLE "webs_destination" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "img" varchar(100) NOT NULL, "desc" text NOT NULL, "offer" boolean NOT NULL);
COMMIT;

```

## migrate
- => python3 manage.py migrate
- make tables in database / schema
- op
```
ashish@ashish-Vostro-3478:projtest$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, webs
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  Applying webs.0001_initial... OK
```

---
# Note for Developer

- Road map of project.. or
- Some milestone..
