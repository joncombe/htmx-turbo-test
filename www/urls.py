from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    #
    path('htmx/', TemplateView.as_view(template_name='htmx/index.html')),
    path('htmx/partial/one', TemplateView.as_view(template_name='htmx/one.html')),
    path('htmx/partial/two', TemplateView.as_view(template_name='htmx/two.html')),
    path('htmx/partial/three', TemplateView.as_view(template_name='htmx/three.html')),
    path('htmx/partial/form', TemplateView.as_view(template_name='htmx/form.html')),
    path('htmx/partial/result', TemplateView.as_view(template_name='htmx/result.html')),

    #
    path('turbo/', TemplateView.as_view(template_name='turbo/index.html')),
    path('turbo/one', TemplateView.as_view(template_name='turbo/one.html')),
    path('turbo/two', TemplateView.as_view(template_name='turbo/two.html')),
    path('turbo/three', TemplateView.as_view(template_name='turbo/three.html')),
    path('turbo/form', TemplateView.as_view(template_name='turbo/form.html')),
    path('turbo/result', TemplateView.as_view(template_name='turbo/result.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
