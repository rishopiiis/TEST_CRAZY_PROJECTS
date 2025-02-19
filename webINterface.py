from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    response = get_answer(user_query)  # Call the RAG function
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)
