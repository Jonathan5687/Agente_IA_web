document.addEventListener('DOMContentLoaded', () => {
      // Obtener referencias a los elementos del DOM
      const agregarCafeForm = document.getElementById('agregar-cafe');
      const cafeTableBody = document.getElementById('cafe-table').getElementsByTagName('tbody')[0];
      const agregarIngredienteForm = document.getElementById('agregar-ingrediente');
      const ingredienteTableBody = document.getElementById('ingrediente-table').getElementsByTagName('tbody')[0];
      const realizarVentaForm = document.getElementById('realizar-venta');
      const cafeSelect = document.getElementById('cafeId');

      // Función para agregar un nuevo café
      function agregarCafe() {
        const nombreCafe = agregarCafeForm['nombreCafe'].value;
        const precio = parseFloat(agregarCafeForm['precio'].value);
        const newRow = cafeTableBody.insertRow();
        newRow.innerHTML = `
          <td>${nombreCafe}</td>
          <td>$${precio.toFixed(2)}</td>
          <td><button onclick="eliminarFila(this)">Eliminar</button></td>
        `;
      }

      // Función para agregar un nuevo ingrediente
      function agregarIngrediente() {
        const nombreIngrediente = agregarIngredienteForm['nombreIngrediente'].value;
        const stock = parseInt(agregarIngredienteForm['stock'].value);
        const newRow = ingredienteTableBody.insertRow();
        newRow.innerHTML = `
          <td>${nombreIngrediente}</td>
          <td>${stock}</td>
          <td><button onclick="eliminarFila(this)">Eliminar</button></td>
        `;
      }

      // Función para eliminar una fila
      function eliminarFila(button) {
        const row = button.parentNode.parentNode;
        cafeTableBody.deleteRow(row.rowIndex);
      }

      // Llenar el select con los nombres de los cafés
      fetch('cafe.json')
        .then(response => response.json())
        .then(data => {
          data.forEach(cafes => {
            const option = document.createElement('option');
            option.value = cafes.id;
            option.text = cafes.nombre;
            cafeSelect.appendChild(option);
          });
        });

      // Event listeners para el formulario de agregar café
      agregarCafeForm.addEventListener('submit', (event) => {
        event.preventDefault();
        agregarCafe();
      });

      // Event listeners para el formulario de agregar ingrediente
      agregarIngredienteForm.addEventListener('submit', (event) => {
        event.preventDefault();
        agregarIngrediente();
      });

      // Event listener para el formulario de realizar venta
      realizarVentaForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const cafeId = cafeSelect.value;
        const cantidadVendida = parseInt(realizarVentaForm['cantidadVendida'].value);
        
        // Aquí podrías implementar la lógica para realizar una venta y actualizar el stock
        console.log(`Se vendió ${cantidadVendida} unidades del café con ID: ${cafeId}`);
      });
    });