import os

from app import create_app
app = create_app()
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', debug=True, port=port)
