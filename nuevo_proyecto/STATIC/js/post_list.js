function cardHTML(post){
    return `
        <div class="tarjeta">
            <h2>${post.title}</h2>
            <p>${post.content.substring(0, 10)}...</p>
            <a href="/posts/${post.pk}">Lee el post</a>

            <ul><p style="font-size: small; margin-top: 10px;">Tags:</p>
            ${post.tags.map(
                t => `<li><a href="/posts_by_tag/${t.id}"><p>${ t.name }</a></li>`
            ).join('')}
            </ul>
        </div>`;
}

function loadPost(page = 1){
    fetch(`/api/posts/?page=${page}`)
        .then(r => r.json())
        .then(json => {
            const lista = Array.isArray(json) ? json : json.results;
            
            const cont = document.querySelector('.grid');
            lista.forEach(p => cont.insertAdjacentHTML('beforeend', cardHTML(p)));
            nextPage = json.next ?? null;
        })
        .catch(err => console.error('Error al cargar:', err));
}

let nextPage = 1;
loadPost()
