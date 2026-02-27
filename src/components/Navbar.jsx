import { useState } from "react";

function Navbar({ setPage }) {
  const [open, setOpen] = useState(false);

  const goTo = (page) => {
    setPage(page);
    setOpen(false); // mobile menu close
  };

  return (
    <nav className="navbar">
      <div className="logo" onClick={() => goTo("home")}>
        Festival Heritage
      </div>

      {/* Hamburger (mobile only) */}
      <div className="menu-icon" onClick={() => setOpen(!open)}>
        ☰
      </div>

      <ul className={`nav-links ${open ? "show" : ""}`}>
        <li onClick={() => goTo("home")}>Home</li>
        <li onClick={() => goTo("festivals")}>Festivals</li>
        <li onClick={() => goTo("trip-planner")}>Trip Planner</li>
        <li onClick={() => goTo("map")}>Map</li>
        <li onClick={() => goTo("about")}>About</li>
        <li onClick={() => goTo("suggest")}>Suggest</li>
      </ul>
    </nav>
  );
}

export default Navbar;
