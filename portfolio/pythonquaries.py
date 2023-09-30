import os
import django

# Set up Django and specify the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
django.setup()

# Import the Project model from the portfolio_app
from portfolio_app.models import Project
from portfolio_app.models import Portfolio
from portfolio_app.models import Student
# Retrieve all Project objects
projects = Project.objects.all()
students= Student.objects.all()
portfolios= Portfolio.objects.all()

# Print the queryset (not the actual data)
# print(projects)
# print(students)
# print(portfolios)
students[0].name ='test'
print(students[0])
