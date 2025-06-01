document.addEventListener('DOMContentLoaded', () => {
  function renderChart(id, type) {
    const canvas = document.getElementById(id);
    if (!canvas) return;

    const labels = JSON.parse(canvas.dataset.labels || "[]");
    const data = JSON.parse(canvas.dataset.data || "[]");

    new Chart(canvas, {
      type: type,
      data: {
        labels: labels,
        datasets: [{
          label: id === "graficoCategorias" ? "Categorías de Productos" : "Stock",
          data: data,
          backgroundColor: [
            '#007bff', '#dc3545', '#ffc107', '#28a745',
            '#17a2b8', '#6f42c1', '#fd7e14', '#20c997'
          ]
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: id === "graficoCategorias" ? "Distribución por Categoría" : "Stock de Productos"
          },
          legend: {
            display: type !== "bar"
          }
        },
        scales: type === "bar" ? {
          y: { beginAtZero: true }
        } : {}
      }
    });
  }

  renderChart("graficoCategorias", "pie");
  renderChart("graficoStock", "bar");
});
