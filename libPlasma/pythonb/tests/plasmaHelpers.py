import re
from plasma import pool

def validate_name(name):
    if len(name) < 1:
        raise PoolInvalidName(name, 'must not be an empty string')
    if len(name) > 100:
        raise PoolInvalidName(name, 'must be no more than 100 characters')
    parsed = pool.__parse_name(name)
    first = True
    for comp in parsed['components']:
        if first and comp == 'local:':
            first = False
            continue
        first = False
        if len(comp) == 0:
            raise PoolInvalidName(name, 'pool components must not be empty strings')
        if comp.startswith('.'):
            raise PoolInvalidName(name, 'pool components may not start with "."')
        if comp.endswith('.'):
            raise PoolInvalidName(name, 'pool components may not end with "."')
        if comp.endswith(' '):
            raise PoolInvalidName(name, 'pool components may not end with a space')
        if comp.endswith('$'):
            raise PoolInvalidName(name, 'pool components may not end with "$"')
        if re.match(r"[^ \\!\\#\\$\\%\\&'\\(\\)\\+,\\.0123456789;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ\\[\\]\\^_`abcdefghijklmnopqrstuvwxyz\\{\\}~\\-", comp):
            raise PoolInvalidName(name, "pool components may only contain the following characters:  !#$%&'()+,-.0123456789;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{}~")
        m = re.match('^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?')
        if m:
            if m.group(2):
                raise PoolInvalidName(name, 'pool components may not begin with "%s."' % m.group(1))
            raise PoolInvalidName(name, 'pool component may not be %s' % comp)
    return parsed

### end ###
