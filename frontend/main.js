// Función para generar el grid de casillas
function createGrid() {
    const grid = document.getElementById('grid');
    const rows = 5;
    const cols = 8;

    for (let i = 0; i < rows; i++) {
        const row = document.createElement('div');
        row.classList.add('row');

        for (let j = 0; j < cols; j++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            cell.dataset.row = i;
            cell.dataset.col = j;
            cell.addEventListener('click', () => selectCell(cell));
            row.appendChild(cell);
        }

        grid.appendChild(row);
    }
}

// Función para seleccionar una celda como A o B
function selectCell(cell) {
    // Lógica para seleccionar las celdas A y B
    // y marcar las celdas no permitidas
}

// Enviar datos al backend y recibir distancias calculadas
fetch('/calculate', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(gridData)
})
.then(response => response.json())
.then(distances => {
    // Mostrar o utilizar las distancias calculadas
    console.log(distances);
})
.catch(error => console.error(error));

// Llamar a la función para generar el grid
createGrid();