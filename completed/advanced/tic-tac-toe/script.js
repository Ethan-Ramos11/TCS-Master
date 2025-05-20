const cells = document.querySelectorAll(".cell");
const resetButton = document.getElementById("reset");

let currentToken = "X";
let board = ["", "", "", "", "", "", "", "", ""];
cells.forEach((cell) => {
  cell.addEventListener("click", handleCellClick);
});

resetButton.addEventListener("click", () => {});

function handleCellClick(e) {
  const index = e.target.getAttribute("data-index");
  if (board[index] === "") {
    board[index] = currentToken;
  }
}
