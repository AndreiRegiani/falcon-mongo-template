clear
cd src/
echo "Loading..."
gunicorn routes:api --reload  # live-reload
