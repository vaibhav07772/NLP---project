from transformers import pipeline

# Load pre-trained BERT QA pipeline
qa_pipeline = pipeline("question-answering")

# Define context paragraph
context = """
Vaibhav Singh is a data science student from Reena Mehta College, Mumbai. 
He is passionate about NLP and building AI tools like chatbots and summarizers.
"""

# Ask question
question = "Where does Vaibhav study?"

# Get answer
result = qa_pipeline(question=question, context=context)
print("Answer:", result['answer'])