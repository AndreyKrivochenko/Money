const accountDeleteModal = document.getElementById('accountDeleteModal')
accountDeleteModal.addEventListener('show.bs.modal', function (event) {
    let button = event.relatedTarget;
    let toHref = button.getAttribute('data-bs-href');
    let accountName = button.getAttribute('data-bs-title');
    let modalButton = accountDeleteModal.querySelector('.btn-delete-account-ok');
    let modalAccountName = accountDeleteModal.querySelector('#account_name')
    modalButton.setAttribute('action', toHref);
    modalAccountName.textContent = accountName;
})

const accountCreateModal = document.getElementById('accountCreateModal')
accountCreateModal.addEventListener('show.bs.modal', async function () {
    const contentDiv = accountCreateModal.querySelector('.modal-content');
    const response = await fetch('/account/create/');
    contentDiv.innerHTML = await response.text();
})

function select() {
    const select = document.querySelector('#id_category');
    select.onchange = function () {
        let indexSelected = select.selectedIndex,
            option = select.querySelectorAll('option')[indexSelected];
        let selectedValue = option.getAttribute('value');
        let newUnits = [];
        for (let i = 0; i < category.length; i++) {
            if (category[i].fields.category == selectedValue) {
                let obj = {
                    'id': category[i].pk,
                    'name': category[i].fields.name
                };
                newUnits.push(obj);
            }
        }
        let newHtml = '<option value="" selected="">Выберите расход/доход</option>';
        for (let i = 0; i < newUnits.length; i++) {
            newHtml += `<option value="${newUnits[i].id}">${newUnits[i].name}</option>`
        }
        document.getElementById('id_category_unit').innerHTML = newHtml;
    }
}

const operationCreateModalPrihod = document.getElementById('operationCreateModalPrihod')
operationCreateModalPrihod.addEventListener('show.bs.modal', async function () {
    const contentDiv = operationCreateModalPrihod.querySelector('.modal-content');
    const response = await fetch('/account/create/operation/?key=1');
    contentDiv.innerHTML = await response.text();

    $(function () {
        $('#id_data').datepicker({
            format: 'dd-mm-yyyy',
            language: 'ru',
            todayHighlight: true,
        });
    });

    select()
})

const operationCreateModalRashod = document.getElementById('operationCreateModalRashod')
operationCreateModalRashod.addEventListener('show.bs.modal', async function () {
    const contentDiv = operationCreateModalRashod.querySelector('.modal-content');
    const response = await fetch('/account/create/operation/?key=2');
    contentDiv.innerHTML = await response.text();

    $(function () {
        $('#id_data').datepicker({
            format: 'dd-mm-yyyy',
            language: 'ru',
            todayHighlight: true,
        });
    });

    select()
})

operationCreateModalRashod.addEventListener('hidden.bs.modal', function () {
    document.getElementById('operation-create-form').innerHTML = ''
})

operationCreateModalPrihod.addEventListener('hidden.bs.modal', function () {
    document.getElementById('operation-create-form').innerHTML = ''
})