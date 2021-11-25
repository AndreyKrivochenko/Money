const counterpartiesCreateModal = document.getElementById('counterpartiesCreateModal');
counterpartiesCreateModal.addEventListener('show.bs.modal', async function (){
    const contentDiv = counterpartiesCreateModal.querySelector('.modal-content');
    const response = await fetch('/catalog/create/counterparties/');
    contentDiv.innerHTML = await response.text();
});

const catalogCreateModal = document.getElementById('catalogCreateModal');
catalogCreateModal.addEventListener('show.bs.modal', async function (){
    const contentDiv = catalogCreateModal.querySelector('.modal-content');
    const response = await fetch('/catalog/create/');
    contentDiv.innerHTML = await response.text();
});

const catalogUnitCreateModal = document.getElementById('catalogUnitCreateModal');
catalogUnitCreateModal.addEventListener('show.bs.modal', async function (event){
    const button = event.relatedTarget;
    const href = button.getAttribute('href');
    const contentDiv = catalogUnitCreateModal.querySelector('.modal-content');
    const response = await fetch(href);
    contentDiv.innerHTML = await response.text();
    const form = document.getElementById('createUnitCategoryModalForm');
    form.setAttribute('action', href)
});

const categoryDeleteModal = document.getElementById('categoryDeleteModal')
categoryDeleteModal.addEventListener('show.bs.modal', function (event){
    let button = event.relatedTarget;
    let toHref = button.getAttribute('data-bs-href');
    let categoryName = button.getAttribute('data-bs-title');
    let modalButton = categoryDeleteModal.querySelector('.btn-delete-category-ok');
    let modalCategoryName = categoryDeleteModal.querySelector('#category_name')
    modalButton.setAttribute('action', toHref);
    modalCategoryName.textContent = categoryName;
});

const categoryUnitDeleteModal = document.getElementById('categoryUnitDeleteModal')
categoryUnitDeleteModal.addEventListener('show.bs.modal', function (event){
    let button = event.relatedTarget;
    let toHref = button.getAttribute('data-bs-href');
    let categoryUnitName = button.getAttribute('data-bs-title');
    let modalButton = categoryUnitDeleteModal.querySelector('.btn-delete-category-unit-ok');
    let modalCategoryUnitName = categoryUnitDeleteModal.querySelector('#category_unit_name')
    modalButton.setAttribute('action', toHref);
    modalCategoryUnitName.textContent = categoryUnitName;
});