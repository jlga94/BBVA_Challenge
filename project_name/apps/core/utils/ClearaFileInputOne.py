from django.forms import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    template_with_initial = (
        # '<div class="media-left">'
        # '   <a href="%(initial_url)s"  data-popup="lightbox">'
        # '       <img src="%(initial)s " class="img-rounded img-preview" />'
        # '   </a> '
        # '</div>'
        '%(clear_template)s <div class="media-body"> %(input)s </div>'
    )

    template_with_clear = ''
