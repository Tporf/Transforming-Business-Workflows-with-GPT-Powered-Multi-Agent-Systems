\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{hyperref}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{listings}
\usepackage{xcolor}

\definecolor{codebg}{rgb}{0.95,0.95,0.95}

\lstset{
  backgroundcolor=\color{codebg},
  basicstyle=\ttfamily\small,
  breaklines=true,
  columns=fullflexible,
  frame=single,
  keepspaces=true,
  numbers=left,
  numberstyle=\tiny\color{gray},
  showstringspaces=false,
  keywordstyle=\color{blue}
}

\title{Transforming Business Workflows with GPT-Powered Multi-Agent Systems}
\author{Your Name \\ \texttt{your.email@example.com}}
\date{2025}

\begin{document}

\maketitle

\section*{Project Overview}
This project demonstrates how to automate HR workflows using multiple GPT-powered chat agents (Google Gemini API). The system includes:

\begin{itemize}
    \item \textbf{Resume Evaluator Agent:} Analyzes candidate resumes against key criteria.
    \item \textbf{Candidate Response Agent:} Generates personalized messages based on evaluation results.
    \item \textbf{Interview Scheduler Agent:} Suggests interview time slots and suitable job vacancies.
\end{itemize}

\section*{Getting Started}

\subsection*{Prerequisites}
\begin{itemize}
    \item Python 3.7+
    \item An API key for Google Gemini / OpenAI API with access to \texttt{gemini-2.5-flash} or similar models.
\end{itemize}

\subsection*{Installation}
\begin{enumerate}
    \item Clone the repository:
    \begin{lstlisting}
git clone https://github.com/yourusername/your-repo.git
cd your-repo
    \end{lstlisting}
    
    \item Create and activate a virtual environment:
    \begin{lstlisting}[language=bash]
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
    \end{lstlisting}
    
    \item Install dependencies:
    \begin{lstlisting}[language=bash]
pip install -r requirements.txt
    \end{lstlisting}
    
    \item Create a \texttt{.env} file in the project root and add your API key:
    \begin{lstlisting}
API_KEY=your_gemini_api_key_here
    \end{lstlisting}
    
    \textbf{Important:} Do not share or commit your \texttt{.env} file to public repositories.
\end{enumerate}

\section*{Usage}

Run the main script to see the multi-agent system in action:

\begin{lstlisting}[language=bash]
python main.py
\end{lstlisting}

This will:
\begin{itemize}
    \item Randomly select a sample resume.
    \item Evaluate the resume with the Resume Evaluator Agent.
    \item Generate a response to the candidate.
    \item If evaluation is positive, schedule an interview and suggest suitable vacancies.
\end{itemize}

\section*{Project Structure}

\begin{verbatim}
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
\end{verbatim}

\section*{License}

This project is licensed under the MIT License -- see the \href{LICENSE}{LICENSE} file for details.

\section*{Acknowledgments}

\begin{itemize}
    \item \href{https://developers.generativeai.google/}{Google Gemini API}
    \item OpenAI Python SDK
    \item Inspiration from multi-agent systems research and GPT-powered automation
\end{itemize}

\end{document}
