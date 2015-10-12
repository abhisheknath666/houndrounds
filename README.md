# Sample Landing page Django App with survey

## **Pre-requisites**:

#### **Install django**: 
```sudo pip install django```

#### **Setup Postgres (Optional)**:
You can download the simple Postgres.app here and run it locally
http://www.postgresql.org/download/macosx/

##### **Create User and DB**:
CREATE DATABASE dbname;
CREATE USER username;
GRANT ALL PRIVILEGES ON DATABASE dbname to username;
ALTER USER username WITH PASSWORD pwd;
commit;

#### ** Edit settings.py to point to your db**: 
Navigate to /houndrounds-master/houndrounds
edit settings.py
change line 77 DATABASES to point to your DB
```DATABASES['default'] = dj_database_url.config(default='postgres://{username}@localhost:5432/{dbname}')```

### **Start Django Project server**:
Navigate to /houndrounds-master
```python manage.py runserver```
