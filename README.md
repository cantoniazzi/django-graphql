# Python and GraphQL - Sample project

This project is a sample using Python (Django and Graphene) and GraphQL. 

## How to configure and run the project locally

### Create a virtualenv:
```
cd <repo-path>
virtualenv -p python3 venv
```

### Activating the environment (**always** do this before performing any other actions):  
```
cd <repo-path>
source venv/bin/activate
```

### Installing dependencies:  
```
cd <repo-path>
source venv/bin/activate
pip install -r requirements/dev.txt
```
### Execute migrations:
```
cd <repo-path>
source venv/bin/activate
python manage.py migrate
python manage.py migrate ingredients

```

### Load data sample to test
```
cd <repo-path>
source venv/bin/activate
python manage.py loddata ingredients
```

### Running dev server:  
```
cd <repo-path>
source venv/bin/activate
python manage.py runserver
# do not terminate/close
```
