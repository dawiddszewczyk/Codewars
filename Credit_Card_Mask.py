"""Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'."""

def maskify(cc):
    new_string=""
    if len(cc) > 4:
       new_text = cc[-4:]
       for i in range(len(cc)-4):
           new_string+="#"
       new_string+=new_text
       return new_string
    else:
        return cc

print(maskify("4556364607935616")) == "############5616"
print(maskify(     "64607935616")) ==      "#######5616"
print(maskify(               "1")) ==                "1"
print(maskify(                "")) ==                 ""

# "What was the name of your first pet?"
print(maskify("Skippy"))                                   == "##ippy"
print(maskify("Nananananananananananananananana Batman!")) == "####################################man!"