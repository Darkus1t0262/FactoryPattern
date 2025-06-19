# 🏭 Factory Pattern - Python Example

This is a simple Python implementation of the Factory Design Pattern using greetings (`hello` and `goodbye`). The project is containerized using Docker.

## 📁 Project Structure

FactoryPattern/
├── greetings/
│ ├── init.py
│ ├── hello.py
│ └── goodbye.py
├── factory.py
├── main.py
└── Dockerfile


---

## 🚀 How to Use

### 🛠️ Build the Docker Image

Run this in your terminal from the root of the project:

```bash
docker build -t factory-pattern .
docker run -it --rm darkjus/factory-pattern
echo "hello" | docker run -i --rm darkjus/factory-pattern
