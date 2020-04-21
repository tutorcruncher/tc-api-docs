from html import escape

from harrier.config import Mode
from harrier.extensions import template
from harrier.render import resolve_url as harrier_resolve_url


@template.contextfunction
def resolve_url(ctx, path):
    # Need to reference api.tc.com for tc.com/api/
    config = ctx['config']
    if config.mode == Mode.development:
        return config.site_root_dev + harrier_resolve_url(ctx, path)
    return config.site_root + harrier_resolve_url(ctx, path)


@template.contextfunction
def js_url(ctx, path):
    return path if ctx['config'].mode == Mode.development else resolve_url(ctx, path)


@template.contextfunction
def code_line_list(ctx, file_name):
    with open('./pages/' + file_name, 'r+') as f:
        # Return as list as need length of list in jinja template
        return list(map(escape, f.readlines()))


def replace_spaces(line):
    space_count = 0
    for i, char in enumerate(line, start=1):
        if char != ' ':
            space_count = i - 1
    return escape(line).replace(' ', '&nbsp;', space_count)


@template.contextfunction
def json_line_list(ctx, file_name):
    with open('./pages/' + file_name, 'r+') as f:
        return map(replace_spaces, f.readlines())
