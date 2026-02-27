import { useState } from "react";
import festivals from "../data/festivals.json";
import FestivalDetails from "./FestivalDetails";

function TripPlanner() {
    const [state, setState] = useState("All");
    const [startDate, setStartDate] = useState("");
    const [endDate, setEndDate] = useState("");
    const [selectedFestival, setSelectedFestival] = useState(null);

    const states = ["All", ...new Set(festivals.map((fest) => fest.state))];

    const filteredFestivals = festivals.filter((fest) => {
        // State Filter
        const matchState =
            state === "All" || fest.state.toLowerCase() === state.toLowerCase();

        // Date Filter
        let matchDate = true;
        if (startDate && endDate) {
            const start = new Date(startDate);
            const end = new Date(endDate);
            const festStart = new Date(fest.startDate);
            const festEnd = new Date(fest.endDate);

            // Check if festival dates overlap with travel dates
            matchDate = festStart <= end && festEnd >= start;
        }

        return matchState && matchDate;
    });

    if (selectedFestival) {
        return (
            <FestivalDetails
                festival={selectedFestival}
                onBack={() => setSelectedFestival(null)}
            />
        );
    }

    return (
        <div className="trip-planner">
            <h1 className="main-title">Festival Trip Planner</h1>
            <p style={{ textAlign: "center", marginBottom: "30px", fontSize: "1.1rem" }}>
                Enter your travel dates and location to find festivals you can experience!
            </p>

            <div className="filters trip-filters" style={{ display: "flex", gap: "15px", flexWrap: "wrap", justifyContent: "center", marginBottom: "30px" }}>
                <select
                    className="filter-select"
                    value={state}
                    onChange={(e) => setState(e.target.value)}
                >
                    {states.map((s) => (
                        <option key={s} value={s}>
                            {s === "All" ? "All States" : s}
                        </option>
                    ))}
                </select>

                <div style={{ display: "flex", flexDirection: "column" }}>
                    <label style={{ fontSize: "0.8rem", color: "#666" }}>Travel Start Date</label>
                    <input
                        className="filter-select"
                        type="date"
                        value={startDate}
                        onChange={(e) => setStartDate(e.target.value)}
                    />
                </div>

                <div style={{ display: "flex", flexDirection: "column" }}>
                    <label style={{ fontSize: "0.8rem", color: "#666" }}>Travel End Date</label>
                    <input
                        className="filter-select"
                        type="date"
                        value={endDate}
                        onChange={(e) => setEndDate(e.target.value)}
                    />
                </div>
            </div>

            <div className="festival-grid">
                {!startDate || !endDate ? (
                    <p className="empty-message">Please enter your travel dates to see suggestions.</p>
                ) : filteredFestivals.length === 0 ? (
                    <p className="empty-message">No festivals found during your trip dates in this state.</p>
                ) : (
                    filteredFestivals.map((fest) => (
                        <div key={fest.id} className="festival-card">
                            <h3>{fest.festivalName}</h3>
                            <p>
                                <b>State:</b> {fest.state}
                            </p>
                            <p>
                                <b>Dates:</b> {fest.startDate} to {fest.endDate}
                            </p>
                            <p>
                                <b>Why:</b> {fest.shortInfo.why}
                            </p>
                            <button onClick={() => {
                                if (fest.externalLink) {
                                    window.open(fest.externalLink, "_blank");
                                } else {
                                    setSelectedFestival(fest);
                                }
                            }}>
                                Read More {fest.externalLink && "↗"}
                            </button>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
}

export default TripPlanner;
