import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, BrowserRouter } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import MapView from "./pages/MapView";

function App() {
  const [threats, setThreats] = useState([]);

  useEffect(() => {
    const mockThreats = [
      {
        id: 1,
        type: "Social Unrest",
        location: "Downtown Plaza",
        distance: "0.3 km",
        severity: "high",
        confidence: 92,
        description:
          "Large crowd gathering reported with potential for escalation",
        time: "2 mins ago",
        source: "Twitter Analysis",
      },
      {
        id: 2,
        type: "Weather Alert",
        location: "City Center",
        distance: "1.2 km",
        severity: "medium",
        confidence: 88,
        description: "Severe thunderstorm warning issued",
        time: "15 mins ago",
        source: "Weather Service",
      },
      {
        id: 3,
        type: "Traffic Incident",
        location: "Main Street",
        distance: "2.1 km",
        severity: "low",
        confidence: 76,
        description: "Multi-vehicle accident causing delays",
        time: "32 mins ago",
        source: "Traffic Reports",
      },
    ];
    setThreats(mockThreats);
  }, []);

  return (
    
    <Router >
      <Navbar />
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 min-h-screen bg-black text-white">
        <Routes>
          <Route path="/" element={<Dashboard threats={threats} />} />
          <Route path="/map" element={<MapView />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
