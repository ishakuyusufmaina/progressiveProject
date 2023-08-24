
const intface = document.getElementById("interface");
const board = document.getElementById("board");
intface.addEventListener("input", ()=>{
    board.innerHTML = intface.textContent;
})
