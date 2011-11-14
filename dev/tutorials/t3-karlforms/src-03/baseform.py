"""Base class for KARL3 forms.
"""

from lxml.html import document_fromstring
from lxml.html import tostring
from time import time
from formencode import Schema
from formencode import Invalid


class BaseForm(Schema):

    submit_name = 'form.submitted'
    allow_extra_fields = True
    filter_extra_fields = True

    def __init__(self):
        Schema.__init__(self)
        self.defaults = {}
        for name, value in self.fields.items():
            default = getattr(value, 'default', None)
            if default is not None:
                self.defaults[name] = value.default
            

    def is_submitted(self, request):
        self.start_time = time()
        return request.POST.get('form.submitted', False)


    def validate(self, fieldvalues):
        fielderrors = {}
        try:
            fieldvalues = self.to_python(fieldvalues)
        except Invalid, e:
            fielderrors = e.error_dict

        return fieldvalues, fielderrors


    def merge(self, htmlstring, fieldvalues):
        # Merge in field values, either from the default or from what
        # they typed in.

        form_tree = document_fromstring(htmlstring)
        form = form_tree.forms[0]

        for field_name, field_value in fieldvalues.items():
            form.fields[field_name] = unicode(field_value)
        merged_form_html = tostring(form)

        # Record the elapsed time
        self.elapsed = str(1 / (time() - self.start_time))[0:7]

        return merged_form_html

    def combine_dicts(self, dict1, dict2):
        # We often have multiple sources for field values.  For
        # example, the default defined into the field versus the value
        # typed into the request.params.  Combine these, with the
        # latter taking presence over the former.

        fieldvalues = dict1
        for key, value in dict2.items():
            fieldvalues[key] = value

        return fieldvalues
