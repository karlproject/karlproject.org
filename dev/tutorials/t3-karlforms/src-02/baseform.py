"""Base class for KARL3 forms.
"""

from lxml.html import document_fromstring
from lxml.html import tostring
from time import time

class BaseForm:

    submit_name = 'form.submitted'
    max_age = 200

    def __init__(self, request):
        self.request = request
        self.start_time = time()

    @property
    def is_submitted(self):
        return self.request.POST.get('form.submitted', False)

    def validate(self, fieldvalues):
        """Look at various fields and update values and errors"""

        fielderrors = {}
        for f in fieldvalues.keys():
            fielderrors[f] = None
        age = self.request.POST.get('age', False)
        if age is False or age == '':
            fielderrors['age'] = 'Age is required'
        try:
            if int(age) > self.max_age:
                msg = 'Age must not be over %s' % self.max_age
                fielderrors['age'] = msg
            fieldvalues['age'] = age
        except ValueError:
            fielderrors['age'] = 'Age must be an integer'
            fieldvalues['age'] = age

        return fieldvalues, fielderrors

    def render(self, htmlstring, fieldvalues):
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
