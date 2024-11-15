//Arquivo do script da etapa de "duvidas" do jogo
function infoBtn() {
  const duvida = document.querySelector(".info-text");

  if (duvida.style.display === "none" || duvida.style.display === "") {
    duvida.style.display = "block";
  } else {
    duvida.style.display = "none";
  }
}
