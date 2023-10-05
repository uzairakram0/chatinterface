# Chat Agent with OpenAI GPT-4 Integration

Chat Agent is a simple, yet powerful, chat application that leverages the power of OpenAI's GPT-4 to provide real-time chat responses. Whether you're looking to simulate an AI-based chatbot or want a ready-to-use Django project that integrates with OpenAI, this project is for you.

## Features

- **Dynamic Responses**: With GPT-4 integration, the chat agent provides smart, contextually relevant answers to users' queries.
- **Django Backend**: Built on the Django framework, this chat agent is scalable and easy to integrate with other systems.
- **Database-backed Messages**: Leveraging Django's ORM, all chat messages are stored in the database, allowing for easy retrieval and analysis.
- **API Key Storage**: Store your OpenAI API key securely using the `ApiKey` model.
- **Session-Based Chat Flow**: This ensures that every user sees only their own chat history, preserving privacy and individuality.
- **UI Enhancements**: Built with Bootstrap 4, the interface is responsive and user-friendly.

## Prerequisites

- **Django**: This project is built on the Django framework.
- **OpenAI API Key**: An API key from OpenAI is required for the GPT-4 integration.

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory and install the required dependencies.
3. Set up the database using Django's migrations.
4. Start the development server using Django's `runserver` command.

## Usage

### User Interaction

Users can interact with the chat agent directly from the interface. They simply need to type their query and hit enter. The agent responds in real-time, simulating a conversational experience.

### Managing API Key

To integrate the OpenAI GPT-4 model, you need to set your OpenAI API key. There's a provision in the UI to input the key. This key is securely stored in the database and is used for all subsequent API calls.

### Clearing the Chat

For instances when you want to clear the entire chat history, a 'Clear Chat' button is provided. Clicking this will purge the chat history from the screen and the database.

## Architecture

### Models

- **ChatMessage**: Represents individual chat messages. It keeps track of the sender (User or Agent) and the content of the message.
- **ApiKey**: Used to store the OpenAI API key securely in the database.

### Views

- **index**: This view handles the main chat interaction. It manages the session-based chat flow and integrates with the GPT-4 model to fetch real-time responses.
- **key**: A separate view to manage the input and storage of the OpenAI API key.
- **clear**: A utility view that clears all chat messages from the database, providing a clean slate for users.

### Templates

The `index.html` template provides the user interface for the chat. It's designed with Bootstrap 4 and offers a clean, intuitive chatting experience.

## Customization

The project is structured to allow for easy customization and extension. Whether you want to integrate other AI models, extend the UI, or add additional features, the clean codebase supports it.

## Conclusion

Chat Agent is a versatile project that showcases the potential of combining the Django framework with powerful AI models like GPT-4. It's an excellent starting point for anyone looking to dive into AI-powered chat systems.

