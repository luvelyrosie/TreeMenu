from django import template
from django.urls import reverse, NoReverseMatch
from tree_menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    items = MenuItem.objects.filter(menu=menu_name).select_related('parent').order_by('order')

    item_dict = {item.id: item for item in items}
    tree = []

    for item in items:
        if item.parent_id:
            parent = item_dict.get(item.parent_id)
            if not hasattr(parent, 'children_list'):
                parent.children_list = []
            parent.children_list.append(item)
        else:
            tree.append(item)

    active_item = find_active_item(items, current_path)

    expanded_ids = set()
    if active_item:
        parent = active_item.parent
        while parent:
            expanded_ids.add(parent.id)
            parent = parent.parent

    return {
        'menu_items': tree,
        'expanded_ids': expanded_ids,
        'active_path': current_path,
    }


def find_active_item(items, current_path):
    for item in items:
        url = get_item_url(item)
        if url == current_path:
            item.is_active = True
            return item
    return None


def get_item_url(item):
    if item.named_url:
        try:
            if item.named_url_kwargs:
                return reverse(item.named_url, kwargs=item.named_url_kwargs)
            return reverse(item.named_url)
        except NoReverseMatch:
            return item.url
    return item.url