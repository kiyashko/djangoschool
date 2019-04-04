from django import template

from menu.models import MenuItem


register = template.Library()


@register.inclusion_tag("tags/base_tags.html")
def menu_items(menu, template="tags/menu-item.html"):
    return {
        "template": template,
        "menu_items": MenuItem.objects.filter(menu__name__icontains=menu)
    }
