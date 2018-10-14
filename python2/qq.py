a = open('key_is_here_but_do_you_know_rfc4042', 'r')
b = a.read()
print utf9.utf9decode(b)
