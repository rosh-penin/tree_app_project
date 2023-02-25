from django import template

from tree_app.models import MenuMember

register = template.Library()


def sort_dir_first(somelist: list) -> None:
    """Sort list. Directories on top, after that sort by name in alphabetic order."""
    somelist.sort(key=lambda member: (-member.dir, member.name))


def create_childs(members: list) -> None:
    """There is a need to create new attribute. Extra run on the list so its needs further polishing."""
    for member in members:
        member.childs = None


@register.inclusion_tag('tree_app/menu.html', takes_context=True)
def draw_menu(context, menu):
    """This function will fail if menu is empty."""
    members = list(MenuMember.objects.select_related('menu').select_related('parent').filter(menu__slug=menu).order_by('parent'))
    create_childs(members)

    try:
        selected_id = int(context['request'].GET[menu])
    except Exception:
        selected_id = members[0].pk

    while selected_id:
        childrens = []
        parent = None
        for member in members:
            if member.id == selected_id:
                parent = member

            elif member.parent_id == selected_id:
                childrens.append(member)

        if parent:
            parent.childs = childrens
            sort_dir_first(parent.childs)
            selected_id = parent.parent_id

        # It makes another (unnecessary) run on list but cuts it somewhat...
        [members.remove(child) for child in childrens]

    parents_root = [member for member in members if member.parent_id is None]
    sort_dir_first(parents_root)

    return {'members': parents_root, 'menu': menu}
