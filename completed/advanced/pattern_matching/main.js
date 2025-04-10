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
  flippedCards = [];
  matchedPairs = 0;
  moves = 0;
  gameActive = true;
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

function createCards() {
  gameBoard.innerHTML = "";

  let cardSymbols = [...SYMBOLS, ...SYMBOLS];
  cardSymbols.sort(() => Math.random() - 0.5);

  cards = cardSymbols.map((symbol, index) => {
    const card = document.createElement("div");
    card.className = "card";
    card.dataset.symbol = symbol;
    card.dataset.index = index;
    card.textContent = symbol;
    card.addEventListener("click", flipCard);
    gameBoard.appendChild(card);
    return card;
  });
}

function flipCard() {
  if (
    !gameActive ||
    this.classList.contains("flipped") ||
    this.classList.contains("matched")
  ) {
    return;
  }
  this.classList.add("flipped");
  flippedCards.push(this);

  if (flippedCards.length === 2) {
    moves++;
    movesDisplay.textContent = moves;

    if (flippedCards[0].dataset.symbol === flippedCards[1].dataset.symbol) {
      handleMatch();
    } else {
      handleMisMatch();
    }
  }
}

function handleMatch() {
  flippedCards.forEach((card) => {
    card.classList.add("matched");
    card.removeEventListener("click", flipCard);
  });

  matchedPairs++;
  matchesDisplay.textContent = matchedPairs;

  if (matchedPairs === SYMBOLS.length) {
    endGame();
  }
  flippedCards = [];
}

function handleMisMatch() {
  gameActive = false;
  setTimeout(() => {
    flippedCards.forEach((card) => card.classList.remove("flipped"));
    flippedCards = [];
    gameActive = true;
  }, 1000);
}

function endGame() {
  messageDisplay.textContent = `Congratulations! You won in ${moves} moves and ${timer} seconds!`;

  clearInterval(timer);

  gameActive = false;
}
