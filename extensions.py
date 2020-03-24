from harrier.extensions import template


@template.contextfunction
def code_line_list(ctx, file_name):
    with open('./pages/' + file_name, 'r+') as f:
        return f.readlines()


def replace_spaces(line):
    space_count = 0
    for i, char in enumerate(line, start=1):
        if char != ' ':
            space_count = i - 1
    return line.replace(' ', '&nbsp;', space_count)


@template.contextfunction
def json_line_list(ctx, file_name):
    with open('./pages/' + file_name, 'r+') as f:
        return map(replace_spaces, f.readlines())

