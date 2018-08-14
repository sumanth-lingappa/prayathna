
import config as cfg


with open("tempconfig.py","w") as fw:
    fw.write("NAME = \"{}\"\n".format(cfg.NAME))
    fw.write("COMPANY = \"{}\"\n".format(cfg.COMPANY))


from shutil import copyfile

copyfile("tempconfig.py", "config.py")

#reload(cfg)
print cfg.COMPANY
print cfg.NAME