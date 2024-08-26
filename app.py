import streamlit as st
from dotenv import load_dotenv
load_dotenv() #load all the environment variables
import google.generativeai as genai
import os

from youtube_transcript_api import YouTubeTranscriptApi

#getting the transcript data from YT videos

def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split('=')[1]
        print(video_id)
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        transcript=""
        for i in transcript_text:
            transcript+=""+i['text']

        return transcript

    except Exception as e:
        raise e

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

prompt="""You are a youtube video summarizer. you will be taking the transcript text and summarizing the entire video and 
providing the important summary in points within 250 words.Please provide the summary of the text given here."""


#getting the summary from based on prompt from the google gemini
def generate_gemini_content(transcript_text,subject):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title('youtube Transcript to Detailed Notes Converter')
youtube_link=st.text_input('Enter Youtube link')

if youtube_link:
    video_id=youtube_link.split('=')[1]
    print(video_id)
    st.image(f'http://img.youtube.com/vi/{video_id}/0.jpg',use_column_width=True)
if st.button('Get Detailed notes'):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown('Detailed markdown')
        st.write(summary)






    

