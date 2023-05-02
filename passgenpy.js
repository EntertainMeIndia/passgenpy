// Get form elements
const numLettersInput = document.getElementById('num-letters');
const numSymbolsInput = document.getElementById('num-symbols');
const numNumbersInput = document.getElementById('num-numbers');
const generateButton = document.getElementById('generate-button');
const passwordDisplay = document.getElementById('password-display');
const copyButton = document.getElementById('copy-button');

// Generate password
function generatePassword() {
  const numLetters = parseInt(numLettersInput.value);
  const numSymbols = parseInt(numSymbolsInput.value);
  const numNumbers = parseInt(numNumbersInput.value);

  const letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const symbols = '!@#$%^&*()_+~`|}{[]\:;?><,./-='
  const numbers = '0123456789';

  let password = '';

  // Generate letters
  for (let i = 0; i < numLetters; i++) {
    const randomIndex = Math.floor(Math.random() * letters.length);
    password += letters[randomIndex];
  }

  // Generate symbols
  for (let i = 0; i < numSymbols; i++) {
    const randomIndex = Math.floor(Math.random() * symbols.length);
    password += symbols[randomIndex];
  }

  // Generate numbers
  for (let i = 0; i < numNumbers; i++) {
    const randomIndex = Math.floor(Math.random() * numbers.length);
    password += numbers[randomIndex];
  }

  // Shuffle password
  password = password.split('').sort(() => Math.random() - 0.5).join('');

  // Display password
  passwordDisplay.innerText = password;
}

// Copy password to clipboard
function copyPassword() {
  const password = passwordDisplay.innerText;
  navigator.clipboard.writeText(password)
    .then(() => {
      copyButton.innerText = 'Copied!';
      setTimeout(() => {
        copyButton.innerText = 'Copy';
      }, 3000);
    })
    .catch(err => {
      console.error('Failed to copy text: ', err);
    });
}

// Add event listeners
generateButton.addEventListener('click', generatePassword);
copyButton.addEventListener('click', copyPassword);
