
import config as cfg


with open("tempconfig.py","w") as fw:
    fw.write("NAME = "+ """ + cfg.NAME + """ + "\n")
    fw.write("COMPANY = " + """ + "MY_COMPANY"+ """  + "\n")


from shutil import copyfile

copyfile("tempconfig.py", "config.py")

#reload(cfg)
print cfg.COMPANY
print cfg.NAME