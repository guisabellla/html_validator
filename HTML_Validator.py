#!/bin/python3


def validate_html(html):
    '''
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    try:
        tags = _extract_tags(text)
    except ValueError:
        return False

    stack = []

    for tag in tags:
        if tag.startswith('</'):
            name = tag[2:-1]

            if len(stack) == 0:
                return False

            if stack[-1] != name:
                return False

            stack.pop()
        else:
            name = tag[1:-1]
            stack.append(name)

    return len(stack) == 0
    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the stack.py file.
    # The main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags.


def _extract_tags(html):
    '''
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    i = 0

    while i < len(text):
        if text[i] == '<':
            close = text.find('>', i + 1)

            if close == -1:
                raise ValueError('found < without matching >')

            tag = text[i + 1:close]

            if tag.startswith('/'):
                name = tag[1:].split()[0]
                tags.append('</' + name + '>')
            else:
                name = tag.split()[0]
                tags.append('<' + name + '>')

            i = close + 1
        else:
            i += 1

    return tags
