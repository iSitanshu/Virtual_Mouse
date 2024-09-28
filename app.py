import os
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Endpoint to trigger the Gesture_Controller.py script
@app.route('/start_camera', methods=['GET'])
def start_camera():
    try:
        script_path = os.path.abspath(r'C:\Users\Sitanshu\Virtual_Mouse\Virtual-Mouse\Gesture-Controlled-Virtual-Mouse\src\Gesture_Controller.py')

        if not os.path.exists(script_path):
            app.logger.error('Script not found at the specified path.')
            return jsonify({"message": "Script not found!"}), 404

        result = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        app.logger.info('Gesture control script started successfully.')
        return jsonify({"message": "Gesture control started successfully!"}), 200

    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({"message": f"Error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(port=5000)
