# Transforming Business Workflows with GPT-Powered Multi-Agent Systems

## Introduction
This project focuses on transforming business processes, specifically the employee recruitment process, using modern GPT models and the concept of multi-agent systems. The use of artificial intelligence (AI) enables the automation of routine yet complex stages of talent acquisition — from initial resume evaluation to interview scheduling. By integrating with the OpenAI Gemini API, the system supports intelligent interaction among multiple agents, each solving specific tasks, which contributes to increased efficiency and reduced human bias in candidate selection.

## Objectives
The primary goal of the project is to automate and improve the candidate evaluation process in HR, minimizing subjectivity and accelerating the processing of a large number of applications. This is achieved by creating a set of specialized agents that:
- Analyze the relevance of a candidate’s work experience to the job opening;
- Check for the presence of key professional skills;
- Evaluate the level of education;
- Generate personalized responses for candidates;
- Suggest convenient time slots for interviews and recommend suitable vacancies based on the candidate’s profile.

This approach aims to enhance decision quality and reduce HR specialists’ workload related to routine operations.

## Features
The system consists of three main AI agents, each responsible for a separate task:
- **Resume Analyst (HR Analyst)** — performs semantic analysis of resumes, comparing data on experience, skills, and education against predefined criteria and outputs an evaluation of “satisfactory” or “unsatisfactory” for each parameter.
- **Recruiter (Communication Agent)** — based on the evaluation results, generates a response to the candidate: if the candidate meets most criteria, sends a welcoming message with interview questions; otherwise, politely informs of disqualification.
- **Interview Coordinator** — proposes several time slots for interviews and suggests several job vacancies likely to match the candidate’s experience and competencies.

This division facilitates scalability and modification of the system for different scenarios and business processes.

## Process & Methods
The process begins by submitting a candidate’s resume to the first agent, which uses GPT model calls to analyze the text, extracting relevant experience and skills and matching them with job requirements. The analysis output is sent to the second agent, which creates a communication message accordingly. If the candidate passes, the third agent receives the resume to propose interview times and appropriate vacancies.

Implementation uses Python with the OpenAI client library, where each function represents a separate agent interacting through structured messages. This simulated multi-agent architecture allows distributing logic among agents and provides flexible sequencing of evaluation and communication steps.

## Structure
Architecturally, the system is a set of agent functions, each playing its own role and calling the GPT API with predefined system and user messages. Authorization and model access are organized through an API client with key and base URL. Application logic controls the sequence of agent execution: after evaluating the candidate, it counts the number of “satisfactory” criteria and branches accordingly — either proceeding with interview scheduling or sending a rejection notice. This modular design ensures ease of maintenance, testing, and future expansion.


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
The implementation demonstrates a fully automated preliminary recruitment cycle where resumes are processed and evaluated without human involvement, shortening processing time and reducing bias. Personalized messages improve the quality of candidate engagement by making communication more human-like and informative. The ability to propose concrete interview slots and relevant vacancies optimizes organizational parts and accelerates decision-making. The system’s flexibility allows adjusting evaluation criteria and vacancy recommendations for different industries.

## Conclusion
This project serves as a compelling example of how GPT-based multi-agent systems can significantly transform business workflows. Automating and coordinating multiple specialized agents enables effective and scalable handling of complex tasks requiring multi-step analysis and decision-making. Such an approach saves resources, improves selection quality, enhances candidate satisfaction, and opens opportunities for implementing similar solutions in other business areas—from customer support to project management and beyond.

