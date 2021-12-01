const accountDeleteModal = document.getElementById('accountDeleteModal')
accountDeleteModal.addEventListener('show.bs.modal', function (event){
    let button = event.relatedTarget;
    let toHref = button.getAttribute('data-bs-href');
    let accountName = button.getAttribute('data-bs-title');
    let modalButton = accountDeleteModal.querySelector('.btn-delete-account-ok');
    let modalAccountName = accountDeleteModal.querySelector('#account_name')
    modalButton.setAttribute('action', toHref);
    modalAccountName.textContent = accountName;
})

const accountCreateModal = document.getElementById('accountCreateModal')
accountCreateModal.addEventListener('show.bs.modal', async function (){
    const contentDiv = accountCreateModal.querySelector('.modal-content');
    const response = await fetch('/account/create/');
    contentDiv.innerHTML = await response.text();
})

const operationCreateModal = document.getElementById('operationCreateModal')
operationCreateModal.addEventListener('show.bs.modal', async function (){
    const contentDiv = operationCreateModal.querySelector('.modal-content');
    const response = await fetch('/account/create/operation/');
    contentDiv.innerHTML = await response.text();
})