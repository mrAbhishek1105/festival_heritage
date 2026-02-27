require("dotenv").config();
const express = require("express");
const cors = require("cors");
const nodemailer = require("nodemailer");
const xlsx = require("xlsx");
const fs = require("fs");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

const PORT = 5000;

// ==========================================
// 1. Email Feedback Route
// ==========================================
app.post("/api/feedback", async (req, res) => {
    const { name, email, message } = req.body;

    if (!name || !email || !message) {
        return res.status(400).json({ error: "All fields are required." });
    }

    // Configure Nodemailer transporter
    const transporter = nodemailer.createTransport({
        service: "gmail",
        auth: {
            user: process.env.EMAIL_USER, // e.g., rexocreation@gmail.com
            pass: process.env.EMAIL_APP_PASSWORD, // 16-digit Google App Password
        },
    });

    const mailOptions = {
        from: process.env.EMAIL_USER,
        to: "rexocreation@gmail.com",
        subject: `New Feedback from Festival Heritage: ${name}`,
        text: `You have received new feedback from the Festival Heritage Platform.\n\nName: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
    };

    try {
        await transporter.sendMail(mailOptions);
        res.status(200).json({ success: "Feedback sent successfully!" });
    } catch (error) {
        console.error("Error sending email:", error);
        res.status(500).json({ error: "Failed to send feedback email. Check server configuration." });
    }
});

// ==========================================
// 2. Excel Suggestion Route
// ==========================================
app.post("/api/suggest", (req, res) => {
    const suggestionData = req.body;

    // Ensure the body has data
    if (!suggestionData || Object.keys(suggestionData).length === 0) {
        return res.status(400).json({ error: "Suggestion data is empty." });
    }

    // Define the path to the Excel file in the main project directory (one level up from /server)
    const excelFilePath = path.join(__dirname, "..", "festival_suggestions.xlsx");

    try {
        let workbook;
        let worksheet;
        const sheetName = "Suggestions";

        // Format new row data with timestamp
        const newRow = {
            Timestamp: new Date().toISOString(),
            ...suggestionData
        };

        // Check if the file already exists
        if (fs.existsSync(excelFilePath)) {
            // 1. Read existing file
            workbook = xlsx.readFile(excelFilePath);
            worksheet = workbook.Sheets[sheetName];

            // If the sheet somehow doesn't exist, create it. Otherwise, append to it.
            if (!worksheet) {
                worksheet = xlsx.utils.json_to_sheet([newRow]);
                xlsx.utils.book_append_sheet(workbook, worksheet, sheetName);
            } else {
                // Convert existing sheet to JSON, push new data, convert back
                const existingData = xlsx.utils.sheet_to_json(worksheet);
                existingData.push(newRow);

                // Create a new worksheet reflecting the updated data
                const newWorksheet = xlsx.utils.json_to_sheet(existingData);
                workbook.Sheets[sheetName] = newWorksheet;
            }
        } else {
            // 2. File doesn't exist, create it fresh
            workbook = xlsx.utils.book_new();
            worksheet = xlsx.utils.json_to_sheet([newRow]);
            xlsx.utils.book_append_sheet(workbook, worksheet, sheetName);
        }

        // 3. Write back to file
        xlsx.writeFile(workbook, excelFilePath);

        res.status(200).json({ success: "Suggestion successfully saved to Excel sheet!" });
    } catch (error) {
        console.error("Error writing to Excel:", error);
        res.status(500).json({ error: "Failed to save suggestion to Excel file." });
    }
});

app.listen(PORT, () => {
    console.log(`Festival Heritage Backend Server running on http://localhost:${PORT}`);
});
