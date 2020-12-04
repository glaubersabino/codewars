def to_camel_case(text):
    if text == '':
        return ''

    if '-' in text:
        text = text.split('-')

        for k, v in enumerate(text):
            if '_' in v:
                if k == 0:
                    new = v.split('_')
                    for key, value in enumerate(new):
                        if key != 0:
                            new[key] = value.capitalize()
                    text[k] = ''.join(new)
                else:
                    new = v.split('_')
                    for key, value in enumerate(new):
                        new[key] = value.capitalize()
                    text[k] = ''.join(new)
            else:
                if k != 0:
                    text[k] = v.capitalize()
    elif '_' in text:
        text = text.split('_')

        for k, v in enumerate(text):
            if '-' in v:
                if k == 0:
                    new = v.split('-')
                    for key, value in enumerate(new):
                        if key != 0:
                            new[key] = value.capitalize()
                    text[k] = ''.join(new)
                else:
                    new = v.split('-')
                    for key, value in enumerate(new):
                        new[key] = value.capitalize()
                    text[k] = ''.join(new)
            else:
                if k != 0:
                    text[k] = v.capitalize()

    return ''.join(text)

to_camel_case('the-cat_is-pippi')