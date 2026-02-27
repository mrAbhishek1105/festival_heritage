import React, { useState } from "react";
import "../App.css";

function SuggestFestival() {
  const [formData, setFormData] = useState({
    festivalName: "",
    state: "Bihar",
    month: "January",
    why: "",
    how: "",
    submitterName: "",
    submitterEmail: ""
  });

  const [status, setStatus] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("Submitting...");

    try {
      // Send data to the Express backend
      const response = await fetch("http://localhost:5000/api/suggest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const result = await response.json();

      if (response.ok) {
        setStatus("Success! Your suggestion has been recorded securely.");
        setFormData({
          festivalName: "", state: "Bihar", month: "January",
          why: "", how: "", submitterName: "", submitterEmail: ""
        });
      } else {
        setStatus(`Error: ${result.error}`);
      }
    } catch (error) {
      console.error("Submission error:", error);
      setStatus("Error: Could not connect to the server. Is it running?");
    }
  };

  const states = ["Bihar", "Jammu & Kashmir", "Rajasthan"];
  const months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];

  return (
    <div className="container" style={{ maxWidth: "700px" }}>
      <div className="glass-container">
        <h2 style={{ fontSize: "2.5rem", color: "var(--accent)", marginBottom: "1rem" }}>Suggest a Festival</h2>
        <p style={{ color: "var(--text-muted)", marginBottom: "2rem" }}>
          Help us document the rich cultural heritage of India. Submitted festivals will be reviewed and
          automatically saved to our offline Excel database for future inclusion.
        </p>

        {status && (
          <div style={{ padding: "12px", borderRadius: "8px", marginBottom: "1.5rem", backgroundColor: status.includes("Error") ? "rgba(244, 63, 94, 0.2)" : "rgba(34, 197, 94, 0.2)", border: status.includes("Error") ? "1px solid var(--primary)" : "1px solid #22c55e", color: "white" }}>
            {status}
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "1.5rem" }}>

          <div style={{ display: "flex", gap: "1rem" }}>
            <div className="form-group" style={{ flex: 1, marginBottom: 0 }}>
              <label>Your Name</label>
              <input type="text" name="submitterName" value={formData.submitterName} onChange={handleChange} className="form-input" required placeholder="John Doe" />
            </div>
            <div className="form-group" style={{ flex: 1, marginBottom: 0 }}>
              <label>Your Email</label>
              <input type="email" name="submitterEmail" value={formData.submitterEmail} onChange={handleChange} className="form-input" required placeholder="john@example.com" />
            </div>
          </div>

          <div className="form-group">
            <label>Festival Name</label>
            <input type="text" name="festivalName" value={formData.festivalName} onChange={handleChange} className="form-input" required placeholder="e.g. Navratri" />
          </div>

          <div style={{ display: "flex", gap: "1rem" }}>
            <div className="form-group" style={{ flex: 1, marginBottom: 0 }}>
              <label>State</label>
              <select name="state" value={formData.state} onChange={handleChange} className="filter-select" style={{ width: "100%" }}>
                {states.map(s => <option key={s} value={s}>{s}</option>)}
              </select>
            </div>
            <div className="form-group" style={{ flex: 1, marginBottom: 0 }}>
              <label>Month</label>
              <select name="month" value={formData.month} onChange={handleChange} className="filter-select" style={{ width: "100%" }}>
                {months.map(m => <option key={m} value={m}>{m}</option>)}
              </select>
            </div>
          </div>

          <div className="form-group">
            <label>Why is it celebrated?</label>
            <textarea name="why" value={formData.why} onChange={handleChange} className="form-input" required rows="3" placeholder="Historical or religious significance..."></textarea>
          </div>

          <div className="form-group">
            <label>How is it celebrated?</label>
            <textarea name="how" value={formData.how} onChange={handleChange} className="form-input" required rows="3" placeholder="Key rituals, foods, and practices..."></textarea>
          </div>

          <button type="submit" className="primary-btn" style={{ marginTop: "1rem", width: "100%" }}>
            Submit Suggestion Offline
          </button>
        </form>
      </div>
    </div>
  );
}

export default SuggestFestival;
