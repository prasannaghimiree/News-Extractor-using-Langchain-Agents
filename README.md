# News Query Retrieval System with Langchain Agents

This project provides a sophisticated retrieval-based system for querying news data. It uses Langchain agents to process and format data from a Google search engine, fetched via a custom SearxNG instance, and returns structured responses. The backend is built using FastAPI, and the system leverages various Large Language Models (LLMs) like Ollama Mistral, Groq Mixtral, and Anthropic ChatBedrock for query processing.

## Features

- **Search Tool**: Fetches raw data from a custom search engine using SearxNG.
- **Formatter Tool**: Converts raw search results into structured JSON, extracting key details such as headlines, authors, publication date, and content.
- **Langchain Agent**: Automates the process of querying, analyzing, filtering, summarizing, and formatting the search results.
- **Frontend**: A simple web frontend built using HTML and CSS for user interaction.
- **FastAPI Backend**: Serves as the intermediary for the Langchain agent and the frontend, allowing users to query news and receive succinct, structured answers.

## Technologies

- **Langchain**: For creating agents and integrating tools.
- **SearxNG**: Custom search engine to retrieve data from the web.
- **FastAPI**: Backend API framework.
- **Ollama Mistral**: Large language model for query handling.
- **Groq Mixtral-8x7b-32768**: Another LLM for query processing.
- **Anthropic ChatBedrock**: Optional LLM for handling complex queries.
- **Docker**: For containerizing the application.
- **HTML/CSS**: Frontend for the user interface.

## Architecture

The system has the following components:

1. **Search Tool (SearxNG)**: Fetches results from Google using a custom instance of SearxNG.
2. **Formatter Tool**: Structures the raw data into a clean and readable JSON format.
3. **Agent Executor**: Combines both the search and formatter tools in sequence to produce relevant, structured answers to user queries.
4. **Backend (FastAPI)**: A FastAPI application handles the query flow and interfaces with Langchain and the tools.
5. **Frontend**: An HTML/CSS-based interface allows users to interact with the system.

## Setting up the Project

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>

## Docker run 
- docker compose up -d --build
- docker logs -t <container-id>