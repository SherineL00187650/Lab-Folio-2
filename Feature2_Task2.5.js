// Required packages
const express = require('express');
const fs = require('fs');
const app = express();

app.use(express.json());

const DATA_FILE = 'userProgress.json';

// Load progress data from file
function loadProgress() {
    if (fs.existsSync(DATA_FILE)) {
        const data = fs.readFileSync(DATA_FILE);
        return JSON.parse(data);
    } else {
        return { credits: 0, hintsUnlocked: {}, currentQuestion: 0 };
    }
}

// Save progress data to file
function saveProgress(data) {
    fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

// Route to get user progress
app.get('/progress', (req, res) => {
    const progress = loadProgress();
    res.json(progress);
});

// Route to update user progress
app.post('/progress', (req, res) => {
    const progress = loadProgress();
    const { credits, hintsUnlocked, currentQuestion } = req.body;

    progress.credits = credits || progress.credits;
    progress.hintsUnlocked = hintsUnlocked || progress.hintsUnlocked;
    progress.currentQuestion = currentQuestion || progress.currentQuestion;

    saveProgress(progress);
    res.json({ status: 'Progress saved' });
});

// Route to reset user progress
app.post('/progress/reset', (req, res) => {
    const defaultProgress = { credits: 0, hintsUnlocked: {}, currentQuestion: 0 };
    saveProgress(defaultProgress);
    res.json({ status: 'Progress reset' });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
