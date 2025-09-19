# 💬 AI Chatbot with Persistent Chat History

A modern AI chatbot application built with Gradio that features persistent chat history using Google Firestore and OpenAI's GPT models. Create multiple chat sessions, switch between conversations, and never lose your chat history!

## ✨ Features

- **Persistent Chat History**: All conversations are stored in Google Firestore
- **Multiple Chat Sessions**: Create and manage multiple chat sessions
- **Session Management**: Easy switching between different chat conversations
- **Modern UI**: Clean and responsive Gradio interface
- **OpenAI Integration**: Powered by OpenAI's GPT-4o-mini model
- **Real-time Updates**: Chat history updates in real-time across sessions

## 🛠️ Technologies Used

- **Frontend**: Gradio
- **AI Model**: OpenAI GPT-4o-mini
- **Database**: Google Firestore
- **Backend**: Python with LangChain
- **Authentication**: Google Cloud SDK

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- Google Cloud Project with Firestore enabled
- OpenAI API account and API key
- Google Cloud Service Account with Firestore permissions

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd chatbot-firestore
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud Authentication**
   - Create a service account in your Google Cloud Console
   - Download the service account key JSON file
   - Set the environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
     ```

4. **Create a `.env` file in the root directory**
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json
   ```

## 📦 Dependencies

Create a `requirements.txt` file with the following dependencies:

```
gradio>=4.0.0
langchain-openai>=0.1.0
langchain-google-firestore>=0.1.0
google-cloud-firestore>=2.10.0
python-dotenv>=1.0.0
```

## ⚙️ Configuration

The application uses the following configuration:

- **Project ID**: `langchain-chatbot-aad4e` (update this in the code to match your project)
- **Collection Name**: `chat_history`
- **Model**: `gpt-4o-mini`
- **Server**: Runs on `0.0.0.0:8080`

To customize these settings, modify the following variables in the main script:

```python
PROJECT_ID = "your-google-cloud-project-id"
COLLECTION_NAME = "your_collection_name"
model = ChatOpenAI(model="gpt-4o-mini")  # or any other OpenAI model
```

## 🏃‍♂️ Running the Application

1. **Ensure your `.env` file is properly configured**

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Access the application**
   Open your browser and navigate to `http://localhost:8080`

## 🎯 How to Use

1. **Starting a New Chat**
   - Enter a unique session ID in the "New Session ID" field
   - Click "➕ Start New Chat" to create a new conversation

2. **Loading Previous Chats**
   - Select from the "Previous Chats" dropdown to load an existing conversation
   - All your chat history will be restored automatically

3. **Chatting**
   - Type your message in the text box at the bottom
   - Press Enter or click send to get AI responses
   - All messages are automatically saved to Firestore

## 🔧 Environment Variables

Your `.env` file should contain:

```env
# Required: OpenAI API Key
OPENAI_API_KEY=sk-your-openai-api-key-here

# Optional: If not using GOOGLE_APPLICATION_CREDENTIALS environment variable
# GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account-key.json
```

## 🗃️ Database Structure

The application creates documents in Firestore with the following structure:

```
Collection: chat_history
Document ID: {session_id}
Fields:
  - created: timestamp
  - messages: array of message objects
```

## 🚨 Troubleshooting

### Common Issues:

1. **Authentication Error**
   - Ensure your Google Cloud credentials are properly set
   - Check that your service account has Firestore permissions

2. **OpenAI API Error**
   - Verify your OpenAI API key is correct and has sufficient credits
   - Check your API usage limits

3. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`

4. **Connection Issues**
   - Ensure your Firestore database is properly configured
   - Check your internet connection

### Debug Mode:

To run with debug information, you can modify the launch command:

```python
demo.launch(server_name="0.0.0.0", server_port=8080, debug=True)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Gradio](https://gradio.app/) for the amazing UI framework
- [LangChain](https://langchain.com/) for the AI integration tools
- [OpenAI](https://openai.com/) for the powerful language models
- [Google Cloud Firestore](https://firebase.google.com/products/firestore) for reliable data storage

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about the problem

---

**⭐ If you find this project helpful, please consider giving it a star!**
