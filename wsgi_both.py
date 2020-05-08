from run_both import application
"""
https://stackoverflow.com/questions/35837786/how-to-run-flask-with-gunicorn-in-multithreaded-mode
gunicorn -b :5000 run_both:application --threads 5
"""