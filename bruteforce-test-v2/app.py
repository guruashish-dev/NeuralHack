from flask import Flask, render_template, request, Response
import itertools
import string
import time

app = Flask(__name__)

# Define the character set (letters, digits, and special characters)
character_set = string.ascii_letters + string.digits + string.punctuation

def incremental_brute_force(username, password, char_set):
    """Attempts to brute-force the password character by character."""
    print(f"Attempting to brute force {username}'s password (Length: {len(password)})...")
    start_time = time.time()
    cracked_password = ""

    for position in range(len(password)):
        for char in char_set:
            time.sleep(0.0005)  # Simulate processing delay
            if password[position] == char:
                cracked_password += char
                yield f"Username: {username} | Found: {char} (Position {position + 1})"
                break  # Move to the next character

    end_time = time.time()
    elapsed_time = end_time - start_time
    yield f"Password cracked for {username} in {elapsed_time:.2f} seconds! ✅"
    yield f"Cracked Password: {cracked_password} 🔓"
    yield "DONE"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    username = request.args.get("username")
    password = request.args.get("password")

    if not username or not password:
        return "Missing username or password", 400

    def generate():
        for log in incremental_brute_force(username, password, character_set):
            yield f"data: {log}\n\n"

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
