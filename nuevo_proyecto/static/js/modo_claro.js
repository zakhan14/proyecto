document.getElementById("modo-btn").addEventListener(`click`, function () {
    document.body.classList.toggle(`dark-mode`);
    if (document.getElementById(`modo-btn`).textContent == "🌙 Modo Oscuro")
      document.getElementById(`modo-btl`).textContent = "🔆 Modo claro";
    else {
      document.getElementById(`modo-btn`).textContent = "🌙 Modo Oscuro";
    }
  });
  
  const textos = {
    es: {
      titulo: "Mi Pagina",
      contacto: "Contacto",
      nombre: "nombre",
      email: "E-mail",
      mensaje: "mensaje",
    },
    en: {
      titulo: "My Page",
      contacto: "Contact",
      nombre: "Name",
      email: "E-Mail",
      mensaje: "Message",
    },
  };
  let idioma = "es";
  document.getElementById("lang-btn").addEventListener(`click`, function () {
    if (idioma == "es") {
      idioma = "en";
    } else {
      idioma = "es";
    }
    document.getElementById("Titulo").textContent = textos[idioma].titulo;
    document.getElementById("contacto").textContent = textos[idioma].contacto;
    document.getElementById("label-nombre").textContent = textos[idioma].nombre;
    document.getElementById("label-email").textContent = textos[idioma].email;
    document.getElementById("label-mensaje").textContent = textos[idioma].mensaje;
    document.getElementById("lang-btn").innerHTML =
      idioma === "es"
        ? `<img src="https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg" alt="UK Flag" width="30" height="20">`
        : `<img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg" alt="ES Flag" width="30" height="20">`;
  });
  