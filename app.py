
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps and SRE Case Study</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>DevOps and SRE Case Study</h1>
            <h2>Application is Running Successfully!</h2>
            <p>Continuous Integration and Reliability Demonstration</p>
            <p>Developed by: Shivam Malode</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "DevOps-SRE-CaseStudy"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
