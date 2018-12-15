# Guia per a l'utilització de les dades obertes de governobert.gencat.cat

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

L'arxiu modules/socrata_tools.py conté la funció get_pandas_from_dataset_id(DatasetId)

La qual passant la id del dataset desitjat et retorna un Objecte PandasDataframe amb les dades.

Al fitxer exemple.ipynb es pot veure com utilitzar-la.

## Com instalar l'entorn d'anàlisi per treballar amb dades?

### Afegir les claus ssh al teu compte de Git

https://vperezb.github.io/add-ssh-keys-to-windows-github-gitlab/

### Clone repo

Dirigeixte a la carpeta que vulguis que contingui el projecte i executa `git clone git@github.com:vperezb/eines-governobert.git`

Si vols saber més sobre git: https://vperezb.github.io/introduction-to-git/

### Instala·la python

* Descarrega i instal·la [python3](https://www.python.org/downloads/)

### Instala·la pip

`pip` es el gestor de paquets de python, a les darreres versions de python aquest gestor ve instal·lat per defecte o pots seleccionar-ho al procés d'instal·lació marcant un checkbox que diu "Instalar también pip"

També pots instalar-lo manualment: [PIPinstall](https://pip.pypa.io/en/stable/installing/)

### Instala·la virtualenv usanutilitzant pip

`pip3 install virtualenv`

### Crea y activa l'entorn virtual

#### Mac

* `cd ruta/del/projecte` per dirigir-se a la carpeta on vols crear l'entorn
* `python3 -m virtualenv Env` per crear l'entorn dins de la ruta/del/projecte
* `source Enc/bin/activate` per activar l'entorn

#### Windows(Bash)

* `cd ruta/del/projecte` per dirigir-se a la carpeta on vols crear l'entorn
* `virtualenv --python=C:/Python36-32/python.exe Env` per crear l'entorn dins de la ruta/del/projecte (Si no es passa el paràmetre --python s'utilitzarà la versió que correspongui al path python de les variables d'entorn)
* `source Env/Scripts/activate` per activar l'entorn

### Instal·la llibreries

* `pip install -r requirements.txt`

### Inicia l'entorn de treball amb notebooks (s'obrirà al navegador)

* `jupyter lab`



