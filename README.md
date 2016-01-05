# Confiture

> Eh oui, confiture ça commence comme configuration. 

## Confiture, c'est quoi ?

~~La confiture est une confiserie obtenue, le plus souvent, en faisant cuire dans une bassine à confiture certains fruits, éventuellement dénoyautés et coupés en morceaux, avec un poids équivalent de sucre.~~

Confiture, c'est un bout de code qui permet de tester un fichier de configuration `yaml`.
Par tester, on entend vérifier que des champs requis sont bien présents.

## Installation

```
spread confiture
```

Vraiment ? - Non.

```
pip install confiture
```

Vraiment ? - Non.

```bash
git clone git@github.com:Frky/confiture.git 
cd confiture
pip install -r requirements.txt
```

Vraiment ? - Bah oui. 

### Requirements
Ce projet nécessite `pyyaml`. 

## Utilisation

### Fichier de template
Un fichier de template est un fichier qui définit les champs que l'on veut vérifier en parsant
des fichiers de configuration. Il s'écrit aussi au format `yaml`, sous la forme suivante :

```yaml
foo:
    bar: ""
    foobar:
        foo: ""
        bar: ""

bar: ""
```

Un fichier de configuration sera conforme au fichier de template si chacun des champs spécifiés par 
le template sont présents. Ça n'empêche pas le fichier de configuration de posséder des champs
supplémentaires.


### Création d'un objet Confiture

Pour créer un objet Confiture selon un template donné :

```python
from confiture import Confiture
# conf pour confiture ou configration ?
conf = Confiture("examples/templates/confiture.yaml")
```

### Parsing d'un fichier de configuration
Une fois l'objet Confiture créé, on peut tester des fichiers de configuration yaml :

```python
# Simple test
conf.check("examples/config/blueberry_ok.py")
# Test et récupération du contenu du fichier sous forme de dictionnaire
config = conf.check_and_get("examples/config/blueberry_ok.py")
```

Si le fichier de configuration n'est pas conforme au fichier de template, une exception de type `ConfigFileError` est levée.

## Exemple

### Code
```python
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
```

### Output 
```
(confiture) > python ./example.py 
[*] loading template
[*] checking required files for blueberry
[*] blueberry file is correct
[*] checking required files for banana
*** fruit field not found -- aborting
```

## FAQ

#### Comment avez-vous eu l'idée de faire (de la) Confiture ?
*C'était un matin maladroit de septembre, au petit déjeuner. Au moment précis où j'ai commencé à me faire une tartine de Nutella.*
#### Pourquoi une documentation ?
*Parce qu'un projet sans documentation, c'est comme une confiture sans banane.*

#### Pourquoi une documentation aussi longue ?
*Parce que la documentation c'est comme la banane dans la confiture, plus il y en a mieux c'est.*

#### Pourquoi une documentation aussi longue pour un code aussi court ?
*Parce que maintenant, enfin, je peux dire que j'ai écrit UNE FOIS dans ma vie une documentation plus longue que le projet lui-même !*
