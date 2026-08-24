import { useState } from "react";
import "./App.css";

function App() {
  const [showSchedule, setShowSchedule] = useState(false);
  const [simulationDone, setSimulationDone] = useState(false);
  const [approved, setApproved] = useState(false);
  const maintenanceRequests = [
    {
      track: "S01",
      priority: "Critical",
      duration: "3 hrs",
      status: "Pending",
    },
    {
      track: "S02",
      priority: "High",
      duration: "2 hrs",
      status: "Pending",
    },
    {
      track: "S03",
      priority: "Medium",
      duration: "1 hr",
      status: "Pending",
    },
  ];

  return (
    <div className="app">
      {/* Header */}
      <header className="header">
        <div>
          <h1>🚆 TrackSense</h1>
          <p>AI-Powered Railway Maintenance Planning</p>
        </div>

        <div className="planner">
          Planner Dashboard
        </div>
      </header>

      {/* Main content */}
      <main className="dashboard">

        <section className="welcome-section">
          <div className="welcome-content">
            <div>
              <h2>Railway Maintenance Dashboard</h2>
              <p>
                AI-assisted planning for safer and more efficient railway operations.
              </p>
            </div>

            <div className="system-status">
              <span className="status-dot"></span>
              System Operational
            </div>
          </div>

          <div className="summary-grid">

            <div className="summary-card critical-card">
              <div className="summary-icon">🔴</div>
              <div>
                <strong>1</strong>
                <span>Critical</span>
              </div>
            </div>

            <div className="summary-card high-card">
              <div className="summary-icon">🟠</div>
              <div>
                <strong>1</strong>
                <span>High Priority</span>
              </div>
            </div>

            <div className="summary-card medium-card">
              <div className="summary-icon">🟡</div>
              <div>
                <strong>1</strong>
                <span>Medium Priority</span>
              </div>
            </div>

            <div className="summary-card approved-card">
              <div className="summary-icon">🟢</div>
              <div>
                <strong>{approved ? "1" : "0"}</strong>
                <span>Approved</span>
              </div>
            </div>

          </div>
        </section>

        {/* Maintenance table */}
        <section className="card">
          <div className="card-header">
            <h2>Maintenance Requests</h2>
            <span>{maintenanceRequests.length} Requests</span>
          </div>

          <table>
            <thead>
              <tr>
                <th>Track</th>
                <th>Priority</th>
                <th>Duration</th>
                <th>Status</th>
              </tr>
            </thead>

            <tbody>
              {maintenanceRequests.map((request) => (
                <tr key={request.track}>
                  <td>{request.track}</td>

                  <td>
                    <span
                      className={`priority ${request.priority.toLowerCase()}`}
                    >
                      {request.priority}
                    </span>
                  </td>

                  <td>{request.duration}</td>

                  <td>
                    {request.track === "S01" && approved
                      ? "Approved"
                      : request.status}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        {/* Generate button */}
        <div className="generate-section">
          <button
            className="generate-button"
            onClick={() => setShowSchedule(true)}
          >
            Generate Schedule
          </button>
        </div>

        {/* Recommended schedule */}
        {showSchedule && (
          <section className="card recommendation">
            <div className="card-header">
              <h2>🤖 Recommended Maintenance Block</h2>
              <span className="ai-badge">AI Recommended</span>
            </div>

            <div className="schedule-details">
              <div className="detail">
                <span>Track</span>
                <strong>S01</strong>
              </div>

              <div className="detail">
                <span>Maintenance Window</span>
                <strong>02:00 AM → 05:00 AM</strong>
              </div>

              <div className="detail">
                <span>Duration</span>
                <strong>3 Hours</strong>
              </div>
            </div>

            <div className="impact-section">
              <h3>Estimated Impact</h3>

              <div className="impact-grid">
                <div className="impact-box">
                  <strong>2</strong>
                  <span>Trains Affected</span>
                </div>

                <div className="impact-box">
                  <strong>650</strong>
                  <span>Passengers Affected</span>
                </div>

                <div className="impact-box">
                  <strong>LOW</strong>
                  <span>Disruption Level</span>
                </div>
              </div>
            </div>

            <div className="action-buttons">
              <button
                className="simulate-button"
                onClick={() => setSimulationDone(true)}
              >
                {simulationDone ? "Simulation Complete ✓" : "Simulate Impact"}
              </button>

              <button
                className="approve-button"
                onClick={() => setApproved(true)}
              >
                {approved ? "Block Approved ✓" : "Approve Block"}
              </button>
            </div>
          </section>
        )}

      </main>
    </div>
  );
}

export default App;