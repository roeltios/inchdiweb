import React, { useState } from "react";
import axios from "axios";
import {
  Container,
  Typography,
  Button,
  Card,
  CardContent,
  Box,
  Stack,
} from "@mui/material";

function App() {
  const [taskChallenge, setTaskChallenge] = useState("");
  const [performanceChallenge, setPerformanceChallenge] = useState("");
  const [visibleCard, setVisibleCard] = useState(null); // "task", "performance", or null

  const getTaskChallenge = async () => {
    try {
      const res = await axios.get("http://localhost:5000/api/reto");
      setTaskChallenge(res.data.reto);
      setVisibleCard("task");
    } catch (err) {
      setTaskChallenge("⚠️ Could not generate TASK challenge. Try again.");
      setVisibleCard("task");
    }
  };

  const getPerformanceChallenge = async () => {
    try {
      const res = await axios.get("http://localhost:5000/api/performance");
      setPerformanceChallenge(res.data.challenge);
      setVisibleCard("performance");
    } catch (err) {
      setPerformanceChallenge("⚠️ Could not generate PERFORMANCE challenge. Try again.");
      setVisibleCard("performance");
    }
  };

  return (
    <Container maxWidth="md" sx={{ mt: 6, textAlign: "center" }}>
      <Typography variant="h4" gutterBottom>
        🎭 Instant Challenge Generator
      </Typography>

      <Stack spacing={2} direction="row" justifyContent="center" sx={{ mb: 4 }}>
        <Button variant="contained" onClick={getTaskChallenge}>
          Generate TASK
        </Button>
        <Button variant="contained" color="secondary" onClick={getPerformanceChallenge}>
          Generate PERFORMANCE
        </Button>
      </Stack>

      {visibleCard === "task" && (
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              🛠 TASK Challenge
            </Typography>
            <Typography>{taskChallenge}</Typography>
          </CardContent>
        </Card>
      )}

      {visibleCard === "performance" && (
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              🎬 PERFORMANCE Challenge
            </Typography>
            <Typography>{performanceChallenge}</Typography>
          </CardContent>
        </Card>
      )}
    </Container>
  );
}

export default App;
