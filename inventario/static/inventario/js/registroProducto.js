document.addEventListener('DOMContentLoaded', function () {
  const categoriaSelect = document.getElementById('id_categoria');
  const vencimientoGroup = document.getElementById('fecha-vencimiento-group');
  const fechaVencimientoInput = document.getElementById('id_fecha_vencimiento');
  const stockInput = document.getElementById('id_stock');
  const stockMinimoInput = document.getElementById('id_stock_minimo');
  const alertaError = document.getElementById('alerta-error');
  const form = document.querySelector('form');

  function mostrarFechaSiEsLubricante() {
    const selectedOption = categoriaSelect.options[categoriaSelect.selectedIndex];
    const categoriaTexto = selectedOption ? selectedOption.text.toLowerCase().trim() : "";

    if (categoriaTexto.includes("lubricante") && categoriaTexto.includes("vencimiento")) {
      vencimientoGroup.style.display = 'block';
    } else {
      vencimientoGroup.style.display = 'none';
      if (fechaVencimientoInput) fechaVencimientoInput.value = "";
    }
  }

  function mostrarAlerta(mensaje) {
    alertaError.textContent = mensaje;
    alertaError.classList.remove('d-none');
    alertaError.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function ocultarAlerta() {
    alertaError.classList.add('d-none');
    alertaError.textContent = '';
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

    if (categoriaTexto.includes("lubricante") && categoriaTexto.includes("vencimiento")) {
      if (!fechaVencimiento) {
        event.preventDefault();
        mostrarAlerta("Debe seleccionar una fecha de vencimiento para productos de categoria: Lubricantes con vencimiento.");
        return;
      }
    }
  }

  if (categoriaSelect) {
    mostrarFechaSiEsLubricante();
    categoriaSelect.addEventListener('change', mostrarFechaSiEsLubricante);
  }

  if (form) {
    form.addEventListener('submit', validarFormulario);
  }
});
