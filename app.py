import os
from flask import Flask

app = Flask(__name__)

# 프로젝트 데이터
PROJECTS = [
    {"title": "Furniture AI", "img": "p1.jpg", "link": "https://..."},
    {"title": "Chatbot UI", "img": "p2.jpg", "link": "https://..."},
    {"title": "Portfolio Site", "img": "p3.jpg", "link": "https://..."},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)

PROJECTS = [
    {
        "title": "가구 쇼핑몰",
        "desc": "YOLO + CLIP 기반의 가구 추천 서비스",
        "img": "furniture.jpg",
        "link": "https://web-production-5985.up.railway.app/chatbot",
        "roles": [
            "YOLOv8 객체 탐지 모델 적용",
            "CLIP 유사도 계산 기반 추천 로직",
            "Flask 기반 API 서버 구축",
            "Top3 추천 결과 제공 기능 개발"
        ]
    },
    {
        "title": "영화 추천 챗봇",
        "desc": "GPT를 활용한 대화 기반 영화 추천 봇",
        "img": "movie.jpg",
        "link": "https://web-production-5985.up.railway.app/chatbot",
        "roles": [
            "GPT API Key 연동",
            "프롬프트 엔지니어링 설계",
            "응답 구조 설계 및 최적화",
            "사용자 질문 기반 영화 추천 로직 설계"
        ]
    },
    {
        "title": "체스 오프닝 챗봇",
        "desc": "설계 중",
        "img": "construction.jpg",
        "link": "https://google.com",
        "roles": [
            "구상 중"
        ]
    }
]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

