# Festival Heritage

A web application designed to explore cultural festival heritage, provide suggestions for new festivals, and submit feedback. Built with a React frontend and a Node.js/Express backend.

## Features

- **Explore Festivals**: View details and information about different cultural festivals.
- **Suggest Festivals**: Users can submit suggestions for new festivals, which are saved to an Excel file (`festival_suggestions.xlsx`) by the backend.
- **Feedback System**: Seamless integration for handling user feedback via email using the backend API.
- **Modern UI**: Clean and professional interface utilizing glassmorphism aesthetics.

## Project Structure

- `src/` & `public/` - React frontend source code and assets.
- `server/` - Node.js Express backend API, handling email feedback and Excel file generation.

## 🚀 Installation & Setup

### Prerequisites
- [Node.js](https://nodejs.org/) (installed)
- npm or yarn

### 1. Frontend Setup

1. Open your terminal and navigate to the root directory `festival-heritage`.
2. Install the necessary dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
4. The application should now be running at [http://localhost:3000](http://localhost:3000).

### 2. Backend Setup

1. Open a new terminal window and navigate to the backend directory:
   ```bash
   cd server
   ```
2. Install the backend dependencies:
   ```bash
   npm install
   ```
3. Create a `.env` file in the `server` directory (this is where you will add your email credentials or port number, e.g., `PORT=5000`, `EMAIL_USER=...`, `EMAIL_PASS=...`).
4. Start the Node.js backend server:
   ```bash
   npm start
   # or node server.js
   ```
5. The backend API is now ready and listening for requests.

## Notes
- Environment files (`.env`) and generated Excel files (`festival_suggestions.xlsx`) are ignored by Git to keep sensitive data and persistent local data out of version control.
- If you use the Python scripts provided in the directory, make sure you have Python installed and the generated cache files will similarly be ignored.
