# support de l'Atelier Python

## Attention

Certains liens pointent vers le site de [Sam et Max](http://sametmax.com/). Ce dernier a comme moto: Du code et du C*l. Dès lors, je vous invite à être extrêmement vigilent lorsque vous vous y rendez.

## documentation

**python objects** [doc](http://effbot.org/zone/python-objects.htm) qui explique la notion d'objet en python

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

### IDE VSCode (arrh M$, on t'aime aussi !)

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

### Virtual Environnement (venv)

Un *venv* (ou **V**irtual **Env**ironment) est un environnement ad-hoc créé pour installer toutes les dépendances; et ça, en dehors du système. En général, on fournit un fichier nommé ```requirements.txt``` qui liste les noms/(versions) des paquets à installer. Ces modules se téléchargent depuis  le dépôt de paquets : pypi.python.org (Pypi étant une sorte de CPAN de Perl pour Python).

Le *venv* offre une certaine souplesse à double tranchant. D'un côté, il permet d'installer des paquets indépendamment de la distribution GNU/Linux, il permet aussi de les installer sans avoir à devenir *root* et de l'autre les paquets python installés dans un *venv* n'ont pas de mécanisme de **m-à-j de sécurité** comme avec *Debian*.

De plus, cette indépendance permet de préserver un SE (Système d'Exploitation) fonctionnel. Car l'installation à travers un ```pip`` d'un paquet en tant que root peut compromettre une application packagée par le système (ça m'est déjà arrivé).

__CRÉATION__:

```bash
# en debian TODO
apt install python3-pip python3-venv
mkdir ~/ton-super-projet/
cd !$
python3 -m venv venv
# to resolve some bugs
./venv/bin/pip install --upgrade pip
```

Cela va créer un fichier venv dans ```~/ton-super-projet/``` qui comporte une pseudo racine (lib, bin, include, share). Dans le répertoire ```./venv/bin```, vous trouverez des activate, des easy_install, des pip et des python.

__UTILISATION__ :

**En modifiant le shell**. Pour ce faire, "sourcé" le fichier ```./venv/bin/activate``` correspondant à votre shell. Une fois fait:

```bash
which python
  # /home/briner/ton-super-projet/venv/bin/python

which pip
  # /home/briner/ton-super-projet/venv/bin/pip

which easy_install
  # /home/briner/ton-super-projet/venv/bin/easy_install
```

**En modifiant le bang**: Au lieu d'utiliser dans vos en-têtes de script ```#!/usr/bin/python``` vous utiliserez ```#!./venv/bin/python```

__INSTALLATION DE PACKAGES__ :

Rien de plus simple, utilise le bon pip (en sourceant ou en spécifiant le chemin ./ven/bin/pip). Et fait juste un :

**pip install <nom_de_paquet>** : pour installer le nom_de_paquet (ex pour installer *ipython* dans votre *venv*: faites: **pip install ipython**)

**pip search <motif_de_recherche>** : pour chercher un paquet.

**pip install -r requirements.txt** : pour installer toutes les dépendances listées dans requirements.txt

**pip list** : pour lister ceux qui sont installer

**pip uninstall <nom_de_paquet>** : pour désinstaller le paquet <nom_de_paquet>

les paquets installé seront mis quelque part dans *./venv*

**pip freeze** : créer une liste des paquets installé comme la commande ```list```, mais elle formate ces données pour le fichiers requirements (ex: ```pip freeze > requirements.txt```)

### Pypi (TODO to use the pypi fournit par Pierre Laroche)

Pypi est pour python ce qu'est CPAN pour Perl. C'est un dépôt central de tous les paquets (packages) publiés. Le Nexus de l'OCSIN offre une passerelle vers ces derniers accessible sur https://prod.etat-ge.ch/ctinexus/repository/pypi-all/
Help on function a in module __main__:

a()
    Ceci est la documentation de a.
    on peut mettre ici des tartines de doc

TODO: how to configure it

## type builtins

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

## fonctions builtins

### zip unzip iteritems

**zip** de list list

```python
a=[i for i in zip([1,2,3],[11,22,33])]
a
  # [(1, 11), (2, 22), (3, 33)]
type(a)
  # list
```

### filter

filtre avec une fonction lambda (chez[Sam et Max](http://sametmax.com/fonctions-anonymes-en-python-ou-lambda/) ou chez [python.org::3.7](https://docs.python.org/fr/3.7/reference/expressions.html?highlight=lambda#lambda))

```python
[i for i in filter( lambda a:a%2, [1,2,3,4,5,6,7])]
Out[14]: [1, 3, 5, 7]
```

### créer un dictionnaire depuis deux listes

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

## Object

## structure

## modules

C'est la façon courante de mettre un morceau de code dans un fichier. Le fichier à courament l'extension .py.

```bash
cat > ~/mon_module.py << EOF
#!/usr/bin/python3
# Ci-dessus est le shebang python

# ceci est un commentaire pour python

print("Bonjour à tous !")
EOF

chmod +x ~/mon_module.py
~/mon_module.py
  # Bonjour à tous !
```



## packages

TODO

## objet

TODO

### self

TODO

### init

TODO

### builtins

TODO

## control

### if

La [défintition de ```if```](https://docs.python.org/3/reference/compound_stmts.html#if) permet par exemple de faire:

```python
if x < 0:) [if statement](
  x = 0) [if statement](
  print('Negative changed to zero')
elif x == 0:
  print('Zero')
elif x == 1:
  print('Single')
else:
  print('More')
```

rien de bien spécial sous le soleil.

### for

La [définition de ```for```](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) permet de boucler sur une séquence. Notons quelle contient un ```else``` statement.

```raw
for_stmt ::=  "for" target_list "in" expression_list ":" suite
              ["else" ":" suite]
```

Le else statement est joué seulement s'il n'y a pas un ```break```

```python
break_if=6
for liste_de_chiffre in [range(1,10,2), range(9)]:
  print("")
  msg="liste de chiffre: {} > {}".format(liste_de_chiffre,list(liste_de_chiffre))
  print(msg)
  print("-"*len(msg))
  for entier in liste_de_chiffre:
    print(f"numéro: {entier}")
    if entier == break_if:
      print("numéro {} trouvé !".format(entier))
      print("on", "sort", "de", "la", "boucle", "for", "!", end="")
      print(" ".join([" Car", "le", "chiffre", str(break_if), "n'est", "pas", "sorti !"]))
      break
  else:
    print("on a joué la liste jusqu'à la fin. Car le numéo {last} n'est sorti !".format(last=break_if))
```

### while

La [défintion du ```while```](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) permet de faire la même chose que celle du for. Notons quelle a aussi la notion du ```else``` qui s'opère s'il n'y a pas de break dans la boucle.

### def : définition d'une fonction

simplement ça ce passe comme ça

```python
def a():
  '''Ceci est la documentation de a.
on peut mettre ici des tartines de doc'''
  print("Enter A")

a()
  # Enter A

print(a.__doc__)
  # Ceci est la documentation de a.
  # on peut mettre ici des tartines de doc

help(a)
  # Help on function a in module __main__:
  # a()
  #     Ceci est la documentation de a.
  #     on peut mettre ici des tartines de doc



def b(avec_parametre):
  print("Enter B")
  print(avec_parametre)

b("un paramètre inutile.")
  # Enter B
  # un paramètre inutile.

def c(premier_param, deuxieme_param):
  print("Enter C")
  print("premier:", premier_param)
  print("deuxieme:", deuxieme_param)

c(1, 2)
  # Enter C
  # premier: 1  
  # deuxieme: 2
```

On peut aussi ajouter des paramètres optionnelles

```python
def d(premier=1):
  print("Enter D")
  print(f"premier: {premier}")

d()
  # Enter D
  # premier: 1

d(3)
  # Enter D
  # premier: 3

def e(obligatoire, optionel=1):
  print("Enter E")
  print(f"arguments: {obligatoire} {optionel}")

e(12)
  # Enter E
  # arguments: 12 1

e(1,11)
  # Enter E
  # arguments: 1 11
```

Attention, il faut mettre les valeurs optionnels à la fin. Sinon, ça fait des erreurs.

```python
def f(optionel=1, obligatoire):
  print("Enter F")
  print(f"arguments: {obligatoire} {optionel}")

  # SyntaxError: non-default argument follows default argument
```

On peut aussi rendre une fonction avec des paramètres variables

```python
def g(obligatoire, *args):
  print("Enter G")
  print("params", obligatoire, *args)
  print("params", obligatoire, args)

g(1, 2, 3)
  # Enter G
  # params 1 2 3
  # params 1 (2, 3)

def h(obligatoire, reobligatoire, *args, kvdonne=1, kvredonne=2, **kv):
  print("Enter G")
  print("obli:", obligatoire, ", reobli:", reobligatoire,
        ",kvdonne:", kvdonne, "kvredonne:", kvredonne)
  print("args: ", *args)
  print("kv: ", repr(kv))

h("obli-1", "reobli 2", "optionnel1", "optionnel2")
  # Enter G
  # obli: obli-1 , reobli: reobli 2 ,kvdonne: 1 kvredonne: 2
  # args:  optionnel1 optionnel2
  # kv: {}

h("obli-1", "reobli 2", "optionnel1", "optionnel2")
  # Enter G
  # obli: obli-1 , reobli: reobli 2 ,kvdonne: 1 kvredonne: 2
  # args:  optionnel1 optionnel2
  # kv:  {}
```

### yield

C'est une sorte de return, mais qui maintient le status de la fonction

```python
def a(i):
  while i<10:
    yield(i)
    i=i+1

mon_iter=a(3)
next(mon_iter)
  # 3
next(mon_iter)
  # 4

for i in mon_iter:
  print(i)

  # 5
  # 6
  # 7
  # 8
  # 9

```

### try raise

La levée d'exception se fait à l'aide de l'outil ```raise```. L'interception d'exception à l'aide de ```try ... except```

Tout d'abord regardons comment faire pour intercepter n'importe quelles erreurs

```python
a={1:11, 2:22}
try:
  a.append({3:33})
except:
  print("On a intercepté une erreur")

  # On a intercepté une erreur

```

L'exception est un objet qu'on peut récupérer

```python

a={1:11, 2:22}
try:
  a.append({3:33})
except Exception as err:
  print("On a intercepté une erreur")
  print("err:", err)
  print("type:", type(err))

  # On a intercepté une erreur
  # err: 'dict' object has no attribute 'append'
  # type: <class 'AttributeError'>
```

On peut aussi faire un except que sur un certain type d'erreurs. Dans ce cas, on voit que l'erreur levée est de type AttributeError. On peut spécifier qu'on interecpte seulement ce type d'erreur.

```python
a={1:11, 2:22}
try:
  a.append({3:33})
except AttributeError as err:
  print("On a intercepté une erreur")

  # On a intercepté une erreur
```

et donc une erreur du type ```KeyError`` ne sera pas interceptée

```python
a={1:11, 2:22}
try:
  print(a[3])
except AttributeError as err:
  print("On a intercepté une erreur")

  # KeyError: 3
```

On peut aussi ce dire qu'on souhaite intercepté l'erreur KeyError et l'erreur AttributeError

```python
a={1:11, 2:22}
try:
  print(a[3])
except AttributeError as err:
  print("On a intercepté l'erreur du type AttributeError")
except KeyError as err:
  print("On a intercepté l'erreur du type KeyError")

  # On a intercepté l'erreur du type KeyError
```

On peut aussi imprimer l'erreur et la relancer

```python
a={1:11, 2:22}
try:
  print(a[3])
except AttributeError as err:
  print("On a intercepté l'erreur du type AttributeError")
  raise(err)
except KeyError as err:
  print("On a intercepté l'erreur du type KeyError")
  raise(err)
```

Un truc intéressant, c'est d'attraper l'erreur, de tenter de la gérer et si ça ne joue pas envoyer la pile d'appel.

```python
import sys
a={1:11, 2:22}
try:
  print(a[3])
except KeyError as err:
  print("On a intercepté l'erreur du type KeyError")
  import traceback
  exc_type, exc_value, exc_traceback = sys.exc_info()
  tb_format_exception=traceback.format_exception(exc_type, exc_value, exc_traceback)
  for mline in tb_format_exception:
    for line in mline.split("\n"):
      if line:
        print(line)

  # On a intercepté l'erreur du type KeyError
  # Traceback (most recent call last):
  #   File "<ipython-input-127-8c7b1d6b6912>", line 4, in <module>
  #     print(a[3])
  # KeyError: 3
```

### open file

À la va vite,

```python
open("/etc/passwd","r").read()
open("/etc/passwd","r").readlines()
```

À la manière juste, qui ne laissera pas de handler ouvert :

```python
with open('/etc/passwd') as f:
  for line in f.readlines():
    print(line.rstrip())

  # root:x:0:0:root:/root:/bin/bash
  # daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
  # …

f.closed
  # True
```


## lib

### argparse (Analyseur de paramètres)

C'est un package permettant de générer automagiquement les options d'un programme.

```bash
cd argparse
chmod +x example.py
./example.py --help
  # usage: example.py [-h] {utils,minion} ...
  #
  # tools to manage salt
  #
  # positional arguments:
  #   {utils,minion}  sub-command help
  #     utils         utils
  #     minion        minion
  #
  # optional arguments:
  #   -h, --help      show this help message and exit

./example.py utils --help
  # usage: example.py utils [-h] {clean,day} ...
  #
  # positional arguments:
  #   {clean,day}  utils-command
  #     clean      clean it
  #     day        print a working-day-X using apt-spread defined in
  #                /etc/test.yaml
  #
  # optional arguments:
  #   -h, --help   show this help message and exit
```

### pex

PEX signifie '''P'''ython '''EX'''ecutable. Il permet d'emballer un module/package python et touts ces dépendances dans un seul binaire. Dès lors, le déploiement est beaucoup plus simple, car dorénvant il suffit juste de faire un ```scp`` avec le chmod qui va bien.

Des examples se trouvent sur:

* [pex-01](./pex-01) pour emballer un module (un fichier) et ces dépendances pip.
* [pex-02](./pex-01) pour emballer un package (une répertoire) et ces dépendances pip.

### requests (https for human)

Le package qui a rendu l'interrogation de service http et https facile. Ci-dessous l'extrait de code du site [web](http://docs.python-requests.org/en/master/)

```python
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
  # 200
r.headers['content-type']
  # 'application/json; charset=utf8'
r.encoding
  # 'utf-8'
r.text
  # u'{"type":"User"...'
r.json()
  # {u'private_gists': 419, u'total_private_repos': 77, ...}
```

### flask

C'est une suite de librairie pour python qui permet de créer facilement des webservices en python. Comme dit dans la section documentation, je vous incite à suivre le [flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) de Miguel Grinberg.

Pour ma part, j'ai juste mis le serveur le plus petit du monde sur le répertoire [./flask/helloword.py](./flask/helloword.py) avec le [./flask/helloworld.readme](./flask/helloworld.readme) qui va avec

### functools [doc](https://docs.python.org/3.7/library/functools.html)

functools liste des fonctions outils utiles. Un décorateur permettant de:

* faire du cache
* de rendre des objets triable facilement


### black

Le problème d'indentation de code à une solution dans le package [black](https://github.com/ambv/black). Ce dernier ré-indente le code à sa manière et tous le monde est heureux.

```bash
pip install black
black {source_file_or_directory}
```

Dans l'outil VSCode, il semble être déjà intégré

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

def exe_cmd(cmd_str, do_shell=False):
    logger.debug('execute cmd(%s):' % cmd_str)
    cmd = shlex.split(cmd_str)
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=do_shell,
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
  # (0,
  #  ['total 68',
  #   'lrwxrwxrwx   1 root root     7 Oct 13 01:32 bin -> usr/bin',
  #   'drwxr-xr-x   4 root root  4096 Feb 27 15:22 boot',
  #    ...
  #  [])

exe_cmd("ls -l / | grep d")
  # ça fait une erreur

# et si on remplace shell=False par shell=True
# attention ça risque l'injection de code
exe_cmd("ls -l / | grep d", do_shell=True)
  # (0,
  #  ['bin',
  #   'boot',
  # ...
  #   'vmlinuz.old'],
  #  [])
```

### shutil

C'est un module qui facilite le travail avec les répertoires (rmtree/copytree pour supprimer/copier une arborescence, which, move...)

### pprint (pretty print)

pretty print, de façon à pouvoir imprimer joliment. C'est surtout intéressant, je 

### paramiko

pour faire du ssh natif en python

## snippet

### pdb

En zonant sur le web, je suis tombé sur des vidéos de *PyCon* (pour **Py**thon **Con**férence), dont [une qui parlait de débogage](https://www.youtube.com/watch?v=lnlZGhnULn4) à l'aide de *pdb* (**P**ython **D**é**B**oggueur).

**LANCER LE DÉBOGUEUR**

C'est le genre de truc à connaître. Peut-être pas dans les premières semaines, mais c'est un outil à acquérir.

Pour lancer le script ```/usr/local/bin/toto argument1``` en mode déboggage plusieurs choix s'offrent:

**Le lancer le package pdb** avec ```python3 -m pdb /usr/local/bin/toto argument1```

**Modifier le script** en mettant dans les imports ```import pdb``` et en insérant un ```pdb.set_trace()``` à l'endroit que l'on souhaite dans le code.

**Utiliser son IDE** pour que la magie s'installe.

**avec un runcall dans ipython**: pdb.runcall(name_of_the_function, argument_1, argument_2)

**utiliser le déboggeur**

Toutes les informations sont sur le site du package python [pdb](https://docs.python.org/3.7/library/pdb.html#debugger-commands)

* h: **h**elp
* w: **w**here montre la pile
* d: **d**own pour déscendre dans la pile
* u: **u**p pour monter dans la pile
* b: **b**reak pour mettre un point d'arrêt (b(reak) [([filename:]lineno | function) [, condition]])
* cl: **cl**ear pour supprimer un point d'arrêt.
* s: **s**tep pour avancer d'un pas. Si on invoke une fonction, on se retrouvera à la première ligne de la fonction
* n: **n**ext avance d'un pas sans rentrer dans une fonction.
* c: **c**ontinue avance jusqu'au prochait point d'arrêt.
* l: **l**list
* ll: **l**ong **l**ist ontre les prochaines lignes de code

```python
import pdb
def fsomme1(a, b, c, d):
  pdb.set_trace()
  pre_somme=fsomme2(b,c, d)
  somme=a+pre_somme
  return somme

def fsomme2(a, b, c):
  pre_somme=fsomme3(b, c)
  somme=a+pre_somme
  return somme

def fsomme3(a, b):
  pdb.set_trace()
  pre_somme=a+b
  somme=a+pre_somme
  return somme

a_sommer=[1,2,3,4]
fsomme1( *a_sommer)

# ligne pour le déboggue
## pour voir la pile d'appel
where

## pour voire une variable
## attention avec le conflit entre le nom d'une variable
## et le nom des sous-comandes du débugue.
## Si votre variable s'appelle q : quit pour le débuggue
## faite
## p q
## au lieu de q

# pour voir a ou b
p a
p b

# pour voir les arguments: a pour args
a

# pour monter dans la pile d'appel: u pour up
u

# pour descendre: d pour down
d

# pour voir ou on est dans la pile d'appel: w pour where
w
```