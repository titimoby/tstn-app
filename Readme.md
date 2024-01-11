serveur et examples d'apps utilisées pendant les cours à l'IPI pour les TSTN 2ème année

Avant de pouvoir utiliser l'exemple 04 qui a besoin du serveur, il faut passer par python3.10 (à cause d'une erreur avec la librairie duckdb et python 3.12.1)

sudo apt install python3.10-venv
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
