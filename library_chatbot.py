from flask import Flask, request, jsonify
from flask_cors import CORS
from difflib import get_close_matches

app = Flask(__name__)
CORS(app)

faq_data = {
    "carry library card": "Yes, students must carry their library card while entering the library. It serves as your identification for accessing library facilities and borrowing books.",
    "access to e-books or journals": "Yes, our college library provides access to a wide range of digital resources!\n\n✅ E-books on various subjects\n\n📑 Online journals and research papers",
    "renew a borrowed book": "Yes, you can renew a borrowed book online through the Library Management System.\n\nHere's how to do it:\n1. Log in to your Library Account on the portal.\n2. Go to 'My Borrowed Books'.\n3. Click on the 'Renew' option next to the book you'd like to extend.",
    "late return fines": "If you return a book after the due date, a fine will be charged as per the library policy.\n\n📅 Fine amount: ₹2 per day per book\n\n⏰ Fines will continue to accumulate until the book is returned.",
    "how many books can i borrow": "📚 As a student, you can borrow up to 6 books at a time using your library card. This limit helps ensure fair access to books for all students.",
    "duration of book issue": "⏳ The standard issue period for each book is 6 months. You will be informed about the exact due date for each book in your mail account. If needed, you can request a renewal before the due date by visiting the library.",
    "library timings": "🕒 Library Timings:\n\nMonday to Friday: 9:00 AM – 10:00 PM\nSaturday: 2:00 PM – 10:00 PM\nSunday: Closed\n\n📌 Please note: Hours may vary during exams or special events. Always check the latest updates on your mail account.",
    "library open during holidays": "📅 The library remains closed on public holidays and may have reduced or adjusted hours during semester breaks which will be informed on your mail."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    best_match = get_best_faq_match(user_input)
    if best_match:
        return jsonify({"response": faq_data[best_match]})
    else:
        return jsonify({"response": "Sorry, I couldn't find an answer to that question. Please contact the library staff for more information."})

def get_best_faq_match(user_input):
    questions = list(faq_data.keys())
    matches = get_close_matches(user_input, questions, n=1, cutoff=0.4)
    return matches[0] if matches else None

if __name__ == "__main__":
    app.run(debug=True)
