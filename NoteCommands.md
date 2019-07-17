# Commands
	
---
- description..
- => pwd


---
- install django
- => pip3 install django


---
- check django version
- => django-admin --version


---
- enable appn on local system
- => python3 manage.py runserver
- Hit in browser, localhost:8000


---
- create project
- (syntax) => python3 manage.py startproject proj_name
- => python3 manage.py startproject projtest


---
- create application
- (syntax) => python3 manage.py startapp app_name
- => python3 manage.py startapp calc
- => python3 manage.py startapp webs


---
- make static dir/files
- => python3 manage.py collectstatic
- create 'assets' dir..
---


---
## django help command
- => python manage.py help


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
## re-migrate
 -=> python3 manage.py makemigrations
 - create 0002_destination_price.py file (webs/migrations/0002_destination_price.py)
 - => Hit 1, Then 0
 - op:
 ```
ashish@ashish-Vostro-3478:projtest$ python3 manage.py makemigrations
You are trying to add a non-nullable field 'price' to destination without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 0
Migrations for 'webs':
  webs/migrations/0002_destination_price.py
    - Add field price to destination
```

- => python3 manage.py migrate
- op:
```
ashish@ashish-Vostro-3478:projtest$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, webs
Running migrations:
  Applying webs.0002_destination_price... OK
```


---
## Access admin feataure
- Hit localhost:8000/admin


---
## Create Super User
- => python3 manage.py createsuperuser
- op:
```
ashish@ashish-Vostro-3478:projtest$ python3 manage.py createsuperuser
Username (leave blank to use 'ashish'):       
Email address: 
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```


---
```
ashish@ashish-Vostro-3478:projtest$ python3 manage.py makemigrations
Migrations for 'webs':
  webs/migrations/0003_auto_20190716_0527.py
    - Alter field img on destination


ashish@ashish-Vostro-3478:projtest$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, webs
Running migrations:
  Applying webs.0003_auto_20190716_0527... OK
```

---
- => ashish@ashish-Vostro-3478:projtest$ python3 manage.py startapp accounts