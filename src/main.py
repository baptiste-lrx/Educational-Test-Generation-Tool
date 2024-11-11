from text_extraction import extract_text_from_pdf, extract_text_from_image
from question_generation import generate_questions
from answer_generation import generate_answers

def main():
    # Chemin vers le fichier PDF ou l'image
    file_path = '../data/sample_pdfs/exemple.pdf'
    
    # Extraire le texte
    text = extract_text_from_pdf(file_path)
    # Ou pour une image :
    # text = extract_text_from_image(file_path)
    
    # Générer les questions
    questions = generate_questions(text)
    
    # Générer les réponses
    answers = generate_answers(questions, text)
    
    # Afficher les questions et réponses
    for q, a in zip(questions, answers):
        print(f"Question: {q}")
        print(f"Réponse: {a}\n")

if __name__ == "__main__":
    main()
