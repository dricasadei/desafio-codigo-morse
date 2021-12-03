function submitOnEnter(event) {
  console.log("veio aqui");
  if (event.which === 13) {
    console.log("veio aqui 2");
    document.getElementById("morseForm").submit();
    event.preventDefault(); // Prevents the addition of a new line in the text field (not needed in a lot of cases)
  }
}
let textarea = document.getElementById("morseTextArea");
if (textarea !== null) {
  textarea.addEventListener("keypress", submitOnEnter);
}
