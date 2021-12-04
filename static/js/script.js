function submitOnEnter(event) {
  if (event.which === 13) {
    document.getElementById("morseForm").submit();
    event.preventDefault(); // Prevents the addition of a new line in the text field (not needed in a lot of cases)
  }
}
let textarea = document.getElementById("morseTextArea");
if (textarea !== null) {
  textarea.addEventListener("keypress", submitOnEnter);
}
