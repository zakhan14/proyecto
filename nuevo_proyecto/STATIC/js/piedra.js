const opciones = ["piedra", "papel", "tijeras"];
let playerScore = 0;
let cpuScore = 0;
const maxScore = 10; // puntaje para ganar el juego

//para que el juego arrance con el boton "comenzar"
document.getElementById("comenzar").addEventListener("click", () => {
  document.getElementById("pantalla-inicio").style.display = "none";
  document.getElementById("juego").style.display = "block";
});

// Manejo de elecciones en el juego
document.querySelectorAll(".choice").forEach((boton) => {
  boton.addEventListener("click", () => jugar(boton.id));
});

function jugar(eleccionJugador) {
  const eleccionCPU = opciones[Math.floor(Math.random() * 3)];
  let resultado = "";

  if (eleccionJugador === eleccionCPU) {
    resultado = "¡Empate!";
  } else if (
    (eleccionJugador === "piedra" && eleccionCPU === "tijeras") ||
    (eleccionJugador === "papel" && eleccionCPU === "piedra") ||
    (eleccionJugador === "tijeras" && eleccionCPU === "papel")
  ) {
    resultado = "¡Ganaste! ";
    playerScore++;
  } else {
    resultado = "¡Perdiste! ";
    cpuScore++;
  }

  actualizarInterfaz(eleccionJugador, eleccionCPU, resultado);
  verificarGanador();
}

function actualizarInterfaz(jugador, cpu, resultado) {
  document.getElementById(
    "resultado"
  ).textContent = `Elegiste ${jugador}, CPU eligió ${cpu}. ${resultado}`;
  document.getElementById("player-score").textContent = playerScore;
  document.getElementById("cpu-score").textContent = cpuScore;

  // Calcular el porcentaje de la barra (he tenido que utilizar chatgpt para que se ajustase)
  let playerPercentage = (playerScore / maxScore) * 120;
  let cpuPercentage = (cpuScore / maxScore) * 120;

  // Actualizar las barras de puntuación(he tenido que utilizar chatgpt para que funcionase bien)
  document.getElementById("player-bar").setAttribute("width", playerPercentage);
  document.getElementById("cpu-bar").setAttribute("width", cpuPercentage);
}

// Función para verificar si alguien ha ganado
function verificarGanador() {
  if (playerScore === maxScore) {
    mostrarPantallaFinal(
      "¡Enhorabuena, has podido derrotar al bot! Si quieres probar tu suerte de nuevo dale al boton"
    );
  } else if (cpuScore === maxScore) {
    mostrarPantallaFinal(
      "¡Mala suerte campeón! Si quieres probar de nuevo tu suerte, dale al botón."
    );
  }
}

// Función para mostrar pantalla de fin de juego
function mostrarPantallaFinal(mensaje) {
  document.getElementById("juego").style.display = "none";
  document.getElementById("pantalla-final").style.display = "block";
  document.getElementById("mensaje-final").textContent = mensaje;
}

// Función para reiniciar el juego
document.getElementById("reiniciar").addEventListener("click", () => {
  playerScore = 0;
  cpuScore = 0;
  actualizarInterfaz("piedra", "piedra", "¡Elige una opción!"); // Resetear texto
  document.getElementById("pantalla-final").style.display = "none";
  document.getElementById("juego").style.display = "block";
});
