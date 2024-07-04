# CODESTAGRAM

> 이 프로젝트는 Django와 Domain-Driven Design(DDD) 원칙을 사용하여 인스타그램과 유사한 서비스를 구현한 것입니다.

## 기능

- JWT 기반 사용자 인증 및 회원가입
- 사진 포스팅 기능
- 포스트에 댓글 달기 기능
- 팔로잉 및 팔로워 관리 기능
- 해시태그를 통한 포스트 분류
- 사용자 및 해시태그 검색 기능

## 아키텍처 개요

이 프로젝트는 DDD 원칙을 따르며, 도메인별로 비즈니스 로직을 명확히 분리하여 유지보수성과 확장성을 높였습니다. 주요 도메인으로는 `accounts`, `posts`, `relationships`, `hashtags`가 있으며, 각 도메인은 자체 모델, 리포지토리, 서비스, 스키마, 뷰를 가지고 있습니다.

### DDD의 핵심 요소

1. **모델(Model)**: 데이터베이스의 테이블과 매핑되는 객체로, 도메인의 핵심 데이터를 정의합니다.
2. **리포지토리(Repository)**: 데이터베이스와의 상호작용을 담당하며, 데이터 접근 로직을 캡슐화합니다.
3. **서비스(Service)**: 비즈니스 로직을 처리하며, 트랜잭션을 관리합니다.
4. **스키마(Schema)**: 데이터 전송 객체(DTO)로, API 요청 및 응답에 사용됩니다.
5. **뷰(View)**: API 엔드포인트를 정의하며, 클라이언트의 요청을 처리합니다.

## 도메인 설명

### 1. Accounts 도메인

**Accounts** 도메인은 사용자 인증 및 관리를 담당합니다.

- `models.py`: 사용자 모델 정의
- `repositories.py`: 사용자 데이터베이스 접근 로직
- `services.py`: 사용자 생성 및 인증 로직
- `schemas.py`: 사용자 데이터 전송 객체
- `views.py`: 사용자 관련 API 엔드포인트

### 2. Posts 도메인

**Posts** 도메인은 사진 포스팅과 관련된 기능을 담당합니다.

- `models.py`: 포스트 모델 정의
- `repositories.py`: 포스트 데이터베이스 접근 로직
- `services.py`: 포스트 생성 및 삭제 로직
- `schemas.py`: 포스트 데이터 전송 객체
- `views.py`: 포스트 관련 API 엔드포인트

### 3. Relationships 도메인

**Relationships** 도메인은 팔로잉 및 팔로워 관리 기능을 담당합니다.

- `models.py`: 팔로잉 관계 모델 정의
- `repositories.py`: 팔로잉 데이터베이스 접근 로직
- `services.py`: 팔로우 및 언팔로우 로직
- `schemas.py`: 팔로우 데이터 전송 객체
- `views.py`: 팔로우 관련 API 엔드포인트

### 4. Hashtags 도메인

**Hashtags** 도메인은 해시태그 관리 및 검색 기능을 담당합니다.

- `models.py`: 해시태그 모델 정의
- `repositories.py`: 해시태그 데이터베이스 접근 로직
- `services.py`: 해시태그 생성 및 검색 로직
- `schemas.py`: 해시태그 데이터 전송 객체
- `views.py`: 해시태그 관련 API 엔드포인트

***

## DRF vs Ninja
그동안 django 기반의 서버를 개발하면서 DRF가 조금 답답하게 느껴졌습니다. 물론 훌륭한 API 개발 라이브러리이지만, 
개인적으로 FastAPI와 같은 단순하면서도 빠른 `pydantic`한 느낌을 원했습니다. 
여러 프레임워크를 찾던 중 `Ninja` 를 통한 API를 구현해보도록 하겠습니다.


## License

[MIT LICENSE](LICENSE)