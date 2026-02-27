import { useState } from "react";


import Navbar from "./components/Navbar";
import HomePage from "./components/HomePage";
import FestivalList from "./components/FestivalList";
import FestivalDetails from "./components/FestivalDetails";
import AboutPage from "./components/AboutPage";
import SuggestFestival from "./components/SuggestFestival";
import TripPlanner from "./components/TripPlanner";
import MapFeature from "./components/MapFeature";
import Footer from "./components/Footer";

import "./App.css";

function App() {
  // Page navigation state
  const [page, setPage] = useState("home");

  // Festival details state
  const [selectedFestival, setSelectedFestival] = useState(null);

  // Change page and reset selected festival
  const changePage = (newPage) => {
    setSelectedFestival(null);
    setPage(newPage);
  };

  return (
    <div className="app">
      {/* NAVBAR */}
      <Navbar setPage={changePage} />

      {/* MAIN CONTENT */}
      <div className="container">
        {page === "home" && <HomePage setPage={changePage} />}
        {page === "about" && <AboutPage />}

        {/* 🔹 STEP B: Suggest Festival Page (Protected) */}
        {page === "suggest" && <SuggestFestival />}

        {page === "festivals" && (
          <>
            <h1 className="main-title">Festival Heritage Project</h1>

            {selectedFestival === null ? (
              <FestivalList setSelectedFestival={setSelectedFestival} />
            ) : (
              <FestivalDetails
                festival={selectedFestival}
                onBack={() => setSelectedFestival(null)}
              />
            )}
          </>
        )}

        {page === "trip-planner" && <TripPlanner />}
        {page === "map" && <MapFeature />}
      </div>

      {/* FOOTER */}
      <Footer />
    </div>
  );
}

export default App;
