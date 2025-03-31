# LinkedIn Post Generator 🚀

Generate **LinkedIn posts** based on topic, length, and language, leveraging past writing styles for personalized content.

![alt text](./LinkedIn_Post_Gen_Streamlit.png)

## 🔹 Features  
✅ AI-powered post generation based on historical writing patterns  
✅ Customizable output (topic, length, language)  
✅ Automated data enrichment from LinkedIn post history  
✅ Fast and scalable API integration with **Groq**  

---

## 🛠 Technical Architecture  

### Stage 1: Data Collection & Enrichment  
- Collect LinkedIn posts in **JSON format**  
- Extract **valuable insights** (writing style, structure, tone)  
- Enrich data with **NLP techniques**  

### Stage 2: Post Generation  
- Input **topic, language, and length**  
- Generate **context-aware** LinkedIn posts  
- Optimize for **engagement and readability**  

---

## 🚀 Setup & Installation  

### 1️⃣ Get API Key  
Create an API key from **Groq** and set the environment variable:  

```bash
export GROQ_API_KEY=your_api_key_here
```

### 2️⃣ Install Dependencies
Ensure you have Python 3.8+, then install the required packages  
```
pip install -r requirements.txt
```

### 3️⃣ Run the Application
Start the Streamlit app  
```
streamlit run main.py
```

## 📌 Usage  

Follow these steps to generate a LinkedIn post:  

1️⃣ **Enter a topic** for your LinkedIn post.  

2️⃣ **Select post length** (Short, Medium, or Long).  

3️⃣ **Choose a language** for the output.  

4️⃣ Click **Generate**, and the app will create a **well-structured LinkedIn post** instantly!  

---
