import os

import streamlit as st
from openai import OpenAI
my_secret = st.secrets["OPENAI_API_KEY"]
#my_secret = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=my_secret)


def story_gen(prompt):
  system_prompt = """ you are a world renowned 50 years experience children storyteller. 
you will be given a concept to generate a story suitable for ages 5-7 years old. """

  response = client.chat.completions.create(model='gpt-4o-mini',
                                            messages=[
                                                {
                                                    "role": "system",
                                                    "content": system_prompt
                                                },
                                                {
                                                    "role": "user",
                                                    "content": prompt
                                                },
                                            ],
                                            temperature=1.3,
                                            max_tokens=200)
  return response.choices[0].message.content


#cover prompt
def cover_gen(prompt):
  system_prompt = """ you will given a children story books. 
  generate a prompt for a cover art that is suitable and shows off the story themes.
  the prompt will be sent to dall-e-2. """

  response = client.chat.completions.create(model='gpt-4o-mini',
                                            messages=[
                                                {
                                                    "role": "system",
                                                    "content": system_prompt
                                                },
                                                {
                                                    "role": "user",
                                                    "content": prompt
                                                },
                                            ],
                                            temperature=1.3,
                                            max_tokens=100)
  return response.choices[0].message.content


#cover art
def image_gen(prompt):
  response = client.images.generate(model='dall-e-2',
                                     prompt=prompt,
                                     size='256x256',
                                     n=1)
  return response.data[0].url


#storybook method
def storybook(prompt):
  story = story_gen(prompt)
  cover = cover_gen(story)
  image = image_gen(cover)

  st.write(image)
  st.write(story)


st.title("Storybook Generator for kids for fun")
st.divider()

prompt = st.text_area("Enter your story concept")

if st.button("Generate Storybook"):
      story = story_gen(prompt)
      cover = cover_gen(story)
      image = image_gen(cover)

      st.image(image)
      st.write(story)
