import { useState } from "react";

function FestivalDetails({ festival, onBack }) {
  const [showHindi, setShowHindi] = useState(false);

  return (
    <div className="festival-details">

      {/* BACK BUTTON */}
      <button className="back-btn-modern" onClick={onBack}>
        ← Back to Festivals
      </button>

      {/* HEADER */}
      <div className="festival-header">
        <span className="folk-badge">Local / Folk Festival</span>

        <h1>{festival.festivalName}</h1>

        <p className="meta">
          <b>Religion:</b> {festival.religion} &nbsp; | &nbsp;
          <b>State:</b> {festival.state} &nbsp; | &nbsp;
          <b>Month:</b> {festival.month}
        </p>
      </div>

      {/* WHY */}
      <section className="section">
        <h2>Why this festival matters</h2>
        <p>{festival.shortInfo.why}</p>
      </section>

      {/* HISTORY */}
      {festival.shortInfo.history && (
        <section className="section card">
          <h2>History & Origin</h2>
          <p>{festival.shortInfo.history}</p>
        </section>
      )}

      {/* INFO GRID */}
      <div className="info-grid">

        {festival.shortInfo.do && (
          <div className="info-card">
            <h3>What to Do</h3>
            <p>{festival.shortInfo.do}</p>
          </div>
        )}

        {festival.shortInfo.avoid && (
          <div className="info-card">
            <h3>What to Avoid</h3>
            <p>{festival.shortInfo.avoid}</p>
          </div>
        )}

        {festival.shortInfo.dress && (
          <div className="info-card">
            <h3>Traditional Dress</h3>
            <p>{festival.shortInfo.dress}</p>
          </div>
        )}

        {festival.shortInfo.food && (
          <div className="info-card">
            <h3>Traditional Food</h3>
            <p>{festival.shortInfo.food}</p>
          </div>
        )}

      </div>

      {/* HINDI TOGGLE */}
      {festival.hindi && (
        <div className="hindi-toggle">
          <button
            className="secondary-btn"
            onClick={() => setShowHindi(!showHindi)}
          >
            {showHindi ? "Hide Hindi Information" : "View Hindi Information"}
          </button>

          {showHindi && (
            <div className="language-box hindi">
              <h3>हिंदी में जानकारी</h3>
              <p>{festival.hindi}</p>
            </div>
          )}
        </div>
      )}

    </div>
  );
}

export default FestivalDetails;
