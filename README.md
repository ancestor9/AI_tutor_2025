# AI 튜터 시스템 (MVC 아키텍처)

학생 수준을 진단하고 맞춤형 문제를 제공하는 AI 튜터 시스템입니다. MVC(Model-View-Controller) 아키텍처로 구현되었습니다.

---

## 🏗 시스템 아키텍처

### Model
- **StudentModel**: 학생 정보 및 성적 데이터 관리 (PostgreSQL)
- **ProblemModel**: 문제 데이터 관리 (FAISS 벡터 DB)

### View
- **APIView**: FastAPI 기반 REST API 인터페이스

### Controller
- **StudentController**: 학생 관련 비즈니스 로직
- **ProblemController**: 문제 관련 비즈니스 로직
- **TutorController**: AI 튜터 핵심 로직 (진단, 문제 생성, 피드백 등)

---

## 🔑 주요 기능

- **학생 관리**: 학생 등록 및 조회
- **학생 진단**: 문제 풀이 이력 기반 학생 수준 진단
- **맞춤형 문제 제공**: 학생 수준과 약점에 맞는 문제 선택
- **AI 문제 생성**: 기존 문제가 없을 때 LLM으로 새 문제 생성
- **개인화된 피드백**: 학생 답변에 대한 맞춤형 피드백 제공

---

## ⚙️ 설치 및 실행

### 환경 요구사항
- Python 3.9 이상
- PostgreSQL 데이터베이스
- OpenAI API 키

### 설치 방법

#### 저장소 복제
```bash
git clone <repository-url>
cd ai-tutor-mvc
