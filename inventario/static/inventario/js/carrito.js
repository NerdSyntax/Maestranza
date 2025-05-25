document.addEventListener("DOMContentLoaded", function () {
  const botonesAgregar = document.querySelectorAll(".agregar-carrito");
  const abrirCarrito = document.getElementById("abrir-carrito");
  const cerrarCarrito = document.getElementById("cerrarCarrito");
  const cartModal = document.getElementById("carrito-modal");
  const contentProducts = document.getElementById("contentProducts");
  const cartCount = document.getElementById("cartCount");
  const totalElement = document.getElementById("total");
  const btnVaciar = document.getElementById("emptyCart");
  const btnComprar = document.getElementById("comprarBtn");

  // Mostrar/Ocultar carrito
  abrirCarrito.addEventListener("click", () => {
    cartModal.style.display = cartModal.style.display === "none" ? "block" : "none";
  });

  cerrarCarrito.addEventListener("click", () => {
    cartModal.style.display = "none";
  });

  // Agregar al carrito
  botonesAgregar.forEach(btn => {
    btn.addEventListener("click", () => {
      const id = btn.dataset.id;
      const nombre = btn.dataset.nombre;
      const precio = parseFloat(btn.dataset.precio);
      const imagen = btn.dataset.img;

      let carrito = JSON.parse(localStorage.getItem("carrito")) || {};

      if (carrito[id]) {
        carrito[id].cantidad += 1;
      } else {
        carrito[id] = { nombre, precio, cantidad: 1, imagen };
      }

      localStorage.setItem("carrito", JSON.stringify(carrito));
      actualizarCarrito();
    });
  });

  // Vaciar carrito
  btnVaciar.addEventListener("click", () => {
    localStorage.removeItem("carrito");
    actualizarCarrito();
  });

  // Comprar (alerta por ahora)
  btnComprar.addEventListener("click", () => {
    const carrito = JSON.parse(localStorage.getItem("carrito")) || {};
    if (Object.keys(carrito).length === 0) {
      alert("El carrito está vacío.");
      return;
    }
    alert("¡Compra realizada con éxito!");
    localStorage.removeItem("carrito");
    actualizarCarrito();
    cartModal.style.display = "none";
  });

  // Actualizar contenido del carrito
  function actualizarCarrito() {
    const carrito = JSON.parse(localStorage.getItem("carrito")) || {};
    let html = "";
    let total = 0;
    let cantidadTotal = 0;

    for (let id in carrito) {
      const item = carrito[id];
      const subtotal = item.precio * item.cantidad;
      total += subtotal;
      cantidadTotal += item.cantidad;

      html += `
        <tr>
          <td><img src="${item.imagen}" style="width: 50px;"></td>
          <td>${item.nombre}</td>
          <td>$${item.precio}</td>
          <td>${item.cantidad}</td>
          <td><button class="btn btn-sm btn-danger eliminar" data-id="${id}">X</button></td>
        </tr>
      `;
    }

    contentProducts.innerHTML = html;
    cartCount.textContent = cantidadTotal;
    totalElement.textContent = total.toFixed(2);

    // Eliminar producto
    document.querySelectorAll(".eliminar").forEach(btn => {
      btn.addEventListener("click", () => {
        const id = btn.dataset.id;
        let carrito = JSON.parse(localStorage.getItem("carrito")) || {};
        delete carrito[id];
        localStorage.setItem("carrito", JSON.stringify(carrito));
        actualizarCarrito();
      });
    });
  }

  // Inicializar
  actualizarCarrito();
});
