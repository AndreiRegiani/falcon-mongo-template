clear
cd src/
echo "Loading..."
gunicorn routes:api --access-logfile - --reload  # live-reload (development only!)
