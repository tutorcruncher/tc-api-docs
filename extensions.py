import json
from html import escape

from harrier.config import Mode
from harrier.extensions import template
from harrier.render import resolve_url as harrier_resolve_url


@template.pass_context
def resolve_url(ctx, path):
    # Need to reference api.tc.com for tc.com/api/
    config = ctx['config']
    if config.mode == Mode.development:
        return harrier_resolve_url(ctx, path)
    return config.site_root + harrier_resolve_url(ctx, path)


@template.pass_context
def js_url(ctx, path):
    return path if ctx['config'].mode == Mode.development else resolve_url(ctx, path)


@template.pass_context
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


@template.pass_context
def json_line_list(ctx, file_name):
    with open('./pages/' + file_name, 'r+') as f:
        return map(replace_spaces, f.readlines())


SUBJECT_TYPE_HREF = {
    'Job': 'services',
    'Lesson': 'appointments',
    'Client': 'clients',
    'Affiliate': 'agents',
    'Tutor': 'contractors',
    'Invoice': 'invoices',
    'Payment Order': 'payment-orders',
    'Credit Request': 'proforma-invoices',
    'Student': 'recipient',
    'Ad Hoc Charge': 'adhoccharges',
    'Application': 'tenders'
}


@template.pass_context
def get_actions(ctx):
    with open('./data/actions.json', 'r') as f:
        actions = json.load(f)

    for action in actions:
        sub_types = action.get('subject_types')
        if sub_types:
            type_data = [{'name': sub_type, 'href': SUBJECT_TYPE_HREF[sub_type]} for sub_type in sub_types]
            action['subject_types_data'] = type_data
    return actions
