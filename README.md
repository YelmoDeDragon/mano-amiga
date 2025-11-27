# mano-amiga
Mano Amiga project Django



# Create New DataBase
```bash
# Start PostgreSQL
brew services start postgresql
```

```bash
# Create the DB
brew createdb your_database_name
```

# Setup PostgreSQL User (Optional)
```bash
# Create PostgreSQL User
psql postgres
```

```bash
# Setup
CREATE USER your_database_user WITH PASSWORD 'your_password';
ALTER ROLE your_database_user SET client_encoding TO 'utf8';
ALTER ROLE your_database_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_database_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_database_user;
```

# Setup Django Settings
```bash
# On mano_amiga_project/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',   # Same name as created above
        'USER': 'your_database_user',   # The user created or PostgreSQL default
        'PASSWORD': 'your_password',     # The password for the user
        'HOST': 'localhost',
        'PORT': '5432',                  # Default PostgreSQL port
    }
}
```
```bash
# Current Config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mano_amiga_db',
        'USER': 'yelmodedragon',ß
        'PASSWORD': 'qwerty159',
        'HOST': 'localhost',  # or your database host
        'PORT': '5432',       # default port for PostgreSQL
    }
}
```

# Run Migrations
```bash
# Migrations
python manage.py makemigrations
python manage.py migrate
```

# Verify Table created on DB
```bash
# Check Table
sql -U your_database_user -d your_database_name
\dt 
```
Current table: api_student

# Run Project
```bash
# Run
python manage.py runserver
```


