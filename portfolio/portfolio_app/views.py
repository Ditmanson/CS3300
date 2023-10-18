from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Student, Project, Portfolio
from .forms import ProjectForm, PortfolioForm
# Create your views here.



class StudentListView(generic.ListView):
    model = Student
    
class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioListView(generic.ListView):
    model = Portfolio

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'  # Specify the template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.get_object()  # Retrieve the portfolio object
        projects = Project.objects.filter(portfolio=portfolio)  # Retrieve associated projects
        context['projects'] = projects  # Pass projects to the context
        return context

def createProject(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id) 
    print("portfolio", portfolio.id)
    form = ProjectForm()
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
   
    return render(request, 'portfolio_app/project_form.html', context)



def deleteProject(request, pk):
    project = get_object_or_404(Project, pk=pk)
    portfolio_id = project.portfolio.id 
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio-detail', portfolio_id)
    context = {'project': project, 'portfolio_id': portfolio_id}  # Add 'portfolio_id' to the context
    return render(request, 'portfolio_app/delete_project.html', context)


def updateProject(request, pk):
    #portfolio = Portfolio.objects.get(pk=portfolio_id) 
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(instance=project)
    portfolio_id = project.portfolio.id
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data, instance=project)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            project.save()
            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)
    context = {'form': form} 
    return render(request, 'portfolio_app/project_form.html', context)

def updatePortfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    form = PortfolioForm(instance=portfolio)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            portfolio = form.save()
            # Assuming you have a relation to a student in your Portfolio model
            return redirect('student-detail', portfolio.student.pk)
    context = {'form': form} 
    return render(request, 'portfolio_app/portfolio_form.html', context)

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project


  
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

