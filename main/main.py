#This file will be used to iniate the service, and call other needed files

with open("../shared/hello_world.py") as f:
    exec(f.read())

with open("../rumf/rumf_scrapper.py") as f:
    exec(f.read())