# Text-summarization

## 🔎 Danh Mục

1. [Giới thiệu](#Giới-thiệu)
2. [Chức năng](#chức-năng-chính)
3. [Tổng quan hệ thống](#tổng-quan-hệ-thống)
4. [Cấu trúc thư mục](#cấu-trúc-thư-mục)
5. [Hướng dẫn cài đặt](#hướng-dẫn-cài-đặt)
    - [📋 Yêu cầu](#📋-yêu-cầu)
    - [🔨 Cài đặt](#🔨-cài-đặt)



## Giới thiệu
**Text summarization** là một ứng dụng cho phép người dùng có thể tóm tắt các văn bản ngắn.

## Chức năng chính
Project tập trung vào chức năng chính là cho phép người dùng gửi văn bản và trả về tóm tắt của văn bản đó

## Tổng quan hệ thống
Backend của hệ thống được sử dụng với những công nghệ sau:
-   [Fastapi](https://fastapi.tiangolo.com/): Xây dựng API cho summary
-   [Docker](https://www.docker.com/): Containerize các service.
-   [Docker Compose](https://docs.docker.com/compose/): Quản lý các container.

Frontend của hệ thống sử dụng:
-   [Streamlit](https://streamlit.io/): Framework giúp dựng một giao diện nhanh chóng bằng python

## Cấu trúc thư mục
```
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── models
│   │   ├── routers
│   │   └── utils
│   ├── config
│   │   ├── configs.py
│   │   ├── __init__.py
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── shared
│   │   ├── base
│   │   ├── __init__.py
│   │   └── vncorenlp
│   └── test
│       ├── __init__.py
│       └── test.py
├── docker-compose.yml
├── frontend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── README.md
```

## Hướng dẫn cài đặt

### 📋 Yêu cầu
Để cài đặt và chạy được dự án, trước tiên bạn cần phải cài đặt các công cụ bên dưới. Hãy thực hiện theo các hướng dẫn cài đặt sau, lưu ý chọn hệ điều hành phù hợp với máy tính của bạn:

-   [Docker]()
-   [Docker compose]()

### 🔨 Cài đặt

-   Đầu tiên clone dự án về máy:
```
git clone https://github.com/0152neich/Text-summarization
```

-   Sau đó cd vào thư mục dự án và chạy lệnh
```
docker compose up --build
```

-   Truy cập địa chỉ sau để sử dụng
```
127.0.0.1:8501
```