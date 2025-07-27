# AI Recruitment Assistant Project

## Introduction  
This AI recruitment assistant project exemplifies how generative language models can be employed to automate and enhance key human resource functions. By leveraging multiple specialized AI agents, the system aims to streamline resume screening, candidate communication, and interview scheduling, contributing to improved efficiency and candidate experience within recruitment workflows.

## Objectives  
The core objectives are to automate the evaluation of candidate resumes against relevant hiring criteria, generate personalized responses to candidates based on evaluation outcomes, and suggest appropriate interview time slots and job vacancies matched to the candidate’s profile. Ultimately, this reduces manual workload for recruiters and accelerates the hiring process while maintaining professionalism and engagement with candidates.

## Features  
The system is composed of three sequential AI-powered agents:  
1. A resume evaluation agent that acts as a virtual HR analyst, assessing experience relevance, possession of key skills, and education level, producing a "satisfactory" or "unsatisfactory" rating for each criterion.  
2. A candidate response agent that, depending on the evaluation results, either crafts a welcoming message with tailored interview questions or politely informs candidates about disqualification.  
3. An interview scheduler and vacancy recommender agent that proposes multiple interview time slots and suggests relevant job openings aligned with the candidate’s qualifications and experience.

## Process & Methods  
The process begins by selecting candidate resumes from a predefined dataset to simulate incoming applications. The resume evaluator agent analyzes the resume text using guided system prompts and generates a criterion-wise assessment. This evaluation output is then passed to the recruiter agent, which applies conditional logic to decide on candidate messaging — offering interviews or rejection notices accordingly. For candidates meeting the acceptance threshold, the interview scheduling agent suggests interview times and compatible vacancies. All agents interact with a generative language model API via structured system and user prompts, allowing AI-guided natural language understanding and generation mapped to specific recruitment tasks.

## Structure  
Implemented in Python, the system interacts with the OpenAI API to query a generative language model, passing role-specific system messages and user content. The modular architecture features independent functions for each agent’s logic, facilitating easy maintenance and extension. Conditional checks are employed to control workflow progression, linking evaluation outcomes to subsequent candidate engagement and scheduling steps. This design maintains clarity and scalability while enabling focused tuning of each recruitment step.

## Setup  
1. **Clone the repository**  
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure your API key**  
   - Add your key to a `.env` file:  
     ```
     OPENAI_API_KEY=your-key
     ```
4. **Run the demonstration**  
   ```bash
   python main.py
   ```


## Results  
The outcome is an end-to-end automated recruitment pipeline that reads and evaluates free-text resumes, produces candidate-specific communications, and manages interview scheduling and vacancy matching. Demonstrations show a clear sequential output progression — from evaluation through candidate interaction to interview planning — validating the system’s capability to simulate real recruitment decision-making and coordination effectively.

## Conclusion  
This project demonstrates the power of generative AI in augmenting human resource procedures by automating resume screening, personalized candidate communication, and interview coordination. The modular, agent-driven approach provides a flexible, scalable framework that reduces recruiter burden, enhances candidate experience, and expedites hiring timelines. Future enhancements could include integration with applicant tracking systems, advanced resume parsing for deeper skill extraction, and syncing with real-time calendars for dynamic interview scheduling — further advancing AI’s role in intelligent recruitment solutions.

