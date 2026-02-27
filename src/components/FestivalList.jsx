import { useState } from "react";
import festivals from "../data/festivals.json";


function FestivalList({ setSelectedFestival }) {
  const [search, setSearch] = useState("");
  const [month, setMonth] = useState("All");

  const [state, setState] = useState("All");

  // Get unique states from data
  const states = ["All", ...new Set(festivals.map(fest => fest.state))];

  // Month list (static – clean & SIH friendly)
  const months = [
    "All",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  // Filter festivals based on search, state & month
  const filteredFestivals = festivals.filter((fest) => {
    const matchName = fest.festivalName
      .toLowerCase()
      .includes(search.toLowerCase());

    const matchState =
      state === "All" ||
      fest.state.toLowerCase() === state.toLowerCase();

    const matchMonth =
      month === "All" ||
      fest.month.toLowerCase().includes(month.toLowerCase());

    return matchName && matchState && matchMonth;
  });

  return (
    <>
      {/* SEARCH + MONTH FILTER */}
      <div className="filters">
        <input
          className="search-input"
          type="text"
          placeholder="Search festival by name..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

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

        <select
          className="filter-select"
          value={month}
          onChange={(e) => setMonth(e.target.value)}
        >
          {months.map((m) => (
            <option key={m} value={m}>
              {m === "All" ? "All Months" : m}
            </option>
          ))}
        </select>
      </div>

      {/* FESTIVAL GRID */}
      <div className="festival-grid">
        {filteredFestivals.length === 0 ? (
          <p className="empty-message">
            No festivals found for the selected month.
          </p>
        ) : (
          filteredFestivals.map((fest) => (
            <div key={fest.id} className="festival-card">
              <h3>{fest.festivalName}</h3>

              <p>
                <b>Religion:</b> {fest.religion}
              </p>
              <p>
                <b>State:</b> {fest.state}
              </p>
              <p>
                <b>Month:</b> {fest.month}
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
    </>
  );
}

export default FestivalList;
