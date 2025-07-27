# Transforming Business Workflows with GPT-Powered Multi-Agent Systems

## Introduction  
This project showcases how GPT-powered multi-agent systems can automate and optimize business workflows, focusing on HR processes. By leveraging AI, it enhances the efficiency and accuracy of resume evaluation, candidate communication, and interview scheduling, reducing manual effort and improving candidate experience.

## Objectives  
- Automate the evaluation of resumes to identify relevant experience, skills, and education  
- Generate dynamic, personalized responses to candidates based on evaluation outcomes  
- Schedule interviews and recommend suitable vacancies intelligently  
- Demonstrate a modular, scalable approach to integrating multiple AI agents in business workflows  

## Features  
- Resume evaluation based on key criteria using an AI agent  
- Automated candidate communication tailored to evaluation results  
- Intelligent interview scheduling and vacancy matching  

## Process & Methods  
- Developed modular agents each responsible for a distinct HR task: evaluation, candidate response, and scheduling  
- Used an OpenAI-compatible GPT model for natural language understanding and generation  
- Created a workflow orchestrator (`main.py`) that integrates agent outputs and controls the decision logic  
- Implemented sample data for testing and demonstration  
- Managed configuration and sensitive data securely through environment variables  

## Structure  
- `agents/`: Contains modular agent scripts for each workflow step  
- `main.py`: Coordinates the multi-agent workflow and runs the demo  
- `examples/`: Holds sample resumes for demonstration purposes  
- `config.py`: Stores project configuration, including API keys (loaded securely)  

## Results  
- Successfully automated the resume screening process with clear, criterion-based evaluations  
- Personalized communication improves candidate engagement and clarity  
- Efficient interview scheduling reduces administrative overhead and matches candidates to relevant job openings  

## Conclusion  
This project demonstrates the practical application of GPT-powered multi-agent systems to transform traditional HR workflows. By modularizing tasks and automating key processes, it offers a scalable and effective solution to improve business operations and candidate experience.

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
