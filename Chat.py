#-*- coding: utf-8 -*-
import requests
import time
import json

# sk-proj-jaFGFErS1eBqy0xzPv10T3BlbkFJL9UiAqMn3VCiPVv2G8VO

from openai import OpenAI
import streamlit as st

input_text = ''
# with open('Input.txt', 'r') as file:
#         input_text = file.read().replace('\n', '')

st.title("GST CHAT ADVISOR")

input_text = st.text_input("Ask your Question")

client = OpenAI(api_key='sk-proj-jaFGFErS1eBqy0xzPv10T3BlbkFJL9UiAqMn3VCiPVv2G8VO')



def main():   

    assistantID = 'asst_t7LBOt47IX6A1QAo0vluiLSP'

    if input_text:
      thread = client.beta.threads.create(
        messages=[
          {
            "role": "user",
            "content": input_text,
            
          }
        ]
      )

      run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id= assistantID)

      while run.status!='completed':

          run = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id= run.id)
          
          time.sleep(1)
      else:
          time.sleep(1)
          

      # Retrieve the message object
      message_list = client.beta.threads.messages.list(thread_id = thread.id)

      messages = message_list.data

      latest_message = messages[0]

      if latest_message:

        latest_message_text = latest_message.content[0].text.value

        if latest_message_text:
          st.text_area(latest_message_text,height=50)
          # open("Output.txt", "w").close()
          # with open("Output.txt","w", encoding="utf-8") as f:
          #   f.write(latest_message_text)
      else:
          st.write("Sorry Didnt Get Anything")

      




if __name__ == '__main__':
    main()



