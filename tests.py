import rippletxt

def test_loads():
    assert rippletxt.loads("""
[domain]
example.org

[accounts]
r3THXKcb5KnJbD5M74kRdMfpoMY1ik8dQ5

[ips]
# ripple.example.org
8.46.236.185 5006
    """) == {
        'ips': ['8.46.236.185 5006'],
        'domain': ['example.org'],
        'accounts': ['r3THXKcb5KnJbD5M74kRdMfpoMY1ik8dQ5']}


def test_get_urls():
    assert rippletxt.get_urls('wasipaid.com') == [
        'https://ripple.wasipaid.com/ripple.txt',
        'https://www.wasipaid.com/ripple.txt',
        'https://wasipaid.com/ripple.txt']