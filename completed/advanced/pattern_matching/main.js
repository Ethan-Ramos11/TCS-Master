/**
 * Array of symbols used in the game. Each symbol appears twice for matching pairs.
 * @type {string[]}
 */
const SYMBOLS = ["★", "♦", "♠", "♣", "♥", "●", "◆", "▲"];
let cards = [];
let flippedCards = [];
let matchedPairs = 0;
let moves = 0;
let gameActive = false;
let timer = 0;
let timerInterval;

// Get DOM elements
const gameBoard = document.getElementById("game-board");
const startButton = document.getElementById("start-button");
const movesDisplay = document.getElementById("moves");
const matchesDisplay = document.getElementById("matches");
const timerDisplay = document.getElementById("timer");
const messageDisplay = document.getElementById("message");

// Add event listeners
startButton.addEventListener("click", startGame);

/**
 * Initializes and starts a new game session.
 * Resets all game state variables, clears the timer, and creates a new set of cards.
 * Updates the UI to reflect the initial game state.
 * Changes the start button text to "Restart Game".
 * @returns {void}
 */
function startGame() {
  flippedCards = [];
  matchedPairs = 0;
  moves = 0;
  gameActive = true;
  timer = 0;

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

/**
 * Creates and shuffles the game cards.
 * Generates pairs of cards with symbols, shuffles them, and adds them to the game board.
 * Sets up event listeners for each card.
 * @returns {void}
 */
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

/**
 * Handles the card flipping logic when a card is clicked.
 * Checks if the card can be flipped (game active, card not already flipped or matched),
 * updates the game state, and checks for matches when two cards are flipped.
 * @this {HTMLElement} - The card element that was clicked
 * @returns {void}
 */
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

/**
 * Handles the logic when two cards match.
 * Marks the matched cards, removes their click event listeners,
 * updates the score, and checks for game completion.
 * @returns {void}
 */
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

/**
 * Handles the logic when two cards don't match.
 * Temporarily disables the game, flips the cards back over after a 1-second delay,
 * and re-enables the game for the next move.
 * @returns {void}
 */
function handleMisMatch() {
  gameActive = false;
  setTimeout(() => {
    flippedCards.forEach((card) => card.classList.remove("flipped"));
    flippedCards = [];
    gameActive = true;
  }, 1000);
}

/**
 * Ends the game and displays the final results.
 * Shows the completion message with moves and time taken,
 * stops the timer, and disables further moves.
 * @returns {void}
 */
function endGame() {
  messageDisplay.textContent = `Congratulations! You won in ${moves} moves and ${timer} seconds!`;

  clearInterval(timerInterval);

  gameActive = false;
}
