async function cargarCorazon() {
    const response = await fetch("heart_pattern.txt");
    const text = await response.text();
    return text;
}

function romantizar(nombre, patron) {
    const letras = [...nombre];
    let i = 0;
    let resultado = patron;

    while (resultado.includes("@")) {
        resultado = resultado.replace("@", letras[i % letras.length]);
        i++;
    }
    return resultado;
}

async function generar() {
    const nombre = document.getElementById("nombre").value.trim() || "Amor";
    const patron = await cargarCorazon();
    const corazon = romantizar(nombre, patron);

    const salida = document.getElementById("salida");
    salida.textContent = corazon;
}
