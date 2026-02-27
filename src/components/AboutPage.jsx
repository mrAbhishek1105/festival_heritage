import React, { useState } from "react";

function AboutPage() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: ""
  });
  const [status, setStatus] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("Sending feedback...");

    try {
      const response = await fetch("http://localhost:5000/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const result = await response.json();

      if (response.ok) {
        setStatus("Success! Feedback sent to Management.");
        setFormData({ name: "", email: "", message: "" });
      } else {
        setStatus(`Error: ${result.error}`);
      }
    } catch (error) {
      console.error("Feedback error:", error);
      setStatus("Error: Could not connect to mail server.");
    }
  };

  return (
    <div className="container" style={{ display: "flex", flexWrap: "wrap", gap: "2rem", alignItems: "flex-start" }}>

      {/* Mission Section */}
      <div className="glass-container" style={{ flex: "1 1 500px" }}>
        <h2 style={{ fontSize: "2.5rem", color: "var(--accent)", marginBottom: "1rem" }}>Our Mission</h2>
        <p className="subtitle" style={{ textAlign: "left", margin: "0 0 1.5rem 0", color: "var(--text-main)" }}>
          Preserving the soul of India through digital immersion.
        </p>
        <p style={{ color: "var(--text-muted)", marginBottom: "1rem" }}>
          The Festival Heritage Platform is dedicated to promoting the "Swadeshi for Atmanirbhar Bharat" initiative
          by documenting and showcasing the incredible diversity of India's cultural heritage.
        </p>
        <p style={{ color: "var(--text-muted)", marginBottom: "1rem" }}>
          Currently focusing on the vibrant states of <strong>Jammu & Kashmir</strong>, <strong>Rajasthan</strong>,
          and <strong>Bihar</strong>, we strive to provide authentic, highly-detailed information about
          traditional, local, and religious celebrations.
        </p>
        <p style={{ color: "var(--primary)", fontWeight: "600" }}>
          Explore. Learn. Suggest.
        </p>
      </div>

      {/* Feedback Form Section */}
      <div className="glass-container" style={{ flex: "1 1 400px", background: "rgba(15, 23, 42, 0.8)" }}>
        <h3 style={{ fontSize: "1.8rem", marginBottom: "1.5rem" }}>Send us Feedback</h3>

        {status && (
          <div style={{ padding: "10px", borderRadius: "8px", marginBottom: "1rem", backgroundColor: status.includes("Error") ? "rgba(244, 63, 94, 0.2)" : "rgba(34, 197, 94, 0.2)", border: status.includes("Error") ? "1px solid var(--primary)" : "1px solid #22c55e", color: "white", fontSize: "0.9rem" }}>
            {status}
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          <div className="form-group" style={{ marginBottom: "0" }}>
            <label>Name</label>
            <input type="text" name="name" value={formData.name} onChange={handleChange} className="form-input" required placeholder="Your Name" />
          </div>

          <div className="form-group" style={{ marginBottom: "0" }}>
            <label>Email</label>
            <input type="email" name="email" value={formData.email} onChange={handleChange} className="form-input" required placeholder="you@example.com" />
          </div>

          <div className="form-group" style={{ marginBottom: "0" }}>
            <label>Message</label>
            <textarea name="message" value={formData.message} onChange={handleChange} className="form-input" required rows="4" placeholder="How can we improve the platform?"></textarea>
          </div>

          <button type="submit" className="primary-btn" style={{ marginTop: "0.5rem" }}>
            Send Feedback securely
          </button>
        </form>
      </div>

    </div>
  );
}

export default AboutPage;
