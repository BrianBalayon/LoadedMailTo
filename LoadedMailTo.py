import pyperclip

def conv_space(txt):
    return txt.replace(" ", "%20")


def add_email():
    raw_add = input("Who is the main recipient (leave blank to skip): \n")
    return raw_add


def add_cc():
    raw_cc = input("Who do you want to CC (leave blank to skip): \n")
    return raw_cc


def add_bcc():
    raw_bcc = input("Who do you want to BCC (leave blank to skip): \n")
    return raw_bcc


def add_subj():
    raw_subj = input("What subject do you want to add (leave blank to skip): \n")
    return raw_subj


def add_body():
    raw_msg = input("What do you want to say (leave blank to skip): \n")
    return conv_space(raw_msg)


def make_link(add, cc, bcc, subj, body):
    ret_val = "mailto:" + add + "?"
    ret_val += "cc=" + cc
    ret_val += "&bcc=" + bcc
    ret_val += "&subject=" + subj
    ret_val += "&body=" + body
    return ret_val


def main():
    add = add_email()
    cc = add_cc()
    bcc = add_bcc()
    subj = add_subj()
    body = add_body()
    link = make_link(add, cc, bcc, subj, body)
    print("Here is your custom loaded Mailto link:\n" + link)
    pyperclip.copy(link)
    print("It has been copied to your clipboard")

if __name__ == "__main__":
    main()
