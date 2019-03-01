# support de l'Atelier Python

## Attention

Certains liens pointent vers le site de [Sam et Max](http://sametmax.com/). Ce dernier a comme moto: Du code et du C*l. Dès lors, je vous invite à être extrêmement vigilent lorsque vous vous y rendez.

## documentation

**entrypoint** [doc](https://amir.rachum.com/blog/2017/07/28/python-entry-points/) par Amir Rachum

Excellente documentation mettant en avant la notion de "point d'entrée". Ces points d'entrées permettent de mettre une étiquette à une fonction. Et de pouvoir demander à un autre programme d'exécuter/recherches des points d'entrée.

**circular dependencies** [video de Miguel Grinbers](https://blog.miguelgrinberg.com/post/flask-webcast-3-circular-dependencies)

Lors de la création de projet avec une structure de packages complexes, on se retrouve quelques fois avec des soucis de "dépendances circulaires". Cette vidéo, un peu longue, mais intéressante montre comment sans sortir

**flask** [Flask de Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

C'est un excellent cours qui permet de mieux comprendre comment flask fonctionne, l'utilisation d'ORM, la gestion des erreurs, la gestion de la base de données..

**[Le type bytes n’est pas du text](http://sametmax.com/le-type-bytes-nest-pas-du-texte/)**

C'est un truc à lire absolument. Ça explique comment et pourquoi les commandes systèmes, qu'on tourne, rendent du types "bytes". Et que pour pouvoir les lires, on doivent faire des:

```python
out_en_bytes.encode("utf-8")
```

**blog de Sam Et Max** que je vous laisse trouver par vous même.

## OCSIN

### IDE VSCode (arrh M$ !)

Jusqu'à maintenant, j'utilisais pycharm pour travailler avec python. Mais entendant de plus en plus d'informations concernant la qualité et la disponibilité de VSCode, j'ai décidé de franchir le pas pour ce cours.

Tous les greffons pour python se trouvent sur [VSCode::Languages::Python](https://code.visualstudio.com/docs/languages/python)

**Intelissense** est l'outil qui déchire lors de la programmation. Il offre une sorte d'autocomplétion. S'il venait à ne pas venir ```Ctrl + Space```. Pour voir plus ou moins ce que ça fait, regardez la [vidéo](https://az754404.vo.msecnd.net/public/python-intellisense.mp4)

Installer la gestion de python avec le logo carré sur la gauche de votre fenềtre, puis chercher python et installer le. Avec, vous aurez un nettoyeur de code (linter).

### px (le proxy de proxy authentifié)

Px est un outil montant à la volée un proxy sur votre machine windows qui se place entre vous et le proxy de l'OCSIN. Il fait l'authentification pour vous de manière automatique et offre en contrepartie un proxy sur votre poste qui se comporte sans authentification. Dès lors, vous pouvez utiliser plus facilement:

* pip : pour installer des packages python
* atom command en cli

L'**installation** se fait de la manière suivante

```cmd
https://github.com/genotrance/px >  releases
download the px.exe

./px.exe --proxy=proxygeadm.etat-ge.ch:3128 --save
./px.exe --install
```

Dès lors quand vous sortez de session windows et que tu y rentres à nouveau, on trouvera le démon qui se sera lancé automatiquement.

À défaut, si on souhaite le lancer à la main

```cmd
./px.exe
  # qui ne rend pas la main.
```

Puis on peut simplement utiliser le proxy

```cmd
http_proxy=localhost:3128
# et / ou
https_proxy:localhost:3128
```

### Pypi

Pypi est pour python ce qu'est CPAN pour Perl. C'est un dépôt central de tous les paquets (packages) publiés. Le Nexus de l'OCSIN offre une passerelle vers ces derniers accessible sur https://prod.etat-ge.ch/ctinexus/repository/pypi-all/

TODO: how to configure it

## builtins

### integer (immutables)

Les entiers sont immuables (angl. immutables) cela signifie qu'une fois l'assignation faite, il est impossible de le modifier. La modification se fera par la création d'un nouvel objet

```python
a=1
id(a)
  # 94905267551528
a=a+1
print(a)
  # 2
id (a)
  # 94905267551504
```

On voit que l'id de a a changé. Ce n'est donc plus le même objet.

Attention, une opération entre entier doit faire un entier

```python
3/5
  # 0
```

Si on souhaite avoir une réponse comme on l'entend, il faut mettre un ```.``` à la fin du chiffre pour spécifier que c'est un ```float```

```python
type(1)
  #  int

type(1.)
  # float

3/5.
  # 0.6

3./5
  # 0.6
```

### string (immutables)

On peut écrire une chaine de caractères comme ça:

```python
"Une chaîne en guillemet."
  # 'Une chaîne en guillemet.'

'Une chaine sans accent entre apostrophe'
  # 'Une chaine sans accent entre apostrophe'

a='''Une
chaine de caratere
un peu trop chainée'''

a
  # 'Une\nchaine de caratere\nun peu trop chainée'

print(a)
  # Une
  # chaine de caratere
  # un peu trop chainée

a="""une chaine
plus courte"""

a
  # 'une chaine\nplus courte'
```

Unicode ou pas, tel est la question ? (attention de bien utilisé python3)

```python
astring='Ceci est une chaîne de caractère'
type(astring)
  # str
type(astring.encode("utf-8"))
  # bytes
astring.encode("utf-8")
  # b'Ceci est une cha\xc3\xaene de caract\xc3\xa8re'
```

On remarque une sorte de préfix ```b``` pour dire que le contenu n'est pas un chaîne de caractère, mais une chaîne d'octets (b: bytes)

Dans ipython, si on tape ```a.``` puis ```TAB```, cela listera toutes les méthodes à disposition: capitalize, find, isupper…

Attention dans python les chaînes de caractères sont immuables (angl. immutables)

```python
a="Ceci est une chaîne de caractères"
id(a)
  # 139846778179344

a=a+" !"
a
  # 'Ceci est une chaîne de caractères !'
id(a)
  # 139846778177664
```

On voit donc que l'objet n'est plus le même.

### lists (mutables)

Une liste est non-immuable. Elle s'exprime de la façon suivante:

```python
a=[1, 2, 3, 4, 5, 6]
id(a)
  # 139846797831240
a.append(7)
a
  # [1, 2, 3, 4, 5, 6, 7]
id(a)
  # 139846797831240
```

Comme ou peut le voir, l'id ne change pas. C'est donc bien le même objet.

Vu que c'est immuable, quand on le passe à une fonction, la fonction si elle vient à changer la liste, elle la changera aussi en dehors. C'est comme une sorte de pointeur en C.

On peut aussi sélectionner un sous-ensemble avec des commandes du genre

```python

a=[i+1 for i in range(10)]
  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a[0:2]
  # [1, 2]
a[0:-2]
  # [1, 2, 3, 4, 5, 6, 7, 8]
a[-4:-2]
  # [7, 8]
a[-4:]
  # [7, 8, 9, 10]
```

### jeux avec un immuable ou un muable (angl. imumutable vs mutable)

Pour un cas immuable:

```python
a=1
id(a)
  # 9079008

def b(a):
  print("id : ", id(a))
  a=a+1
  print("id : ", id(a))
  return a

b(1)
  # id :  9079008
  # id :  9079040
  # 2
b(a)
  # id :  9079008
  # id :  9079040
  # 2
a
  # 1
id(a)
  9079008
```

Pour un cas muable (mutable)

```python
a=[1]
id(a)
  # 39846795992904

def b(a):
  print("id : ", id(a))
  a.append(1)
  print("id : ", id(a))
  return a

b(a)
  # id :  139846795992904
  # id :  139846795992904
  # [1, 1]
a
  # [1, 1]
id(a)
  # 139846795992904
```

Donc, si on souhaite passer un muable à une autre fonction, en s'assurant que ce dernier, quoi qu'il fasse ne viennent pas à changer le contenu de notre variable, on utilise copy

```python
a=[1, 2, 3]
id(a)
  # 139846795992904

# pour copier
b=a.copy()
id(b)
  # 139846796073736
b=a[:]
id(b)
  # 139846778258184

# si notre liste contient, elle aussi, d'autres muable (string ou dictionnaire)
# on sorter l'artillerie lourde
import copy
b=copy.copy(a)
id(b)
  # 139846796031240
```

## sets (ensemble)

Si on souhaite faire des mathématiques des ensembles. Du genre intersection: a ∩ b, le plus simple est de passer par les ensembles (angl. set)

```python
a=[1,1,2,4]
b=set(a)
b
  #  {1, 2, 4}

# pour voir toutes les méthodes des jeux
dir(b)
  # difference
  # intersection
  # …
```

### tuples

Les tuples sont des sortes de listes. Mais elles sont immuables.

```python
a=(1,1,3)
a
  # (1, 1, 3)
type(a)
  # tuple
```

### dicts

Les dictionnaires sont des objets muables. Ils sont du même genre que les listes.

```python
a={1:11,2:22,"3":"33"}
a
  # {1: 11, 2: 22, '3': '33'}
a.keys()
  # dict_keys([1, 2, '3'])
a.pop(3)
  # KeyError
a.pop("3")
  # '33'
a
  # {1: 11, 2: 22}
```

Faire une boucle for sur a

```python 
for k,v in a.items():
  print(f"{k} : {v}")

  # 1 : 11
  # 2 : 22
  # 3 : 33
```



### zip unzip iteritems

**zip** de list list

```python
a=[i for i in zip([1,2,3],[11,22,33])]
a
  # [(1, 11), (2, 22), (3, 33)]
type(a)
  # list
```

**filter** avec une fonction lambda (chez[Sam et Max](http://sametmax.com/fonctions-anonymes-en-python-ou-lambda/) ou chez [python.org::3.7](https://docs.python.org/fr/3.7/reference/expressions.html?highlight=lambda#lambda))

```python
[i for i in filter( lambda a:a%2, [1,2,3,4,5,6,7])]
Out[14]: [1, 3, 5, 7]
```

**dict** d'une list list

```python
a=dict(zip([1,2,3],[11,22,33]))
a
  # {1: 11, 2: 22, 3: 33}
```

### liste compréhensive (list comprehension)

Ça permet de jouer avec des listes de manières assez concises [[doc](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)]

```python
import os
print(os.linesep.join([ f"J'ai {i} oeufs !" for i in [1,2,3,4,5,6] if i > 2 ]))
  # J'ai 3 oeufs !
  # J'ai 4 oeufs !
  # J'ai 5 oeufs !
  # J'ai 6 oeufs !
```

## structure

## packages

TODO

## modules

TODO

## objet

TODO

### self

TODO

### init

TODO

### builtins

## control

### if

TODO

### while

TODO

### yield

TODO

### def

TODO

### for

TODO

### try raise

TODO

### open file

TODO

### decorator

TODO

## utilisation

### ipython

Un des points sympathiques de *Python* est que c'est un langage interprété. La console de base étant trop rudimentaire, on préfère *ipython* (pour **I**nteractive **python**). Sur *Debian* installez-le avec ```apt install ipython3```. Sur un venv faites un ```pip install ipython```

Du coup, vous aurez la complétion automatique, le rappel de l'historique, la capacité de faire un ```cd``` ou un ```ls```. Bref un truc utilisable au jour le jour.

Mais en plus de ça, notez l'existance des commandes:

```%cpaste``` qui permet de copier/coller un fragment de code sans avoir à rattraper les soucis d'indentation

```python
%cpaste
CTL+V
--
```

```?``` pour avoir des informations sur un objet.

```python
import requests
d={1:11,2:22}

requests?
d?
```

```%debug``` pour déboguer un appel qui a planté

```python
def plante():
  l=["a","b","c","d",1]
  for e in l:
    print("a"+e)

%debug
```

## logs

TODO

## lib

### argparse

TODO

### pex

TODO

## requests

TODO

## flask

TODO

## functools [doc](https://docs.python.org/3.7/library/functools.html)

TODO

## black

TODO

## setuptools

setuptools permet de créer des sortes d'archives python. Il y eu pas mal d'archives. Les eggs puis les wheel. En général, ces archives se déposent sur une sorte de registre en ligne. Quelque chose du genre de Pypi ou sur un registre maison du genre d'une page web.

Puis elle s'installe avec un ```pip install ce_module```

```python
from setuptools import setup

setup(
    name='mon_projet_trop_cool',
    version="0.0.1",
    author="BRINER Cédric",
    author_email="cedric.briner@etat.ge.ch",
    description="describe mon projet trop cool",
    license = "gpl3 and above",

    # list all packages:
    # this meeans that ./foo/__init__.py will exists
    # eg:
    # packages = ["foo"],

    # list all the modules
    # this means that ./foo1.py and my_pkg/foo2.py must exists
    # eg:
    # py_modules = [ "foo1", "my_pkg.foo2" ]

    # list the libraries that are required
    # eg:
    # install_requires = ["libcbr", "ug_xymon_malert"],

    # specify the entrypoints
    # "console_scripts" will create automatially script in /usr/local/bin
    # more info at:
    # https://amir.rachum.com/blog/2017/07/28/python-entry-points/
    # eg:
    # entry_points={
    #    'console_scripts': ['ug-lvmoracle = ug_lvmoracle:main'],
    #    'ch.unige.central_it.xymon.malert': ['estool = ug_estool:xymon']
    # }
)
```

## debugging

TODO

## collections

Les OrderedDict [pydoc](https://docs.python.org/3.7/library/collections.html#collections.OrderedDict) (les dictionnaires avec un ordre) permettent en une seule classe d'avoir un objet représentant un dictionnaire mais qui malgré tout maintient l'ordre dans lequel il est créé

```python
from collections import OrderedDict as DO
do=DO({1:11, 3:33, 2:22})
do.keys()
for k,v in do.items():
  print(f"{k} : {v}")

  # 1 : 11
  # 3 : 33
  # 2 : 22
```

## re

Les Expressions Régulières (angl. Régular Expression or re) permettent de chercher un motif dans une chaîne de caractère. 

```python
import re
re.findall("([0-9]+)", "Bonjour 111 Aurevoir 222")
  # ['111', '222']
re.search("\d+", "Bonjour 111 et ça va 222").group()
  # '111'
re.search(r"(?P<prenom>\w+);(?P<nom>\w+);(?P<age>\w+)", "olivier;engel;30ans;").groupdict()
  # {'prenom': 'olivier', 'nom': 'engel', 'age': '30ans'}
```

### logging

Ce fragment de code permet d'inscrire dans un journal hebdomadaire avec 4 semaines de rétention. De plus, si l'outil est lancé depuis un terminal, il affichera aussi dans le terminal. (Frais !)

```python
import os
import sys

import logging
from logging.handlers import TimedRotatingFileHandler

LOG_LEVEL = logging.DEBUG
LOG_ROTATE_PATH = os.path.expanduser("~/atelier-linux.log")

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
rh = TimedRotatingFileHandler(LOG_ROTATE_PATH, when="W0", backupCount=4)
rh.setFormatter(formatter)
logger.addHandler(rh)
if sys.stdout.isatty():
  # si lancé dans un terminal
  sh = logging.StreamHandler()
  formatter = logging.Formatter("%(message)s")
  sh.setFormatter(formatter)
  logger.addHandler(sh)

logger.info("Inscris ça dans le journal")
```

### executing shell command snippet

Attention à mettre LC_ALL=C pour que les sorties stdout/stdout soit toujours formatées de la même façon.

```python
import logging
import shlex
import subprocess
import sys
import os
import traceback
logger = logging.getLogger(__name__)

ENV = os.environ.copy()
ENV['LC_ALL'] = 'C'

def exe_cmd(cmd_str):
    logger.debug('execute cmd(%s):' % cmd_str)
    cmd = shlex.split(cmd_str)
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False,
                                cwd='/', env=ENV)
    except Exception as err:
        logger.info("cmd ({}) failed.".format(cmd_str))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_format_exception=traceback.format_exception(exc_type, exc_value
                                                       ,exc_traceback)
        logger.debug("show traceback output")
        for mline in tb_format_exception:
            for line in mline.split("\n"):
                if line:
                    logger.debug(line)
        raise err
    # si vous voulez lire stdout/stderr au fur et à mesure utiliser select
    lout = [out.decode("utf-8").rstrip("\n") for out in proc.stdout.readlines()]
    lerr = [out.decode("utf-8").rstrip("\n") for out in proc.stderr.readlines()]
    proc.communicate()
    retcode = proc.wait()
    if retcode != 0:
        logger.info("cmd str({}) returns {}".format(cmd_str, retcode))
        for err in lerr:
            logger.info(err)
    return retcode, lout, lerr
```

Then to test the code

```python
exe_cmd("ls -l")
exe_cmd("ls -l / | grep d")

# et si on remplace shell=False par shell=True
exe_cmd("ls -l / | grep d")
```

### shutil

C'est un module qui facilite le travail avec les répertoires (rmtree/copytree pour supprimer/copier une arborescence, which, move...)

### pprint (pretty print)

pour pretty print, de façon à pouvoir imprimer joliment

### paramiko

pour faire du ssh natif en python

##


TODO: *args, **kw


## snippet