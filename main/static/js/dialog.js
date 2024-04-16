let openDialogBtn = document.getElementById("open-dialog-btn");
let closeDialogBtn = document.getElementById("close-dialog-btn");
let dialogOverlay = document.getElementById("dialog-overlay");

openDialogBtn.addEventListener("click", function() {
    dialogOverlay.style.display = "flex";
});

closeDialogBtn.addEventListener("click", function() {
    dialogOverlay.style.display = "none";
});




