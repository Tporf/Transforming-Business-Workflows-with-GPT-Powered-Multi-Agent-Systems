```markdown
# Transforming Business Workflows with GPT-Powered Multi-Agent Systems

This project demonstrates how to automate HR workflows using multiple GPT-powered chat agents (Google Gemini API). The system includes:

- **Resume Evaluator Agent:** Analyzes candidate resumes against key criteria.
- **Candidate Response Agent:** Generates personalized messages based on evaluation results.
- **Interview Scheduler Agent:** Suggests interview time slots and suitable job vacancies.

---

## Getting Started

### Prerequisites

- Python 3.7+
- An API key for Google Gemini / OpenAI API with access to `gemini-2.5-flash` or similar models.

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Create and activate a virtual environment:

```
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API key:

```
API_KEY=your_gemini_api_key_here
```

> **Important:** Do not share or commit your `.env` file to public repositories.

---

### Usage

Run the main script to see the multi-agent system in action:

```
python main.py
```

This will:

- Randomly select a sample resume.
- Evaluate the resume with the Resume Evaluator Agent.
- Generate a response to the candidate.
- If evaluation is positive, schedule an interview and suggest suitable vacancies.

---

## Project Structure

```
project-root/
│
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables (API key, excluded from git)
│
├── main.py                     # Entry point script
├── agents/                     # Agents implementations
│   ├── __init__.py
│   ├── agent_utils.py          # API helper functions
│   ├── resume_evaluator.py     # Resume evaluation agent
│   ├── candidate_response.py   # Candidate response agent
│   └── interview_scheduler.py # Interview scheduling agent
│
├── data/                       # Sample data files
│   └── sample_resumes.txt
│
└── tests/                      # Unit tests for agents
    ├── test_resume_evaluator.py
    ├── test_candidate_response.py
    └── test_interview_scheduler.py
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

Your Name - your.email@example.com

---

## Acknowledgments

- [Google Gemini API](https://developers.generativeai.google/)
- OpenAI Python SDK  
- Inspiration from multi-agent systems research and GPT-powered automation

```

If you want, I can help customize or expand this README with examples or additional usage instructions.
