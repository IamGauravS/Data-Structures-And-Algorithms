## input is like this [["john", "j1@com", ], ["raj", "r2@com"] ...]
## acount should be merged inside the mails should be in sorted order


from collections import defaultdict
from networkx.utils import UnionFind

def merge_accounts(accounts):

    uf = UnionFind()
    email_to_name = {}

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in email_to_name:
                email_to_name[email] = name
            uf.union(account[1], email)

    emails_in_same_account = defaultdict(list)
    for email in email_to_name:
        emails_in_same_account[uf[email]].append(email)

    return [[email_to_name[email]] + sorted(emails) for email, emails in emails_in_same_account.items()]

accounts = [
    ["John", "john1@example.com", "john2@doe.com", "john3@doe.com"],
    ["John", "john4@example.com", "john5@doe.com", "john6@doe.com"],
    ["Jane", "jane1@example.com", "jane2@doe.com", "jane3@doe.com"],
    ["Anon", "anon1@example.com", "anon2@doe.com", "john1@example.com"],
    ["Doe", "doe1@example.com", "doe2@doe.com", "john4@example.com"],
    ["Foo", "foo1@example.com", "foo2@doe.com", "foo3@doe.com"],
    ["Bar", "bar1@example.com", "bar2@doe.com", "jane1@example.com"],
    ["Baz", "baz1@example.com", "baz2@doe.com", "baz3@doe.com"],
    ["Qux", "qux1@example.com", "qux2@doe.com", "doe1@example.com"],
]

print(merge_accounts(accounts))