import openai

openai.api_key = "API-key"

def generate_summary(text, model="gpt-4", temperature=0.7, max_tokens=500):
    input_chunks = split_text(text)
    output_chunks = []
    for chunk in input_chunks:
        response = openai.ChatCompletion.create(  # Use ChatCompletion.create
            model=model,  # Use 'model' instead of 'engine'
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."}, # Add system role
                {"role": "user", "content": f"Summarize the following text:\n{chunk}"}  # Add user role
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stop=None
        )
        summary = response.choices[0].message['content'].strip() # Access content like this
        output_chunks.append(summary)
    return " ".join(output_chunks)

def split_text(text):  # This function remains the same
    max_chunk_size = 8000
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

text = input("Enter the text to summarize: ")
summary = generate_summary(text)
print("\n"+summary)