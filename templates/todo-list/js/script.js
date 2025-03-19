// TODO: Get DOM elements
const todoForm = document.getElementById("todo-form");
const todoInput = document.getElementById("todo-input");
const todoList = document.getElementById("todo-list");

// TODO: Load todos from localStorage
let todos = [];

// TODO: Save todos to localStorage
function saveTodos() {
  // TODO: Implement saving todos to localStorage
}

// TODO: Create new todo item
function createTodoElement(todo) {
  // TODO: Create list item element
  // TODO: Add todo text
  // TODO: Add delete button
  // TODO: Add event listeners for completion and deletion
  // TODO: Return the created element
}

// TODO: Add new todo
function addTodo(e) {
  // TODO: Prevent form submission
  // TODO: Get and validate input
  // TODO: Create new todo object
  // TODO: Add to todos array
  // TODO: Save to localStorage
  // TODO: Add to DOM
  // TODO: Clear input
}

// TODO: Toggle todo completion
function toggleTodo(id) {
  // TODO: Find todo by id
  // TODO: Toggle completed status
  // TODO: Save to localStorage
  // TODO: Update DOM
}

// TODO: Delete todo
function deleteTodo(id) {
  // TODO: Remove from todos array
  // TODO: Save to localStorage
  // TODO: Remove from DOM
}

// TODO: Initialize todo list
function initTodoList() {
  // TODO: Load todos from localStorage
  // TODO: Clear existing list
  // TODO: Add all todos to DOM
}

// TODO: Add event listeners
todoForm.addEventListener("submit", addTodo);

// Initialize the todo list
initTodoList();
