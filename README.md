# Cactus-Prisma-Hack
# AI-Powered Research Paper Summarization & Podcast Generation

## 📌 Overview
This project automates the process of summarizing research papers and converting the summary into AI-powered audio podcasts and presentations. The user can input a research paper, extract its text, generate a concise summary, and choose from multiple output formats, including a podcast and a PowerPoint presentation (PPT). The project offers customizable options for both podcast voice selection and PPT style.

## 🎯 Features
- **Research Paper Processing**: Takes user input for a research paper and extracts its text.
- **Summarization**: Uses BART LLM to generate a concise summary of the extracted text.
- **Podcast Generation**:
  - Converts the summary into an AI-generated voice podcast.
  - Offers **4 different voice options** for user selection.
- **Presentation Generation**:
  - Converts the summary into a PowerPoint presentation.
  - Allows users to choose between a **formal or informal** PPT style.

## 🎙️ Podcast Voice Options
Users can select from **four different AI-generated voices**:
- **Voice 1**
- **Voice 2**
- **Voice 3** 
- **Voice 4**

## 📊 PPT Style Options
Users can choose between:
- **Formal PPT** (Professional layout and tone)
- **Informal PPT** (Casual and engaging style)

## 📂 Output Files
- `elevenlabs_output.mp3` → AI-generated podcast
- `summary_presentation.pptx` → AI-generated presentation

## 🔑 API Requirements
This project uses **ElevenLabs API** for text-to-speech conversion. Ensure you have an **API key** and update `API_KEY` in the script.

## 📌 Future Enhancements
- Integration of **video generation** from the summarized content
- **Graphical abstract** creation for visual representation of research

---

