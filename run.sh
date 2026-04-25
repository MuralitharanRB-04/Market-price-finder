# 1. Create virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup environment
cp .env.example .env
# Edit .env and put your SERPER_API_KEY and OPENAI_API_KEY

# 4. Run the backend
uvicorn main:app --reload --port 8000

# 5. Open frontend
# Just open frontend/index.html in browser or serve it