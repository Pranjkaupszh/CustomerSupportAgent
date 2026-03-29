# A2A Multi-Agent Customer Support System 🤖

An intelligent, multi-agent customer support system powered by AI that automatically routes and handles customer inquiries through specialized agents. Built with Streamlit, Groq API, and a custom Agent-to-Agent (A2A) communication protocol.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)


## Overview

The A2A Multi-Agent Customer Support System is designed to handle customer inquiries efficiently by routing them to specialized AI agents. The system implements an intelligent triaging mechanism that directs queries to the most appropriate agent (FAQ, Billing, or Technical Support) based on query content.

This system demonstrates advanced concepts in:
- Multi-agent systems
- Intelligent query routing/triaging
- Custom inter-agent communication protocols
- Natural language processing
- Conversational AI

## Features

✨ **Multi-Agent Architecture**
- Dedicated FAQ Agent for common questions
- Billing Agent for payment and refund inquiries
- Technical Agent for troubleshooting and support
- Extensible framework for adding new agents

🎯 **Intelligent Query Routing**
- Automatic triaging of customer inquiries
- Context-aware agent selection
- Seamless agent-to-agent communication

🤖 **AI-Powered Responses**
- Leverages Groq's LLaMA 3.3 70B model for intelligent responses
- Technical support powered by advanced LLM capabilities
- Natural and conversational responses

💬 **User-Friendly Interface**
- Built with Streamlit for quick deployment
- Session-based chat history
- Real-time query processing

🔄 **Custom A2A Protocol**
- Structured message format with unique IDs
- Timestamp tracking and context preservation
- Supports inter-agent communication

## Architecture

```
┌─────────────────────────────────────────┐
│        Streamlit Web Interface          │
│      (app.py - User Chat Interface)     │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────▼──────────┐
        │   A2ASystem Core    │
        │   (system.py)       │
        │  - Query Triaging   │
        │  - Message Routing  │
        └──────────┬──────────┘
                   │
      ┌────────────┼────────────┐
      │            │            │
   ┌──▼──┐      ┌──▼──┐      ┌─▼───┐
   │ FAQ │      │Billi │      │Tech │
   │Agent│      │ng    │      │Agent│
   │     │      │Agent │      │     │
   └──┬──┘      └──┬───┘      └──┬──┘
      │            │            │
      └────────────┼────────────┘
                   │
        ┌──────────▼──────────┐
        │  A2A Protocol       │
        │  (a2a_protocol.py)  │
        │  - Message Format   │
        │  - UUID Tracking    │
        └─────────────────────┘
                   │
        ┌──────────▼──────────┐
        │   Groq API (LLaMA)  │
        │  (Advanced Responses)│
        └─────────────────────┘
```

## Prerequisites

- **Python 3.8+** - Core runtime environment
- **Groq API Key** - For accessing LLaMA models
- **pip** - Python package manager

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ai-customersupporta2a
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Groq Library (if not included)

```bash
pip install groq
```

## Configuration

### Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
GROQ_API_KEY=your_groq_api_key_here
```

**To obtain a Groq API Key:**

1. Visit [Groq Console](https://console.groq.com)
2. Sign up or log in to your account
3. Generate an API key from the dashboard
4. Add the key to your `.env` file

## Usage

### Running the Application

Start the Streamlit web interface:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Chat Interface

1. **Open the Web Interface** - Navigate to the Streamlit app URL
2. **Enter Your Query** - Type your customer support question in the chat input
3. **Get Instant Response** - The system automatically:
   - Triages your query
   - Routes it to the appropriate agent
   - Returns an intelligent response

### Example Queries

```
"I want to return my order"          → FAQ Agent
"How many days for refund?"          → Billing Agent
"My payment failed"                  → Billing Agent
"I'm getting an error message"       → Technical Agent
"How long does shipping take?"       → FAQ Agent
"Help me troubleshoot the app"       → Technical Agent
```

## Project Structure

```
ai-customersupporta2a/
├── app.py                  # Streamlit web interface
├── agents.py              # Agent implementations (FAQ, Billing, Technical)
├── system.py              # Core A2ASystem with triaging logic
├── a2a_protocol.py        # A2A message protocol and data structures
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Streamlit application entry point; handles user interface and session management |
| `agents.py` | Contains FAQAgent, BillingAgent, and TechnicalAgent implementations |
| `system.py` | Core system logic: query triaging and agent orchestration |
| `a2a_protocol.py` | Message protocol definitions and factory functions |
| `requirements.txt` | List of Python package dependencies |

## How It Works

### 1. **Query Reception**
The user submits a query through the Streamlit chat interface.

### 2. **Triaging**
The A2ASystem analyzes the query to determine the most appropriate agent:
- **Billing Agent**: Keywords like "payment", "refund"
- **Technical Agent**: Keywords like "error", "bug"
- **FAQ Agent**: Default for common inquiries

### 3. **Message Creation**
A structured A2AMessage is created containing:
- Unique message ID (UUID)
- Sender and receiver information
- Task/query content
- Timestamp
- Optional context

### 4. **Agent Processing**
The selected agent processes the message:
- **FAQ Agent** - Checks knowledge base for direct answers
- **Billing Agent** - Provides business logic responses
- **Technical Agent** - Uses Groq API for complex troubleshooting

### 5. **Response Handling**
If an agent cannot fully resolve the query, it routes the message to another agent. This continues until a customer-appropriate response is generated.

### 6. **Response Display**
The final response is returned to the user and displayed in the chat interface.

## Technologies Used

### Core Framework
- **Streamlit** - Web interface framework
- **Python 3.8+** - Programming language

### AI/ML
- **Groq API** - Access to LLaMA 3.3 70B model
- **Langchain** (via langchain_groq) - LLM integration

### Libraries
- **python-dotenv** - Environment variable management
- **requests** - HTTP library
- **pyngrok** - Ngrok integration for tunneling

## Agent Details

### FAQ Agent
- **Name**: faq
- **Purpose**: Handle frequently asked questions
- **Knowledge Base**:
  - Returns: "You can return items within 30 days."
  - Refunds: "Refund processed within 5 days."
  - Shipping: "Shipping takes 3-5 business days."
- **Fallback**: Routes unknown FAQ questions to Technical Agent

### Billing Agent
- **Name**: billing
- **Purpose**: Handle payment, refunds, and billing inquiries
- **Capabilities**:
  - Refund information and timelines
  - Payment method guidance
  - Billing question clarification

### Technical Agent
- **Name**: tech
- **Purpose**: Provide advanced troubleshooting and technical support
- **Capabilities**:
  - Uses Groq's LLaMA model for complex issues
  - Provides step-by-step troubleshooting
  - Handles custom technical scenarios

## Extending the System

### Adding a New Agent

1. **Create Agent Class** in `agents.py`:

```python
class NewAgent:
    name = "newagent"
    
    def handle(self, msg):
        # Process message
        answer = "Your response"
        return create_message(
            "newagent",
            "customer",
            answer
        )
```

2. **Register in A2ASystem** in `system.py`:

```python
self.agents = {
    "faq": FAQAgent(),
    "billing": BillingAgent(),
    "tech": TechnicalAgent(),
    "newagent": NewAgent()  # Add here
}
```

3. **Update Triaging Logic** to route to your agent based on keywords

## Best Practices

- ✅ Keep agent logic focused and single-purpose
- ✅ Use the A2A protocol for consistent messaging
- ✅ Add error handling in agent implementations
- ✅ Secure your Groq API key in `.env` file
- ✅ Test agents with various query types
- ✅ Monitor response quality and accuracy
- ✅ Update FAQ knowledge base regularly

## Troubleshooting

### Issue: "Groq API Key not found"
**Solution**: Ensure `.env` file exists in project root with valid `GROQ_API_KEY`

### Issue: Streamlit app not opening
**Solution**: Check that port 8501 is not in use, or specify a different port:
```bash
streamlit run app.py --server.port 8502
```

### Issue: Slow responses
**Solution**: This might indicate API latency. Check your internet connection and Groq service status.

### Issue: Agent routing incorrectly
**Solution**: Review the triaging logic in `system.py` and adjust keyword matching as needed.

## Performance Considerations

- **Query Processing**: Typically 2-5 seconds depending on Groq API latency
- **Concurrent Requests**: Streamlit handles single user sessions; consider deployment architecture for multi-user scenarios
- **API Rate Limits**: Monitor Groq API usage and plan accordingly

## Future Enhancements

- 🔄 Add conversation context memory across sessions
- 📊 Implement agent performance analytics
- 🔐 Add user authentication and authorization
- 📝 Create admin panel for FAQ management
- 🎓 Add machine learning-based routing optimization
- 🌐 Multi-language support
- 📞 Integration with ticketing systems
- 💾 Conversation logging and analytics
