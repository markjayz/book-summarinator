from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = ''

@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    data = request.get_json()
    book_title = data.get('title')
    author_name = data.get('author')

    prompt = f"Generate a summary  and keypoints for the book '{book_title}' by {author_name}."
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Choose the appropriate chat model
    messages=[{"role": "system", "content": "You are a book summarizer."},
              {"role": "user", "content": prompt}]
    )
    print(response)

    summary = response['choices'][0]['message']['content']

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)