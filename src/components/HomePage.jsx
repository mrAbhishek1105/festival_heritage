import React from "react";

function HomePage({ setPage }) {
  return (
    <div className="hero-section">
      <h1 className="hero-title">
        Discover the Soul of <span style={{ color: "var(--primary)" }}>India</span>
      </h1>

      <p className="hero-subtitle">
        Immerse yourself in a curated collection of authentic cultural, religious, and seasonal festivals across the diverse landscapes of Jammu & Kashmir, Rajasthan, and Bihar.
      </p>

      <div style={{ display: 'flex', gap: '16px', marginTop: '20px' }}>
        <button className="primary-btn" onClick={() => setPage("festivals")}>
          Explore Festivals
        </button>
        <button className="secondary-btn" onClick={() => setPage("map")}>
          View Interactive Map
        </button>
      </div>

      <div className="hero-stats">
        <div className="stat-item">
          <span className="stat-number">3</span>
          <span className="stat-label">Focus States</span>
        </div>
        <div className="stat-item">
          <span className="stat-number">20+</span>
          <span className="stat-label">Authentic Festivals</span>
        </div>
        <div className="stat-item">
          <span className="stat-number">100%</span>
          <span className="stat-label">Cultural Heritage</span>
        </div>
      </div>
    </div>
  );
}

export default HomePage;
