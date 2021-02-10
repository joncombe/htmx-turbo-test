from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    #
    path('htmx/partial/one', TemplateView.as_view(template_name='htmx/one.html')),
    path('htmx/partial/two', TemplateView.as_view(template_name='htmx/two.html')),
    path('htmx/partial/three', TemplateView.as_view(template_name='htmx/three.html')),
    path('htmx/partial/form', TemplateView.as_view(template_name='htmx/form.html')),
    path('htmx/partial/result', TemplateView.as_view(template_name='htmx/result.html')),
    re_path(r'^htmx/', TemplateView.as_view(template_name='htmx/index.html')),

    #
    path('turbo/partial/one', TemplateView.as_view(template_name='turbo/one.html')),
    path('turbo/partial/two', TemplateView.as_view(template_name='turbo/two.html')),
    path('turbo/partial/three', TemplateView.as_view(template_name='turbo/three.html')),
    path('turbo/partial/form', TemplateView.as_view(template_name='turbo/form.html')),
    path('turbo/partial/result', TemplateView.as_view(template_name='turbo/result.html')),
    re_path('^turbo/', TemplateView.as_view(template_name='turbo/index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
