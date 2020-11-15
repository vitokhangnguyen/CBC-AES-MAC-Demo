export FLASK_APP=server.py
if [ "$1" = "prod" ]; then
    export FLASK_ENV=production
else
    export FLASK_ENV=development
fi
flask run