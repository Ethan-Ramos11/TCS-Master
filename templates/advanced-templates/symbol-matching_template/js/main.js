// TODO: Define game constants
const SYMBOLS = []; // TODO: Add symbols for the game
let cards = [];
let flippedCards = [];
let matchedPairs = 0;
let moves = 0;
let gameActive = false;
let timer = 0;
let timerInterval;

// TODO: Get DOM elements
const gameBoard = document.getElementById("game-board");
const startButton = document.getElementById("start-button");
const movesDisplay = document.getElementById("moves");
const matchesDisplay = document.getElementById("matches");
const timerDisplay = document.getElementById("timer");
const messageDisplay = document.getElementById("message");

// TODO: Add event listeners
startButton.addEventListener("click", startGame);

// TODO: Implement game functions
function startGame() {
  // TODO: Reset game state
  // TODO: Initialize timer
  // TODO: Create and shuffle cards
}

function createCards() {
  // TODO: Clear game board
  // TODO: Create card elements
  // TODO: Add event listeners to cards
  // TODO: Shuffle cards
}

function flipCard() {
  // TODO: Handle card flipping logic
  // TODO: Check for matches
  // TODO: Update game state
}

function handleMatch() {
  // TODO: Mark cards as matched
  // TODO: Update score
  // TODO: Check for win condition
}

function handleMisMatch() {
  // TODO: Flip cards back
  // TODO: Add delay before next move
}

function endGame() {
  // TODO: Display win message
  // TODO: Stop timer
  // TODO: Disable further moves
}
