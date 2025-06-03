document.addEventListener("DOMContentLoaded", function () {
  const categoriaSelect = document.getElementById("id_categoria");
  const vencimientoGroup = document.getElementById("fecha-vencimiento-group");
  const alertaError = document.getElementById("alerta-error");
  const stockInput = document.getElementById("id_stock");
  const stockMinimoInput = document.getElementById("id_stock_minimo");
  const fechaVencimientoInput = document.getElementById("id_fecha_vencimiento");
  const form = document.querySelector("form");

  function mostrarAlerta(mensaje) {
    alertaError.textContent = mensaje;
    alertaError.classList.remove("d-none");
    alertaError.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  function ocultarAlerta() {
    alertaError.classList.add("d-none");
    alertaError.textContent = "";
  }

  function toggleVencimiento() {
    const selectedText = categoriaSelect.options[categoriaSelect.selectedIndex]?.text.toLowerCase().trim();
    if (selectedText === "lubricantes") {
      vencimientoGroup.style.display = "block";
    } else {
      vencimientoGroup.style.display = "none";
    }
  }

  function validarFormulario(event) {
    ocultarAlerta();

    const stock = parseInt(stockInput.value);
    const stockMinimo = parseInt(stockMinimoInput.value);
    const categoriaTexto = categoriaSelect.options[categoriaSelect.selectedIndex]?.text.toLowerCase().trim();
    const fechaVencimiento = fechaVencimientoInput?.value;

    if (!isNaN(stock) && !isNaN(stockMinimo) && stock < stockMinimo) {
      event.preventDefault();
      mostrarAlerta(`El stock (${stock}) no puede ser menor al stock mínimo (${stockMinimo}).`);
      return;
    }

    if (categoriaTexto === "lubricantes" && !fechaVencimiento) {
      event.preventDefault();
      mostrarAlerta("Debe seleccionar una fecha de vencimiento para productos de categoría: Lubricantes.");
      return;
    }
  }

  if (categoriaSelect && vencimientoGroup && form) {
    toggleVencimiento();
    categoriaSelect.addEventListener("change", toggleVencimiento);
    form.addEventListener("submit", validarFormulario);
  } else {
    console.log("Algunos elementos no se encontraron en el DOM.");
  }
});
