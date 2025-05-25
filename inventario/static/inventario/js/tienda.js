document.addEventListener("DOMContentLoaded", function () {
  const botones = document.querySelectorAll(".agregar-carrito");
  const contador = document.getElementById("contador-carrito");
  const modal = document.getElementById("carrito-modal");
  const btnAbrir = document.getElementById("abrir-carrito");
  const contenido = document.getElementById("carrito-contenido");

  // Cargar carrito inicial
  actualizarContador();

  // Agregar al carrito
  botones.forEach(boton => {
    boton.addEventListener("click", function (e) {
      e.preventDefault();
      const id = this.dataset.id;
      const nombre = this.dataset.nombre;
      const precio = parseFloat(this.dataset.precio);
      let carrito = JSON.parse(localStorage.getItem("carrito")) || {};

      if (carrito[id]) {
        carrito[id].cantidad += 1;
      } else {
        carrito[id] = { nombre, precio, cantidad: 1 };
      }

      localStorage.setItem("carrito", JSON.stringify(carrito));
      actualizarContador();
    });
  });

  // Abrir/cerrar carrito
  btnAbrir.addEventListener("click", function () {
    modal.style.display = modal.style.display === "none" ? "block" : "none";
    mostrarCarrito();
  });

  // Mostrar el contenido del carrito
  function mostrarCarrito() {
    let carrito = JSON.parse(localStorage.getItem("carrito")) || {};
    let html = "<ul class='list-group'>";
    let total = 0;

    for (let id in carrito) {
      let item = carrito[id];
      let subtotal = item.precio * item.cantidad;
      total += subtotal;
      html += `
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <div>
            <strong>${item.nombre}</strong><br>
            $${item.precio} x ${item.cantidad} = $${subtotal.toFixed(2)}
          </div>
          <button class="btn btn-danger btn-sm eliminar" data-id="${id}">X</button>
        </li>`;
    }

    html += `</ul><p class="mt-2"><strong>Total:</strong> $${total.toFixed(2)}</p>`;
    contenido.innerHTML = html;

    // Eliminar item
    contenido.querySelectorAll(".eliminar").forEach(btn => {
      btn.addEventListener("click", () => {
        const id = btn.dataset.id;
        let carrito = JSON.parse(localStorage.getItem("carrito")) || {};
        delete carrito[id];
        localStorage.setItem("carrito", JSON.stringify(carrito));
        mostrarCarrito();
        actualizarContador();
      });
    });
  }

  // Actualizar contador
  function actualizarContador() {
    let carrito = JSON.parse(localStorage.getItem("carrito")) || {};
    let cantidad = Object.values(carrito).reduce((acc, el) => acc + el.cantidad, 0);
    contador.textContent = cantidad;
  }
});
