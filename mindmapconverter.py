
import openai

from summarize import generate_summary

text = input("Enter the text to summarize: ")
summary = generate_summary(text)

openai.api_key = "API-key"

try:
    response = openai.Image.create(
        prompt="Create a visual scheme that will help me study of the following" + summary,
        n=1,
        size="1024x1024",
        response_format="url"
    )

    image_url = response['data'][0]['url']
    print(image_url)

except openai.error.OpenAIError as e:
    print(f"OpenAI API error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
# The code above uses the OpenAI Python library to generate a mind map image based on the summary of the input text. The `generate_summary` function splits the input text into chunks and uses the ChatCompletion API to generate a summary for each chunk. The `split_text` function splits the text into chunks based on sentence boundaries. The generated summary is then used as a prompt for the `images.generate` method to generate a mind map image using the DALL-E-3 model. The resulting image URL is printed to the console. You can modify the code to customize the input text, model, temperature, and other parameters as needed.




