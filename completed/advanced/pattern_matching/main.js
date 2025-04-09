const SYMBOLS = ["★", "♦", "♠", "♣", "♥", "●", "◆", "▲"];
let cards = [];
let flippedCards = [];
let matchedPairs = 0;
let moves = 0;
let gameActive = false;
let timer = 0;
let timeInterval;

const gameBoard = document.getElementById("game-board");
const startButton = document.getElementById("start-button");
const movesDisplay = document.getElementById("moves");
const matchesDisplay = document.getElementById("matches");
const timerDisplay = document.getElementById("timer");
const messageDisplay = document.getElementById("message");

startButton.addEventListener("click", startGame);

