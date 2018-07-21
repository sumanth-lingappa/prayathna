mapStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
outStr = ''

for letter in mapStr:
    if letter is 'y': outStr += 'a'
    elif letter is 'z': outStr += 'b'
    else: outStr += chr(ord(letter) + 2) if letter.isalpha() else letter

print outStr

