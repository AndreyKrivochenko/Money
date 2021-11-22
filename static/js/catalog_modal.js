const catalogCreateModal = document.getElementById('catalogCreateModal');
catalogCreateModal.addEventListener('show.bs.modal', async function (){
    const contentDiv = catalogCreateModal.querySelector('.modal-content');
    const response = await fetch('/catalog/create/');
    contentDiv.innerHTML = await response.text();
})

const catalogUnitCreateModal = document.getElementById('catalogUnitCreateModal');
catalogUnitCreateModal.addEventListener('show.bs.modal', async function (event){
    const button = event.relatedTarget;
    const href = button.getAttribute('href');
    const contentDiv = catalogUnitCreateModal.querySelector('.modal-content');
    const response = await fetch(href);
    contentDiv.innerHTML = await response.text();
    const form = document.getElementById('createUnitCategoryModalForm');
    form.setAttribute('action', href)
})