# Django Commands

- All commands need to work with `cmder` under activated virtual environment

## Start a Project

### In General

```shell
django-admin startproject <project name>
```

### For Our Case
- The project name will be fixed as `config` 
- User dot notation to indicate generating project under current directory

```shell
django-admin startproject config .
```

## Start an App

### In General

```shell
python manage.py startapp <app name>
```

### Examples

```shell
python manage.py startapp core
python manage.py startapp users
python manage.py start blog
```

## Start Web Server

### Start Web Server in Default Port: 8000

```shell
python manage.py runserver
```

### Start Web Server with Speicfied IP and Port

```shell
python manage.py runserver 127.0.0.1:4000
python manage.py runserver 0.0.0.0:6000
python manage.py runserver 8001
```

## Make Migrations

- When you create and update your own models, you need to run this for generating mogration file, which includes SQL language

### Make migrations for Entire Site

```shell
python manage.py makemigrations
```

### Make Migrations for Specified App

```shell
python manage.py makemigrations users
```

### Make Migrations Without Output Data to File (Only for Testing Process)

```shell
python manage.py makemigrations --dry-run --verbosity 3
```

## Migrate

- Running migrations files to udpate database

### Migrate for Entire Site

```shell
python manage.py migrate
```

### Migrate for Specified App

```shell
python manage.py migrate users
```

## Create Super User

- Use `Enter` key to accept default username, or provide the username
- Use `Enter` key to escape the email settings, or provide the email
- Password should be at least 8 characters

```shell
python manage.py createsuperuser
<Enter>
<Enter>
mis123456
mis123456
```

## Communicate Data with Database

### Dumping Data

#### Dumping Django System Table

- Example: dump table `auth_user`

```shell
python manage.py dumpdata auth.User --format json --indent 4 > textures/users.json
```

#### Dump Data from the App Model Tables

- Example: dump table users.Profile

```shell
python manage.py dumpdata users.Profile --format json --indent 4 > textures/profiles.json
```

### Loading Data or Seeding Data

- Example

```shell
python manage.py loaddata textures/users.json
```

## Run Test

### For App

```shell
python manage.py test users/
```

## Collect Static Files

### Collect All

```shell
python manage.py collectstatic
```

### Collect with Exclude Directories

```shell
python manage.py collectstatic --noinput -i scss -i admin
```

## Access Python Shell

```shell
python manage.py shell
```

## Access Database Shell

```shell
python manage.py dbshell
```
