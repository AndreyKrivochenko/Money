let accountDeleteModal = document.getElementById('accountDeleteModal')
accountDeleteModal.addEventListener('show.bs.modal', function (event){
    let button = event.relatedTarget;
    let toHref = button.getAttribute('data-bs-href');
    let modalButton = accountDeleteModal.querySelector('.btn-delete-account-ok');
    modalButton.setAttribute('action', toHref);
})
