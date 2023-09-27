#### What I understand before Lecture
- Sql
- Quaries
- Stores information in a table
## Python Relationship To Databases
- [object relational mapping](ORM.md)
## Django
- [model view template](MVT.md)


## Rotate ideas on paper
- Classes
- - Collection of methods
- - Can be an object 
- - can be abstract
- - requires encapsulation
- - requires constructor
- - inheritance
- - instance variables
- - can be used on websites to create forms/websites/dialog boxes/views/etc...
- - Relationships

- Databases
- - store information
- - can retrieve information with quaries 
- - Mysqul / nosql / microsoft access
- - Table


## Project create
| Classes | Data Bases |
| -- | -- |
| Student |  Columns |
| Portfolio | Rows | 
| Project   |  Array  |

### Student Attribute
- name
- email
- degree
- graeduation date

### Portfolio Attributes
- degree
- graduation date


### Project Attributes
- image
- title
- description

### Databases
- store instance object (student)
- A table might represent:
- - Student
- - Project
- - Portfolio
- - - Columns/Rows Design Pattern
- - - - `active record`
- - - Columns
- - - - Attributes


#### Requirements:
- A student can have one portfolio
- A portfolio can have many projects
- A primary key is student id

# Django Database
- db.sqlite3
- migration
- - djangos way of propagating changes to models
- - - adding/deleting
- - - python3 manage.py migrate
- Model
- - class Student(models.Model):
- - - user = models.OneToOneField(User, null=True, <S>on_delete=models.CASCADE</S>)

```python
def 
```

### One to One Database
- Unique Correspondence
- - Each record is asscoicated with one record
- Primary and Foreign Keys
- - Foreign key references primary key
- Use cases
- - 
# Day 2 django models, Databases, Queries
- Models and Databases
- - 
- Migrations
- - Active Recored Pattern
- - When model is changed, perform Migration
- - Django provides
- - - not going to get into removing and recoding
- Routes
- - uniform resource index/list
- - http methods
- - - POST, GET, PUT, DELETE
- CRUDI

| ACTION | MEANING | HTTP | 
|  -- | -- | -- |
| CREATE | Create new instance | POST |
| Read | Retrieve resource instance | GET |
| Update | Modify existing resource | PUT |
| Delete | Destroy | DELETE|
| index | Enumerate collection | GET |

## Example of model
```python
class Student(models.Model):
    name = models.CharField(max_length=200)
    email - models.CharField("UCCS EMAIL", max_length=200)
    major = models.CharField(max_length=200, choices=MAJOR)
```
```Sql
select * from student
```
## Python shell
```python
from portfolio_app.models import Student
querySet= Student.objects.all()
print(querySet)
```

