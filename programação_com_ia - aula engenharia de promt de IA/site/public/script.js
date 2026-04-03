fetch("/produtos")
.then(res => res.json())
.then(produtos => {
    const div = document.getElementById("produtos");

    produtos.forEach(p => {
        div.innerHTML += `
            <div class="card">
                <h3>${p.nome}</h3>
                <p>R$ ${p.preco}</p>
            </div>
        `;
    });
});