import os
from flask import Flask, render_template

app = Flask(__name__)

# =============================
# 프로젝트 데이터 (한 번만 선언)
# =============================
PROJECTS = [
    {
        "title": "GPT 기반 감정 분석 영화 추천 챗봇",
        "desc": "사용자의 감정과 선호도를 기반으로 영화를 추천하는 GPT 기반 AI 챗봇.",
        "img": "movie.jpg",
        "link": "https://web-production-5985.up.railway.app/chatbot",
        "roles": [
            "GPT API Key 연동 및 모델 호출 기능 구현",
            "감정 분석 기반 추천 구조 설계",
            "프롬프트 엔지니어링 및 대화 흐름 최적화",
            "사용자 입력 기반 동적 영화 추천 로직 개발"
        ]
    },
    {
        "title": "YOLO + CLIP 기반 가구 추천 쇼핑몰",
        "desc": "YOLO 객체 탐지 + CLIP 임베딩 유사도 기반으로 사진 속 가구와 유사한 제품을 추천하는 AI 쇼핑몰.",
        "img": "furniture.jpg",
        "link": "https://web-production-5985.up.railway.app/chatbot",
        "roles": [
            "YOLOv8 기반 가구 탐지 기능 구현",
            "CLIP Embedding 기반 가구 유사도 분석",
            "Flask API 서버 구축 및 이미지 처리",
            "Top3 유사 가구 추천 알고리즘 개발"
        ]
    },
    {
        "title": "체스 오프닝 챗봇",
        "desc": "새로운 기술 적용을 목표로 기획 중인 개인 챗봇 프로젝트.",
        "img": "construction.jpg",
        "link": "준비 중입니다.",
        "roles": [
            "오프닝 데이터 수집/정제 예정",
            "챗봇 대화 구조 기획 중",
            "추천 알고리즘 설계 예정"
        ]
    }
]


# =============================
# 라우팅
# =============================
@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)


# =============================
# 실행
# =============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
