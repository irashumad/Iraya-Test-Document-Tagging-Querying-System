import re

def answer_question(question, context):
    if not context or not question.strip():
        return "No answer available."

    question_words = [
        w.lower() for w in re.findall(r"\w+", question)
        if len(w) > 2
    ]

    sentences = re.split(r'(?<=[.!?])\s+', context)
    scored = []

    for sentence in sentences:
        score = sum(1 for w in question_words if w in sentence.lower())
        if score > 0:
            scored.append((score, sentence.strip()))

    if not scored:
        return "No relevant answer found in the document."

    scored.sort(reverse=True, key=lambda x: x[0])
    best_sentences = [s for _, s in scored[:2]]

    return " ".join(best_sentences)