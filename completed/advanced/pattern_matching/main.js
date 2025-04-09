const SYMBOLS = ["★", "♦", "♠", "♣", "♥", "●", "◆", "▲"];
let cards = [];
let flippedCards = [];
let matchedPairs = 0;
let moves = 0;
let gameActive = false;
let timer = 0;
let timerInterval;

const gameBoard = document.getElementById("game-board");
const startButton = document.getElementById("start-button");
const movesDisplay = document.getElementById("moves");
const matchesDisplay = document.getElementById("matches");
const timerDisplay = document.getElementById("timer");
const messageDisplay = document.getElementById("message");

startButton.addEventListener("click", startGame);

function startGame() {
  let flippedCards = [];
  let matchedPairs = 0;
  let moves = 0;
  let gameActive = True;
  let timer = 0;

  movesDisplay.textContent = "0";
  matchesDisplay.textContent = "0";
  timerDisplay.textContent = "0";
  messageDisplay.textContent = "";

  clearInterval(timerInterval);
  timerInterval = setInterval(() => {
    timer++;
    timerDisplay.textContent = timer;
  }, 1000);

  createCards();

  startButton.textContent = "Restart Game";
}

