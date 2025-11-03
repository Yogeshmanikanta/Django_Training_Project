from django.shortcuts import render
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_faculty(user):
    return user.role == 'faculty'

@login_required
@user_passes_test(is_faculty)
def faculty_dashboard(request):
    return render(request, 'faculty/dashboard.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'faculty/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'faculty/feedback.html', {'form': form})




