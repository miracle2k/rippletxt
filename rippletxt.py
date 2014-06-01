__all__ = ('loads', 'get_urls')


def loads(s):
    """Parse the ripple.txt file, return a dict of lists.
    """
    current_section = ""
    sections = {}
    for line in s.splitlines():
        if not line or line.startswith('#'):
            continue
        if line.startswith('[') and line.endswith(']'):
            current_section = sections.setdefault(line[1:-1], [])
            continue
        line = line.strip()
        if line:
            current_section.append(line)
    return sections


def get_urls(domain):
    """Return ripple.txt candidate urls for the domain."""
    return map(lambda s: s.format(domain=domain), [
        # https://ripple.com/wiki/Ripple.txt
        'https://ripple.{domain}/ripple.txt',
        'https://www.{domain}/ripple.txt',
        'https://{domain}/ripple.txt',
    ])