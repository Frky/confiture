
from confiture import Confiture, ConfigFileError

print "[*] loading template"
confiture = Confiture("examples/templates/confiture.yaml")
print "[*] checking required files for blueberry"
try:
    confiture.check("examples/config/blueberry_ok.yaml")
    print "[*] blueberry file is correct"
except ConfigFileError as e:
    print e.message
print "[*] checking required files for banana"
try:
    confiture.check("examples/config/banana_ko.yaml")
    print "[*] banana file is correct"
except ConfigFileError as e:
    print e.message
