from django import template
from django.db import OperationalError, ProgrammingError
from tree_menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    path = request.path if request is not None else None

    try:
        items_qs = MenuItem.objects.filter(menu=menu_name).order_by('order', 'title')
        items = list(items_qs)
    except (OperationalError, ProgrammingError):
        return {
            'menu_name': menu_name,
            'roots': [],
            'request': request,
        }

    nodes = {}
    children_map = {}

    for it in items:
        node = {
            'id': it.id,
            'title': it.title,
            'parent_id': it.parent_id,
            'order': it.order,
            'open_in_new_tab': it.open_in_new_tab,
            'resolved_url': it.get_resolved_url(),
            'children': [],
            'expanded': False,
            'active': False,
        }
        nodes[it.id] = node
        children_map.setdefault(it.parent_id, []).append(node)

    for parent_id, child_list in children_map.items():
        if parent_id is None:
            continue
        parent_node = nodes.get(parent_id)
        if parent_node:
            parent_node['children'].extend(sorted(child_list, key=lambda x: x['order']))

    roots = sorted(children_map.get(None, []), key=lambda x: x['order'])

    active_node = None
    if path:
        for node in nodes.values():
            r = node['resolved_url']
            if not r:
                continue
            if path == r or (r.endswith('/') and path.startswith(r)):
                node['active'] = True
                active_node = node
                break

    if active_node:
        cur = active_node
        while cur:
            cur['expanded'] = True
            cur = nodes.get(cur['parent_id'])
        for ch in active_node['children']:
            ch['expanded'] = True

    return {
        'menu_name': menu_name,
        'roots': roots,
        'request': request,
    }