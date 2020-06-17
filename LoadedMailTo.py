def add_email():
    pass


def add_cc():
    pass


def add_bcc():
    pass


def add_subj():
    pass


def add_body():
    pass


def make_link(add, cc, bcc, subj, body):
    return ""


def main():
    add = add_email()
    cc = add_cc()
    bcc = add_bcc()
    subj = add_subj()
    body = add_body()
    link = make_link(add, cc, bcc, subj, body)
    print("Here is your custom loaded Mailto link:\n", link)


if __name__ == "__main__":
    main()

