// arquivo que receberar o envio das letras pro back e retornarar o feedback

const letraArmazem = [
  "yogute",
  "geladeira",
  "letra",
  "sogra",
  "jujuba",
  "taxa",
];

let tentativas = 0;
let armazemDasLetras = [];

let palavraAleatoria =
  letraArmazem[Math.floor(Math.random() * letraArmazem.length)];

let letraDescoberta = Array(palavraAleatoria.length).fill("_");

function exibirPalavraNova() {
  const palavraExibida = letraDescoberta.join(" ");
  document.getElementById("palavra-text").innerHTML = palavraExibida;
}

function verificarLetra(letraUser) {
  let acerto = false;

  for (let i = 0; i < palavraAleatoria.length; i++) {
    if (palavraAleatoria[i] === letraUser) {
      letraDescoberta[i] = letraUser;
      acerto = true;
    }
  }
  exibirPalavraNova();
  return acerto;
}

function contadorTentativas(letraUser) {
  const numTentativas = document.getElementById("tentativasNum");

  if (!verificarLetra(letraUser)) {
    tentativas++;
  }

  if (tentativas >= 6) {
    alert(`Você perdeu! Palavra oculta: ${palavraAleatoria}`);
    location.reload();
  }
  console.log(tentativas);
  numTentativas.innerHTML = tentativas;
}

function letreroLetras(letraUser) {
  const letrasJaEnviadas = document.getElementById("letrero");
  armazemDasLetras.push(letraUser);

  letrasJaEnviadas.innerHTML = armazemDasLetras;
}

function onClickSubmit() {
  const letraUser = document.getElementById("letra_input").value.toLowerCase();
  document.getElementById("letra_input").value = "";

  if (letraUser && verificarLetra(letraUser)) {
    console.log("Letra correta:", letraUser);
  } else {
    console.log("Letra incorreta ou já descoberta:", letraUser);
  }
  contadorTentativas(letraUser);
  letreroLetras(letraUser);
}

exibirPalavraNova();
