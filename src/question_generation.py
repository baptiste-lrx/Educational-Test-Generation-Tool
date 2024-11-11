from transformers import pipeline

def generate_questions(text):
    nlp = pipeline("question-generation", model="iarfmoose/t5-base-question-generator")
    questions = nlp(text)
    return [q['question'] for q in questions]
