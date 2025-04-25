// Obtener el botón y el elemento body
const darkModeToggle = document.getElementById("darkModeToggle");
const body = document.body;

// Comprobar si el modo oscuro está habilitado previamente
const darkModeEnabled = localStorage.getItem("darkMode") === "enabled";

// Función para activar el modo oscuro
const enableDarkMode = () => {
  body.classList.add("dark-mode");
  localStorage.setItem("darkMode", "enabled");
  darkModeToggle.textContent = "Modo Claro"; // Cambiar el texto del botón
};

// Función para desactivar el modo oscuro
const disableDarkMode = () => {
  body.classList.remove("dark-mode");
  localStorage.setItem("darkMode", "disabled");
  darkModeToggle.textContent = "Modo Oscuro"; // Cambiar el texto del botón
};

// Cambiar el estado de modo oscuro al hacer clic
darkModeToggle.addEventListener("click", () => {
  if (body.classList.contains("dark-mode")) {
    disableDarkMode();
  } else {
    enableDarkMode();
  }
});

// Si el modo oscuro está habilitado previamente, activarlo
if (darkModeEnabled) {
  enableDarkMode();
}
