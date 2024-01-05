import requests
import PyPDF2

def pdf_to_text(path):
    with open(path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text+= page.extract_text()
    print(text)
    return text

pdf_file = './pdf-to-audiobook/name.pdf'
extracted_text = pdf_to_text(pdf_file)


CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/XrExE9yKIg1WjnnlVkGX"

data = {
    "text": extracted_text,
    "voice_settings": {
        "similarity_boost": 0.5,
        "stability": 0.5
    }
}
headers = {
    "Accept": 'audio/mpeg',
    "xi-api-key": "",
    "Content-Type": "application/json"
}
response = requests.post(url, json=data, headers=headers)


with open('./pdf-to-audiobook/output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)