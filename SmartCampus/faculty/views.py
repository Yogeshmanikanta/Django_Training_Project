from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'faculty/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'faculty/feedback.html', {'form': form})
