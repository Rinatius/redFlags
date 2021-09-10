from django.forms import CharField
from django.template import loader
from django_filters.fields import ModelChoiceField
from django_filters.rest_framework import DjangoFilterBackend


class NoMarkupDjangoFilterBackend(DjangoFilterBackend):
    def to_html(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)
        if filterset is None:
            return None

        for key, value in filterset.form.fields.items():
            if isinstance(value, ModelChoiceField):
                filterset.form.fields[key] = CharField(label=value.label, disabled=value.disabled,
                                                       help_text=value.help_text, required=value.required)

        template = loader.get_template(self.template)
        context = {'filter': filterset}
        return template.render(context, request)
