from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from app.form import ContactForm
from app.models import Jarvis, Model, Contact


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jarvis'] = Jarvis.objects.all()
        context['models'] = Model.objects.all()
        context['contact'] = Contact.objects.all()
        return context


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

