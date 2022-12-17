const submitButton = document.getElementById("submit-button");
const uploadButton = document.getElementById("upload-button");
const inputButton = document.getElementById("input-file");

uploadButton.addEventListener("click", () => {
    inputButton.click();
})

inputButton.addEventListener("change", (event) => {
    submitButton.click();
})