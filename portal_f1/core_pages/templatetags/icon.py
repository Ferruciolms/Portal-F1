from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()


@register.simple_tag(name='svg_race-icon')
def svg_icon(icon_name, extra_class=''):
    svg_tag = format_html('<?xml version="1.0" encoding="utf-8"?><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 106.06 122.88" style="enable-background:new 0 0 106.06 122.88" xml:space="preserve"><g><path d="M0,4.16C0,1.86,1.86,0,4.16,0c2.3,0,4.16,1.86,4.16,4.16v6.34h94.62c1.72,0,3.12,1.4,3.12,3.12v66.8 c0,1.72-1.4,3.12-3.12,3.12H8.32v35.18c0,2.3-1.86,4.16-4.16,4.16c-2.3,0-4.16-1.86-4.16-4.16V4.16L0,4.16z M84.42,55.3h15.4V37.73 h-15.4V55.3L84.42,55.3z M82.06,77.3V57.66H64.94V77.3H82.06L82.06,77.3z M82.06,35.37V16.74H64.94v18.63H82.06L82.06,35.37z M43.1,77.3V57.66H25.97V77.3H43.1L43.1,77.3z M45.46,55.3h17.12V37.73H45.46V55.3L45.46,55.3z M43.1,35.37V16.74H25.97v18.63H43.1 L43.1,35.37z M23.62,55.3V37.73H8.43V55.3H23.62L23.62,55.3z"/></g></svg>'
        'class="icon-{name} {extra}">'
        '<use xlink:href="#{name}"></use>'
        '</svg>', name=icon_name, extra=extra_class)

    return mark_safe(svg_tag)