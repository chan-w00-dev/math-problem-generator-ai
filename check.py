import google.generativeai as genai

# [중요] 여기에 API 키를 넣어주세요
genai.configure(api_key="AIzaSyCzBGCikjyRUyHlpe2JxlkFZGpEs3VCYGc") 

print("--- 내 API 키로 사용 가능한 모델 목록 ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"오류 발생: {e}\n(API 키가 정확한지, 인터넷이 연결되었는지 확인해주세요.)")