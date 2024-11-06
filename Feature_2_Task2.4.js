// Questions and hints data
const questions = [
    {
        question: "What is the name of the protagonist in BOTW?",
        options: ["Link", "Zelda", "Ganondorf", "Mipha"],
        answer: "Link",
        hints: [
            "He wears a green tunic traditionally.",
            "He often uses the Master Sword.",
            "He is the main hero of the Zelda series."
        ]
    },
    {
        question: "Which divine beast is located in the Gerudo Desert?",
        options: ["Vah Ruta", "Vah Naboris", "Vah Medoh", "Vah Rudania"],
        answer: "Vah Naboris",
        hints: [
            "This beast has a camel-like appearance.",
            "It is associated with the Gerudo tribe.",
            "Its champion is Urbosa."
        ]
    }
    // Add more questions as needed
];

let currentQuestionIndex = 0;
let credits = 0;

// DOM Elements
const questionEl = document.getElementById('question');
const optionsContainer = document.getElementById('options-container');
const creditsEl = document.getElementById('credits');
const hintsContainer = document.getElementById('hints-container');
const unlockHintButton = document.getElementById('unlock-hint-button');

// Load the current question
function loadQuestion() {
    const currentQuestion = questions[currentQuestionIndex];
    questionEl.textContent = currentQuestion.question;
    optionsContainer.innerHTML = ''; // Clear previous options
    hintsContainer.innerHTML = ''; // Clear previous hints

    currentQuestion.options.forEach(option => {
        const button = document.createElement('button');
        button.textContent = option;
        button.classList.add('option-button');
        button.addEventListener('click', () => checkAnswer(option, currentQuestion.answer));
        optionsContainer.appendChild(button);
    });

    updateCreditsDisplay();
}

// Function to check answer correctness and assign credits
function checkAnswer(selectedOption, correctAnswer) {
    if (selectedOption === correctAnswer) {
        credits += 10; // Earn 10 credits for a correct answer
        alert("Correct! You've earned 10 credits.");
    } else {
        alert("Incorrect! Try again.");
    }
    updateCreditsDisplay();
}

// Update credits display
function updateCreditsDisplay() {
    creditsEl.textContent = `Credits: ${credits}`;
}

// Unlock hints in stages based on credits
function unlockHint() {}
    const currentQuestion = questions[currentQuestionIndex];
    const hintCost = 5; // Set the cost for each hint stage

    // Check if there are hints left to unlock
