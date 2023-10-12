from django.forms import ModelForm
from .models import Project, Portfolio

# Create the class for the project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =('title', 'description')

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
