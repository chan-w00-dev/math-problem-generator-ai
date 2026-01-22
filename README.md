# 🧮 AI Math Problem Generator (AI 수학 문제 생성기)

Google Gemini API를 활용하여 고등학교 수학 문제를 자동으로 생성해주는 프로젝트입니다.

## ✨ 주요 기능
- AI 기반 문제 생성: 사용자가 원하는 주제를 입력하면 Gemini가 새로운 문제를 만들어줍니다.
- 정답 및 풀이 제공: 문제와 함께 정확한 풀이 과정을 제공합니다.
- PDF 저장 (예정): 생성된 문제를 학습지 형태로 저장할 수 있습니다.

## 🛠 사용 기술 (Tech Stack)
- Language: Python 3.10+
- AI Model: Google Gemini Pro
- UI Framework: Streamlit

## 🚀 실행 방법
1. 저장소를 클론합니다.
   ```bash
   git clone [https://github.com/chan-w00-dev/math-problem-generator-ai.git](https://github.com/chan-w00-dev/math-problem-generator-ai.git)
'''   

2. 필요한 라이브러리를 설치합니다.
```bash
   pip install -r requirements.txt
```
  실행이 안되면 pip 대신 pip3 입력
  
3. .env 파일을 생성하고 API 키를 입력합니다.
    GEMINI_API_KEY=your_api_key_here

4. 앱을 실행합니다.
```bash
  steamlit run app.py
```

