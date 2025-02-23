import openai

openai.api_key = "API-key"

# video_path = "test.MP4"
# audio_path = "video_audio.mp3"

# video = VideoFileClip(video_path)
# video.audio.write_audiofile(audio_path)
def generate_transcription(audio_path):
    with open(audio_path, "rb") as audio_file:
        response = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return response.text

#0.28
    # with open(audio_path, "rb") as file:
    #     response = openai.Audio.transcribe(
    #         model="whisper-1",  # 使用 Whisper 模型
    #         file=file  # 传递音频文件的二进制数据
    #     )

    # return response["text"]

def generate_study_plan(text):
    duration="2hours"
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in study planning and task organization."},
            {"role": "user", "content": f"Create a structured study plan based on the following content:\n\n{text}\n\nThe plan should be completed within {duration}."}
        ]
    )
    print(response.choices[0].message.content
)
    return response.choices[0].message.content

# text = [ "The condition for multiplying matrix  A  and matrix  B  is that the number of columns in  A  must be equal to the number of rows in  B . If  A  is an  m times n  matrix and  B  is an  n times p  matrix, then the product  C = A \times B  is an  m \times p  matrix. To compute the elements of  C , each element  C[i][j]  is obtained by multiplying the corresponding elements in the  i -th row of  A  and the  j -th column of  B , then summing them up.",
#         "Basic Properties of Matrix Multiplication Matrix multiplication satisfies the associative property, that is,  (AB)C = A(BC) . It also satisfies the distributive property,  A(B + C) = AB + AC . However, in general, matrix multiplication does not satisfy the commutative property, meaning  AB \neq BA . If matrix  I  is the identity matrix, then  AI = IA = A , and multiplying by the identity matrix does not change the matrix  A ."]
# study_plan = generate_study_plan(text)
# print("Study Plan:\n", study_plan)