from django import template

register = template.Library()

@register.simple_tag
def allowed(value):
    return "Allowed" if value > 13 else "Blocked"

@register.simple_tag
def fizzbuzz(value):
    output = ""
    if(value % 3 == 0):
        output += 'Bizz'
    if(value % 5 == 0):
        output += 'Fuzz'
    if(output == ""):
        output += str(value)
    return output
